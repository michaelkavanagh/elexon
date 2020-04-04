import requests
from datetime import date, datetime
import xml.etree.ElementTree as ET

from .methods import METHODS

ELEXON_URL = 'https://api.bmreports.com/BMRS/'

def __fixup_param(name, klass, options, param):
    optional = 'optional' in options
    default = [x[1] for x in options if isinstance(x, tuple) and x[
        0] == 'default']
    if default:
        default = default[0]
    else:
        default = None
    if param is None:
        if klass is list and default:
            param = default[:]
        else:
            param = default
    return param

def __generate_elexon_method(namespace, method_name, param_data):
    # a required parameter doesn't have 'optional' in the options,
    # and has no tuple option that starts with 'default'
    required = [x for x in param_data if 'optional' not in x[2] and not [
        y for y in x[2] if isinstance(y, tuple) and y and y[0] == 'default']]

    def elexon_method(self, *args, **kwargs):
        params = {}
        for i, arg in enumerate(args):
            params[param_data[i][0]] = arg
        params.update(kwargs)

        for param in required:
            if param[0] not in params:
                raise TypeError("missing parameter %s" % param[0])

        for name, klass, options in param_data:
            if name in params:
                params[name] = __fixup_param(
                    name, klass, options, params[name])

        return self(method_name, params)

    elexon_method.__name__ = method_name
    elexon_method.__doc__ = "Elexon BMRS API call. See https://www.elexon.co.uk/guidance-note/bmrs-api-data-push-user-guide/"

    return elexon_method

class Proxy(object):
    """Represents a "namespace" of Elexon BMRS API calls."""

    def __init__(self, client, name):
        self._client = client
        self._name = name

    def __call__(
            self,
            method=None,
            args=None,
            add_session_args=True):
        # for Django templates
        if method is None:
            return self

        if add_session_args:
            self._client._add_session_args(args)

        return self._client(method, args)

# generate the Elexon BMRS API proxies
def __generate_proxies():
    for namespace in METHODS:
        methods = {}

        for method, param_data in METHODS[namespace].items():
            methods[method] = __generate_elexon_method(
                namespace, method, param_data)

        proxy = type('%sProxy' % namespace.title(), (Proxy,), methods)

        globals()[proxy.__name__] = proxy

__generate_proxies()

class Elexon(object):
    """The Elexon class provides convenient access to Elexon's BMRS API.
    """

    def __init__(self, apikey, service_type = 'xml'):
        self.apikey = apikey
        self.version = 'v1'
        self.service_type = service_type
        self.elexon_url = ELEXON_URL

        for namespace in METHODS:
            self.__dict__[namespace] = eval(
                '%sProxy(self, \'%s\')' %
                (namespace.title(),
                 # 'elexon.%s' %
                 namespace))

    def __call__(self, method = None, args = None):
        """Make a call to Elexon's server."""
        # for Django templates, if this object is called without any arguments
        # return the object itself
        if method is None:
            return self

        return self.__request(method, args)

    def request(self, method, **kwargs):
        args = self._add_session_args(kwargs)
        return self.__request(method, args)

    def __request(self, method, args):
        url = self.get_url( method, self.version )
        request = requests.get( url, params = args)
        request.raise_for_status()
        return self._parse_response(request.text, method)

    def _add_session_args(self, args = None):
        """Adds 'apikey' and 'ServiceType' to args, which are required for all API calls."""
        if args is None:
            args = {}

        args['APIKey'] = self.apikey
        args['ServiceType'] = self.service_type
        return args

    def _parse_response(self, response, method):
        """Parses the response according to the service_type, which should be either 'csv' or 'xml'."""
        if self.service_type == 'xml':
            root = ET.fromstring(response)
            metadata = root.find('./responseMetadata')
            self._check_error(metadata)

            header = root.find('./responseHeader')
            body = root.find('./responseBody')

            parsed_list = []
            for item in body.findall('.//item'):
                item_dict = {}
                for child in item:
                    if child.text is None:
                        item_dict[child.tag] = None
                    elif child.tag == 'activeFlag':
                        item_dict[child.tag] = True if child.text == 'Y' else False
                    else:
                        item_dict[child.tag] = self._convert_type(child.text)

                parsed_list.append(item_dict)

            return parsed_list
        elif self.service_type == 'csv':
            return response
        else:
            raise RuntimeError('Invalid service_type specified.')

    def _check_error(self, metadata):
        """Checks if the given response is an error, and then raises the appropriate exception."""
        httpCode = metadata.find('httpCode').text
        errorType = metadata.find('errorType').text
        description = metadata.find('description').text
        if httpCode != '200':
            raise Exception('Error {} ({}): {}'.format(httpCode, errorType, description))

    def _convert_type(self, s):
        try:
            return int(s)
        except ValueError:
            pass
        try:
            return float(s)
        except ValueError:
            pass
        try:
            return datetime.strptime(s, '%d/%m/%y %H:%M:%S')
        except ValueError:
            pass
        try:
            return datetime.strptime(s, '%d/%m/%y')
        except ValueError:
            pass
        return s

    def get_url(self, report, version):
        return "https://api.bmreports.com/BMRS/{}/{}".format(report.upper(), version)

import xml.etree.ElementTree as ET

import pytest

from elexon import ElexonRawClient
from elexon.exceptions import NoContentException


def test_no_content_exception():
    client = ElexonRawClient(api_key="")

    metadata = ET.fromstring("""
                                <responseMetadata>
                                    <httpCode>204</httpCode>
                                    <errorType>No Content</errorType>
                                    <description>Success But No data available</description>
                                </responseMetadata>    
                            """)

    with pytest.raises(NoContentException):
        client._check_error(metadata)

# Elexon BMRS API

A simple wrapper for the Elexon BMRS API.

## Installing

 1. Install with [pip](https://pip.pypa.io) (recommended):
```Shell
$ pip install elexon
```
 2. Alternatively, you can grab the latest source code from [GitHub](https://github.com/MichaelKavanagh/elexon):
```Shell
$ git clone https://github.com/MichaelKavanagh/elexon.git
$ python setup.py install
```

## Getting Started
 1. Register on the [ELEXON Portal](https://www.elexonportal.co.uk).
 2. Retrieve API Key.
 3. Replace `API_KEY` in the example below with your API Key.
 4. Profit.

## Usage

### Supported Elexon BMRS Reports

For the full list of namespaces, methods, parameters and data types see [methods.py](elexon/methods.py).

### Example

```python
from elexon import ElexonRawClient

api = ElexonRawClient('API_KEY') # available for free from the Elexon Portal

# Actual Aggregated Generation per Type
generation = api.Transparency.B1620(SettlementDate = '2020-01-01', Period = '5')
# Alternatively, use the general request() function by passing the endpoint in with the arguments:
generation = api.request('B1620', SettlementDate = '2020-01-01', Period = '5')
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Further Reading

https://www.elexon.co.uk/guidance-note/bmrs-api-data-push-user-guide/

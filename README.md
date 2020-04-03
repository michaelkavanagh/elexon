# Elexon BMRS API

A simple wrapper for the Elexon BMRS API.

***WIP:*** currently there is zero data validation and raw unparsed `XML` is returned (as a dict)
or the raw `csv` data is returned as a string.

## Installing

```Shell
$ pip install elexon
```

## Getting Started
 1. Register on the [ELEXON Portal](https://www.elexonportal.co.uk).
 2. Retrieve API Key.
 3. Replace `API_KEY` in the example below with your API Key.
 4. Profit.

## Example

```python
from elexon import Elexon

api = Elexon('API_KEY') # available for free from the Elexon Portal

# Actual Aggregated Generation per Type
generation = api.Transparency.B1620(SettlementDate = '2020-01-01', Period = '5')
# Alternatively, use the general request() function by passing the endpoint in with the arguments:
generation = api.request('B1620', SettlementDate = '2020-01-01', Period = '5')
```

## Further Reading

https://www.elexon.co.uk/guidance-note/bmrs-api-data-push-user-guide/

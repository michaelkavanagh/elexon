# https://www.elexon.co.uk/guidance-note/bmrs-api-data-push-user-guide/
import requests
from datetime import datetime

class Elexon(object):
    """The Elexon class provides convenient access to Elexon's BMRS API.
    """

    def __init__(self, apikey=None):
        self.apikey = apikey
        self.version = 'v1'

    def _url(self, report, version):
        return "https://api.bmreports.com/BMRS/{}/{}".format(report.upper(), version)

    def get_stuff(self, report, payload, servicetype):
        payload.update({ 'APIKey': self.apikey, 'ServiceType': servicetype })
        request = requests.get( self._url( report, self.version ), params=payload)
        return request.text

    # Transparency Data and REMIT
    def B1720(self):
        """Amount of Balancing Reserves Under Contract
        """
        pass

    def B1730(self):
        """Prices Of Procured Balancing Reserves
        """
        pass

    def B1740(self):
        """Accepted Aggregated Offers
        """
        pass

    def B1750(self):
        """Activated Balancing Energy
        """
        pass

    def B1760(self):
        """Prices Of Activated Balancing Energy
        """
        pass

    def B1770(self):
        """Imbalance Prices
        """
        pass

    def B1780(self):
        """Aggregated Imbalance Volumes
        """
        pass

    def B1790(self):
        """Financial Expenses and Income For Balancing
        """
        pass

    def B1810(self):
        """CrossBorder Balancing Volumes of Exchanged Bids and Offers
        """
        pass

    def B1820(self):
        """CrossBorder Balancing Prices
        """
        pass

    def B1830(self):
        """Crossborder Balancing Energy Activated
        """
        pass

    def B0610(self):
        """Actual Total Load per Bidding Zone
        """
        pass

    def B0620(self):
        """Day-Ahead Total Load Forecast per Bidding Zone
        """
        pass

    def B0630(self):
        """Week-Ahead Total Load Forecast per Bidding Zone
        """
        pass

    def B0640(self):
        """Month-Ahead Total Load Forecast Per Bidding Zone
        """
        pass

    def B0650(self):
        """Year Ahead Total Load Forecast per Bidding Zone
        """
        pass

    def B0810(self):
        """Year Ahead Forecast Margin
        """
        pass

    def B1410(self):
        """Installed Generation Capacity Aggregated
        """
        pass

    def B1420(self):
        """Installed Generation Capacity per Unit
        """
        pass

    def B1430(self):
        """Day-Ahead Aggregated Generation
        """
        pass

    def B1440(self):
        """Generation forecasts for Wind and Solar
        """
        pass

    def B1610(self):
        """Actual Generation Output per Generation Unit
        """
        pass

    def B1620(self):
        """Actual Aggregated Generation perType
        """
        pass

    def B1630(self):
        """Actual Or Estimated Wind and Solar Power Generation
        """
        pass

    def B0910(self):
        """Expansion and Dismantling Projects
        """
        pass

    def B1320(self):
        """Congestion Management Measures Countertrading
        """
        pass

    def B1330(self):
        """Congestion Management Measures Costs of Congestion Management
        """
        pass

    def B0710(self):
        """Planned Unavailability of Consumption Units
        """
        pass

    def B0720(self):
        """Changes In Actual Availability Of Consumption Units
        """
        pass

    def B1010(self):
        """Planned Unavailability In The Transmission Grid
        """
        pass

    def B1020(self):
        """Changes In Actual Availability In The Transmission Grid
        """
        pass

    def B1030(self):
        """Changes In Actual Availability of OffShore Grid Infrastructure
        """
        pass

    def B1510(self):
        """Planned Unavailability of Generation Units
        """
        pass

    def B1520(self):
        """Changes In Actual Availability of Generation Units
        """
        pass

    def B1530(self):
        """Planned Unavailability of Production Units
        """
        pass

    def B1540(self):
        """Changes In Actual Availability of Production Units
        """
        pass

    def MessageListRetrieval(self):
        """REMIT Flow – Message List Retrieval
        """
        pass

    def MessageDetailRetrieval(self):
        """REMIT Flow – Message Detail Retrieval
        """
        pass

    # Legacy BMRS Data
    # Temperature Data
    # Bid Offer Level Data
    # Credit Default Notice Data
    # System Warnings
    # Balancing Services Adjustment Action Data
    # Balancing Service Adjustment Data
    # Rolling System Frequency
    # Market Index Data
    # Daily energy Volume Data
    # Non BM STOR Instructed Volume Data
    # Applicable Balancing Services Volume Data
    # Rolling System Demand
    # Peak Wind Generation Forecast
    # Wind Generation Forecast and Out-turn Data
    # Generation By Fuel Type (Current)
    # Generation by Fuel Type (24H Instant Data)
    # Half Hourly Outturn Generation by Fuel Type
    # Half Hourly Interconnector Outturn Generation
    # National Output Useable (2-14 Days Ahead)
    # National Output Useable by Fuel Type (2-14 Days Ahead)
    # National Output Useable by Fuel Type and BM Unit (2-14 Days Ahead)
    # National Output Useable (2- 52 Weeks Ahead)
    # National Output Useable by Fuel type (2-52 Weeks Ahead)
    # National Output Useable by Fuel Type and BM Unit (2-52 Weeks Ahead)
    # National Output Useable Data (1 Year)
    # National Output Useable Data (2 Year)
    # National Output Useable Data (3 Year)
    # National Output Useable Data (4 Year)
    # National Output Useable Data (5 Year)
    # Zonal Output Useable (2- 14 Days Ahead)
    # Zonal Output Useable (2-52 Weeks Ahead)
    # Zonal Output Useable Data for 1 Year Ahead
    # Zonal Output Useable Data for 2 Year Ahead
    # Zonal Output Useable Data for 3 Year Ahead
    # Zonal Output Useable Data for 4 Year Ahead
    # Zonal Output Useable Data for 5 Year Ahead
    # Initial Demand Outturn
    # Forecast Day and Day Ahead Margin and Imbalance Data
    # Forecast Day and Day Ahead Demand Data
    # Demand & Surplus Forecast Data (2-14 Days Ahead)
    # Demand & Surplus Forecast Data (2-52 Weeks Ahead)
    # SO-SO Prices (SO-SO)
    # SO SO Trades
    # Peak Demand – Yesterday/Today/Tomorrow
    # Indicative Peak Demand Information (Using Operational Metering Data)
    # System Demand
    # Indicative Triad Demand Information (Using Settlement Metering Data)
    # Physical Data
    # Dynamic Data
    # Derived BM Unit Data
    # Derived System Wide Data
    # Detailed System Prices
    # Market Depth Data
    # Latest Acceptances
    # Historic Acceptances
    # System Messages
    # BM Unit Search
    # System Warning (Today/Tomorrow)
    # System Warning (Historic)
    # Loss of Load Probability
    # Demand Control Instructions
    # STOR Availability Window
    # Trading Unit Delivery Mode
    # Settlement Exchange Rate

    # Replacement Reserve Data
    # RR Bid Data
    # RR Aggregated Information Data
    # RR Activation Data
    # RR Interconnector Schedule
    # RR GB Need Met
    # RR Indicative Cashflow

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
    def TEMP(self):
        """Temperature Data
        """
        pass

    def BOD(self):
        """Bid Offer Level Data
        """
        pass

    def CDN(self):
        """Credit Default Notice Data
        """
        pass

    def SYSWARN(self):
        """System Warnings
        """
        pass

    def DISBSAD(self):
        """Balancing Services Adjustment Action Data
        """
        pass

    def NETBSAD(self):
        """Balancing Service Adjustment Data
        """
        pass

    def FREQ(self):
        """Rolling System Frequency
        """
        pass

    def MID(self):
        """Market Index Data
        """
        pass

    def DEVINDOD(self):
        """Daily energy Volume Data
        """
        pass

    def NONBM(self):
        """Non BM STOR Instructed Volume Data
        """
        pass

    def QAS(self):
        """Applicable Balancing Services Volume Data
        """
        pass

    def ROLSYSDEM(self):
        """Rolling System Demand
        """
        pass

    def WINDFORPK(self):
        """Peak Wind Generation Forecast
        """
        pass

    def WINDFORFUELHH(self):
        """Wind Generation Forecast and Out-turn Data
        """
        pass

    def FUELINSTHHCUR(self):
        """Generation By Fuel Type (Current)
        """
        pass

    def FUELINST(self):
        """Generation by Fuel Type (24H Instant Data)
        """
        pass

    def FUELHH(self):
        """Half Hourly Outturn Generation by Fuel Type
        """
        pass

    def INTERFUELHH(self):
        """Half Hourly Interconnector Outturn Generation
        """
        pass

    def NOU2T14D(self):
        """National Output Useable (2-14 Days Ahead)
        """
        pass

    def FOU2T14D(self):
        """National Output Useable by Fuel Type (2-14 Days Ahead)
        """
        pass

    def UOU2T14D(self):
        """National Output Useable by Fuel Type and BM Unit (2-14 Days Ahead)
        """
        pass

    def NOU2T52W(self):
        """National Output Useable (2- 52 Weeks Ahead)
        """
        pass

    def FOU2T52W(self):
        """National Output Useable by Fuel type (2-52 Weeks Ahead)
        """
        pass

    def UOU2T52W(self):
        """National Output Useable by Fuel Type and BM Unit (2-52 Weeks Ahead)
        """
        pass

    def NOUY1(self):
        """National Output Useable Data (1 Year)
        """
        pass

    def NOUY2(self):
        """National Output Useable Data (2 Year)
        """
        pass

    def NOUY3(self):
        """National Output Useable Data (3 Year)
        """
        pass

    def NOUY4(self):
        """National Output Useable Data (4 Year)
        """
        pass

    def NOUY5(self):
        """National Output Useable Data (5 Year)
        """
        pass

    def ZOU2T14D(self):
        """Zonal Output Useable (2- 14 Days Ahead)
        """
        pass

    def ZOU2T52W(self):
        """Zonal Output Useable (2-52 Weeks Ahead)
        """
        pass

    def ZOUY1(self):
        """Zonal Output Useable Data for 1 Year Ahead
        """
        pass

    def ZOUY2(self):
        """Zonal Output Useable Data for 2 Year Ahead
        """
        pass

    def ZOUY3(self):
        """Zonal Output Useable Data for 3 Year Ahead
        """
        pass

    def ZOUY4(self):
        """Zonal Output Useable Data for 4 Year Ahead
        """
        pass

    def ZOUY5(self):
        """Zonal Output Useable Data for 5 Year Ahead
        """
        pass

    def INDOITSDO(self):
        """Initial Demand Outturn
        """
        pass

    def MELIMBALNGC(self):
        """Forecast Day and Day Ahead Margin and Imbalance Data
        """
        pass

    def FORDAYDEM(self):
        """Forecast Day and Day Ahead Demand Data
        """
        pass

    def DEMMF2T14D(self):
        """Demand & Surplus Forecast Data (2-14 Days Ahead)
        """
        pass

    def DEMMF2T52W(self):
        """Demand & Surplus Forecast Data (2-52 Weeks Ahead)
        """
        pass

    def SOSOP(self):
        """SO-SO Prices (SO-SO)
        """
        pass

    def SOSOT(self):
        """SO SO Trades
        """
        pass

    def PKDEMYESTTDYTOM(self):
        """Peak Demand – Yesterday/Today/Tomorrow
        """
        pass

    def INDPKDEMINFO(self):
        """Indicative Peak Demand Information (Using Operational Metering Data)
        """
        pass

    def SYSDEM(self):
        """System Demand
        """
        pass

    def INDTRIADDEMINFO(self):
        """Indicative Triad Demand Information (Using Settlement Metering Data)
        """
        pass

    def PHYBMDATA(self):
        """Physical Data
        """
        pass

    def DYNBMDATA(self):
        """Dynamic Data
        """
        pass

    def DERBMDATA(self):
        """Derived BM Unit Data
        """
        pass

    def DERSYSDATA(self):
        """Derived System Wide Data
        """
        pass

    def DETSYSPRICES(self):
        """Detailed System Prices
        """
        pass

    def MKTDEPTHDATA(self):
        """Market Depth Data
        """
        pass

    def LATESTACCEPTS(self):
        """Latest Acceptances
        """
        pass

    def HISTACCEPTS(self):
        """Historic Acceptances
        """
        pass

    def SYSMSG(self):
        """System Messages
        """
        pass

    def BMUNITSEARCH(self):
        """BM Unit Search
        """
        pass

    def YSWARNTDYTOM(self):
        """System Warning (Today/Tomorrow)
        """
        pass

    def HISTSYSWARN(self):
        """System Warning (Historic)
        """
        pass

    def LOLPDRM(self):
        """Loss of Load Probability
        """
        pass

    def DEMCI(self):
        """Demand Control Instructions
        """
        pass

    def STORAW(self):
        """STOR Availability Window
        """
        pass

    def TRADINGUNIT(self):
        """Trading Unit Delivery Mode
        """
        pass

    def EURGBFXDATA(self):
        """Settlement Exchange Rate
        """
        pass

    # Replacement Reserve Data
    def RRBidData(self):
        """RR Bid Data
        """
        pass

    def RRAggregatedInfo(self):
        """RR Aggregated Information Data
        """
        pass

    def RRActivation(self):
        """RR Activation Data
        """
        pass

    def RRINTCON(self):
        """RR Interconnector Schedule
        """
        pass

    def RRGBNM(self):
        """RR GB Need Met
        """
        pass

    def RRCashflow(self):
        """RR Indicative Cashflow
        """
        pass

# https://www.elexon.co.uk/guidance-note/bmrs-api-data-push-user-guide/
import requests
from datetime import datetime

class Elexon(object):
    """The Elexon class provides convenient access to Elexon's BMRS API.
    """

    def __init__(self, apikey=None):
        self.apikey = apikey
        self.version = 'v1'

    def __get_url(self, report, version):
        return "https://api.bmreports.com/BMRS/{}/{}".format(report.upper(), version)

    def query(self, report, payload, servicetype='xml'):
        url = self.__get_url( report, self.version )
        payload.update({ 'APIKey': self.apikey, 'ServiceType': servicetype })
        request = requests.get( url, params=payload)
        request.raise_for_status()
        # print(request.url)
        return request.text

    # Transparency Data and REMIT
    def B1720(self, SettlementDate, Period = '*'):
        """Amount of Balancing Reserves Under Contract"""
        endpoint = 'B1720'
        query_parameters = {
            'SettlementDate': SettlementDate,
            'Period': Period
        }
        return self.query(endpoint, query_parameters)

    def B1730(self, SettlementDate, Period = '*'):
        """Prices Of Procured Balancing Reserves"""
        endpoint = 'B1730'
        query_parameters = {
            'SettlementDate': SettlementDate,
            'Period': Period
        }
        return self.query(endpoint, query_parameters)

    def B1740(self, SettlementDate, Period = '*'):
        """Accepted Aggregated Offers"""
        endpoint = 'B1740'
        query_parameters = {
            'SettlementDate': SettlementDate,
            'Period': Period
        }
        return self.query(endpoint, query_parameters)

    def B1750(self, SettlementDate, Period = '*'):
        """Activated Balancing Energy"""
        endpoint = 'B1750'
        query_parameters = {
            'SettlementDate': SettlementDate,
            'Period': Period
        }
        return self.query(endpoint, query_parameters)

    def B1760(self, SettlementDate, Period = '*'):
        """Prices Of Activated Balancing Energy"""
        endpoint = 'B1760'
        query_parameters = {
            'SettlementDate': SettlementDate,
            'Period': Period
        }
        return self.query(endpoint, query_parameters)

    def B1770(self, SettlementDate, Period = '*'):
        """Imbalance Prices"""
        endpoint = 'B1770'
        query_parameters = {
            'SettlementDate': SettlementDate,
            'Period': Period
        }
        return self.query(endpoint, query_parameters)

    def B1780(self, SettlementDate, Period = '*'):
        """Aggregated Imbalance Volumes"""
        endpoint = 'B1780'
        query_parameters = {
            'SettlementDate': SettlementDate,
            'Period': Period
        }
        return self.query(endpoint, query_parameters)

    def B1790(self, Year, Month):
        """Financial Expenses and Income For Balancing"""
        endpoint = 'B1790'
        query_parameters = {
            'Year': Year,
            'Month': Month
        }
        return self.query(endpoint, query_parameters)

    def B1810(self, SettlementDate, Period = '*'):
        """CrossBorder Balancing Volumes of Exchanged Bids and Offers"""
        endpoint = 'B1810'
        query_parameters = {
            'SettlementDate': SettlementDate,
            'Period': Period
        }
        return self.query(endpoint, query_parameters)

    def B1820(self, SettlementDate, Period = '*'):
        """CrossBorder Balancing Prices"""
        endpoint = 'B1820'
        query_parameters = {
            'SettlementDate': SettlementDate,
            'Period': Period
        }
        return self.query(endpoint, query_parameters)

    def B1830(self, SettlementDate, Period = '*'):
        """Crossborder Balancing Energy Activated"""
        endpoint = 'B1830'
        query_parameters = {
            'SettlementDate': SettlementDate,
            'Period': Period
        }
        return self.query(endpoint, query_parameters)

    def B0610(self, SettlementDate, Period = '*'):
        """Actual Total Load per Bidding Zone"""
        endpoint = 'B0610'
        query_parameters = {
            'SettlementDate': SettlementDate,
            'Period': Period
        }
        return self.query(endpoint, query_parameters)

    def B0620(self, SettlementDate, Period = '*'):
        """Day-Ahead Total Load Forecast per Bidding Zone"""
        endpoint = 'B0620'
        query_parameters = {
            'SettlementDate': SettlementDate,
            'Period': Period
        }
        return self.query(endpoint, query_parameters)

    def B0630(self, Year, Week):
        """Week-Ahead Total Load Forecast per Bidding Zone"""
        endpoint = 'B0630'
        query_parameters = {
            'Year': Year,
            'Week': Week
        }
        return self.query(endpoint, query_parameters)

    def B0640(self, Year, Month):
        """Month-Ahead Total Load Forecast Per Bidding Zone"""
        endpoint = 'B0640'
        query_parameters = {
            'Year': Year,
            'Month': Month
        }
        return self.query(endpoint, query_parameters)

    def B0650(self, Year):
        """Year Ahead Total Load Forecast per Bidding Zone"""
        endpoint = 'B0650'
        query_parameters = {
            'Year': Year
        }
        return self.query(endpoint, query_parameters)

    def B0810(self, Year):
        """Year Ahead Forecast Margin"""
        endpoint = 'B0810'
        query_parameters = {
            'Year': Year
        }
        return self.query(endpoint, query_parameters)

    def B1410(self, Year):
        """Installed Generation Capacity Aggregated"""
        endpoint = 'B1410'
        query_parameters = {
            'Year': Year
        }
        return self.query(endpoint, query_parameters)

    def B1420(self, Year):
        """Installed Generation Capacity per Unit"""
        endpoint = 'B1420'
        query_parameters = {
            'Year': Year
        }
        return self.query(endpoint, query_parameters)

    def B1430(self, SettlementDate, Period = '*'):
        """Day-Ahead Aggregated Generation"""
        endpoint = 'B1430'
        query_parameters = {
            'SettlementDate': SettlementDate,
            'Period': Period
        }
        return self.query(endpoint, query_parameters)

    def B1440(self, SettlementDate, Period = '*'):
        """Generation forecasts for Wind and Solar"""
        endpoint = 'B1440'
        query_parameters = {
            'SettlementDate': SettlementDate,
            'Period': Period
        }
        return self.query(endpoint, query_parameters)

    def B1610(self, SettlementDate, NGCBMUnitID, Period = '*'):
        """Actual Generation Output per Generation Unit"""
        endpoint = 'B1610'
        query_parameters = {
            'SettlementDate': SettlementDate,
            'NGCBMUnitID': NGCBMUnitID,
            'Period': Period
        }
        return self.query(endpoint, query_parameters)

    def B1620(self, SettlementDate, Period = '*'):
        """Actual Aggregated Generation perType"""
        endpoint = 'B1620'
        query_parameters = {
            'SettlementDate': SettlementDate,
            'Period': Period
        }
        return self.query(endpoint, query_parameters)

    def B1630(self, SettlementDate, Period = '*'):
        """Actual Or Estimated Wind and Solar Power Generation"""
        endpoint = 'B1630'
        query_parameters = {
            'SettlementDate': SettlementDate,
            'Period': Period
        }
        return self.query(endpoint, query_parameters)

    def B0910(self, Year):
        """Expansion and Dismantling Projects"""
        endpoint = 'B0910'
        query_parameters = {
            'Year': Year
        }
        return self.query(endpoint, query_parameters)

    def B1320(self, SettlementDate, Period = '*'):
        """Congestion Management Measures Countertrading"""
        endpoint = 'B1320'
        query_parameters = {
            'SettlementDate': SettlementDate,
            'Period': Period
        }
        return self.query(endpoint, query_parameters)

    def B1330(self, Year, Month):
        """Congestion Management Measures Costs of Congestion Management"""
        endpoint = 'B1330'
        query_parameters = {
            'Year': Year,
            'Month': Month
        }
        return self.query(endpoint, query_parameters)

    def B0710(self, StartDate, StartTime, EndDate, EndTime):
        """Planned Unavailability of Consumption Units"""
        endpoint = 'B0710'
        query_parameters = {
            'StartDate': StartDate,
            'StartTime': StartTime,
            'EndDate': EndDate,
            'EndTime': EndTime
        }
        return self.query(endpoint, query_parameters)

    def B0720(self, StartDate, StartTime, EndDate, EndTime):
        """Changes In Actual Availability Of Consumption Units"""
        endpoint = 'B0720'
        query_parameters = {
            'StartDate': StartDate,
            'StartTime': StartTime,
            'EndDate': EndDate,
            'EndTime': EndTime
        }
        return self.query(endpoint, query_parameters)

    def B1010(self, StartDate, StartTime, EndDate, EndTime):
        """Planned Unavailability In The Transmission Grid"""
        endpoint = 'B1010'
        query_parameters = {
            'StartDate': StartDate,
            'StartTime': StartTime,
            'EndDate': EndDate,
            'EndTime': EndTime
        }
        return self.query(endpoint, query_parameters)

    def B1020(self, StartDate, StartTime, EndDate, EndTime):
        """Changes In Actual Availability In The Transmission Grid"""
        endpoint = 'B1020'
        query_parameters = {
            'StartDate': StartDate,
            'StartTime': StartTime,
            'EndDate': EndDate,
            'EndTime': EndTime
        }
        return self.query(endpoint, query_parameters)

    def B1030(self, StartDate, StartTime, EndDate, EndTime):
        """Changes In Actual Availability of OffShore Grid Infrastructure"""
        endpoint = 'B1030'
        query_parameters = {
            'StartDate': StartDate,
            'StartTime': StartTime,
            'EndDate': EndDate,
            'EndTime': EndTime
        }
        return self.query(endpoint, query_parameters)

    def B1510(self, StartDate, StartTime, EndDate, EndTime):
        """Planned Unavailability of Generation Units"""
        endpoint = 'B1510'
        query_parameters = {
            'StartDate': StartDate,
            'StartTime': StartTime,
            'EndDate': EndDate,
            'EndTime': EndTime
        }
        return self.query(endpoint, query_parameters)

    def B1520(self, StartDate, StartTime, EndDate, EndTime):
        """Changes In Actual Availability of Generation Units"""
        endpoint = 'B1520'
        query_parameters = {
            'StartDate': StartDate,
            'StartTime': StartTime,
            'EndDate': EndDate,
            'EndTime': EndTime
        }
        return self.query(endpoint, query_parameters)

    def B1530(self, StartDate, StartTime, EndDate, EndTime):
        """Planned Unavailability of Production Units"""
        endpoint = 'B1530'
        query_parameters = {
            'StartDate': StartDate,
            'StartTime': StartTime,
            'EndDate': EndDate,
            'EndTime': EndTime
        }
        return self.query(endpoint, query_parameters)

    def B1540(self, StartDate, StartTime, EndDate, EndTime):
        """Changes In Actual Availability of Production Units"""
        endpoint = 'B1540'
        query_parameters = {
            'StartDate': StartDate,
            'StartTime': StartTime,
            'EndDate': EndDate,
            'EndTime': EndTime
        }
        return self.query(endpoint, query_parameters)

    def MessageListRetrieval(self, EventStart, EventEnd, PublicationFrom, PublicationTo, ParticipantId, MessageID, AssetID, EventType, FuelType, MessageType, UnavailabilityType):
        """REMIT Flow – Message List Retrieval"""
        endpoint = 'MessageListRetrieval'
        query_parameters = {
            'EventStart': EventStart,
            'EventEnd': EventEnd,
            'PublicationFrom': PublicationFrom,
            'PublicationTo': PublicationTo,
            'ParticipantId': ParticipantId,
            'MessageID': MessageID,
            'AssetID': AssetID,
            'EventType': EventType,
            'FuelType': FuelType,
            'MessageType': MessageType,
            'UnavailabilityType': UnavailabilityType
        }
        return self.query(endpoint, query_parameters)

    def MessageDetailRetrieval(self, MessageId, ParticipantId, SequenceId, ActiveFlag):
        """REMIT Flow – Message Detail Retrieval"""
        endpoint = 'MessageDetailRetrieval'
        query_parameters = {
            'MessageId': MessageId,
            'ParticipantId': ParticipantId,
            'SequenceId': SequenceId,
            'ActiveFlag': ActiveFlag
        }
        return self.query(endpoint, query_parameters)

    # Legacy BMRS Data
    def TEMP(self):
        """Temperature Data"""
        pass

    def BOD(self):
        """Bid Offer Level Data"""
        pass

    def CDN(self):
        """Credit Default Notice Data"""
        pass

    def SYSWARN(self):
        """System Warnings"""
        pass

    def DISBSAD(self):
        """Balancing Services Adjustment Action Data"""
        pass

    def NETBSAD(self):
        """Balancing Service Adjustment Data"""
        pass

    def FREQ(self):
        """Rolling System Frequency"""
        pass

    def MID(self, SettlementDate, Period = '*'):
        """Market Index Data"""
        endpoint = 'MID'
        query_parameters = {
            'SettlementDate': SettlementDate,
            'Period': Period
        }
        return self.query(endpoint, query_parameters)

    def DEVINDOD(self):
        """Daily energy Volume Data"""
        pass

    def NONBM(self):
        """Non BM STOR Instructed Volume Data"""
        pass

    def QAS(self):
        """Applicable Balancing Services Volume Data"""
        pass

    def ROLSYSDEM(self):
        """Rolling System Demand"""
        pass

    def WINDFORPK(self):
        """Peak Wind Generation Forecast"""
        pass

    def WINDFORFUELHH(self):
        """Wind Generation Forecast and Out-turn Data"""
        pass

    def FUELINSTHHCUR(self):
        """Generation By Fuel Type (Current)"""
        pass

    def FUELINST(self):
        """Generation by Fuel Type (24H Instant Data)"""
        pass

    def FUELHH(self):
        """Half Hourly Outturn Generation by Fuel Type"""
        pass

    def INTERFUELHH(self):
        """Half Hourly Interconnector Outturn Generation"""
        pass

    def NOU2T14D(self):
        """National Output Useable (2-14 Days Ahead)"""
        pass

    def FOU2T14D(self):
        """National Output Useable by Fuel Type (2-14 Days Ahead)"""
        pass

    def UOU2T14D(self):
        """National Output Useable by Fuel Type and BM Unit (2-14 Days Ahead)"""
        pass

    def NOU2T52W(self):
        """National Output Useable (2- 52 Weeks Ahead)"""
        pass

    def FOU2T52W(self):
        """National Output Useable by Fuel type (2-52 Weeks Ahead)"""
        pass

    def UOU2T52W(self):
        """National Output Useable by Fuel Type and BM Unit (2-52 Weeks Ahead)"""
        pass

    def NOUY1(self):
        """National Output Useable Data (1 Year)"""
        pass

    def NOUY2(self):
        """National Output Useable Data (2 Year)"""
        pass

    def NOUY3(self):
        """National Output Useable Data (3 Year)"""
        pass

    def NOUY4(self):
        """National Output Useable Data (4 Year)"""
        pass

    def NOUY5(self):
        """National Output Useable Data (5 Year)"""
        pass

    def ZOU2T14D(self):
        """Zonal Output Useable (2- 14 Days Ahead)"""
        pass

    def ZOU2T52W(self):
        """Zonal Output Useable (2-52 Weeks Ahead)"""
        pass

    def ZOUY1(self):
        """Zonal Output Useable Data for 1 Year Ahead"""
        pass

    def ZOUY2(self):
        """Zonal Output Useable Data for 2 Year Ahead"""
        pass

    def ZOUY3(self):
        """Zonal Output Useable Data for 3 Year Ahead"""
        pass

    def ZOUY4(self):
        """Zonal Output Useable Data for 4 Year Ahead"""
        pass

    def ZOUY5(self):
        """Zonal Output Useable Data for 5 Year Ahead"""
        pass

    def INDOITSDO(self):
        """Initial Demand Outturn"""
        pass

    def MELIMBALNGC(self):
        """Forecast Day and Day Ahead Margin and Imbalance Data"""
        pass

    def FORDAYDEM(self):
        """Forecast Day and Day Ahead Demand Data"""
        pass

    def DEMMF2T14D(self):
        """Demand & Surplus Forecast Data (2-14 Days Ahead)"""
        pass

    def DEMMF2T52W(self):
        """Demand & Surplus Forecast Data (2-52 Weeks Ahead)"""
        pass

    def SOSOP(self):
        """SO-SO Prices (SO-SO)"""
        pass

    def SOSOT(self):
        """SO SO Trades"""
        pass

    def PKDEMYESTTDYTOM(self):
        """Peak Demand – Yesterday/Today/Tomorrow"""
        pass

    def INDPKDEMINFO(self):
        """Indicative Peak Demand Information (Using Operational Metering Data)"""
        pass

    def SYSDEM(self):
        """System Demand"""
        pass

    def INDTRIADDEMINFO(self):
        """Indicative Triad Demand Information (Using Settlement Metering Data)"""
        pass

    def PHYBMDATA(self):
        """Physical Data"""
        pass

    def DYNBMDATA(self):
        """Dynamic Data"""
        pass

    def DERBMDATA(self):
        """Derived BM Unit Data"""
        pass

    def DERSYSDATA(self):
        """Derived System Wide Data"""
        pass

    def DETSYSPRICES(self):
        """Detailed System Prices"""
        pass

    def MKTDEPTHDATA(self):
        """Market Depth Data"""
        pass

    def LATESTACCEPTS(self):
        """Latest Acceptances"""
        pass

    def HISTACCEPTS(self):
        """Historic Acceptances"""
        pass

    def SYSMSG(self):
        """System Messages"""
        pass

    def BMUNITSEARCH(self):
        """BM Unit Search"""
        pass

    def YSWARNTDYTOM(self):
        """System Warning (Today/Tomorrow)"""
        pass

    def HISTSYSWARN(self):
        """System Warning (Historic)"""
        pass

    def LOLPDRM(self):
        """Loss of Load Probability"""
        pass

    def DEMCI(self):
        """Demand Control Instructions"""
        pass

    def STORAW(self):
        """STOR Availability Window"""
        pass

    def TRADINGUNIT(self):
        """Trading Unit Delivery Mode"""
        pass

    def EURGBFXDATA(self, SettlementDayFrom, SettlementDayTo):
        """Settlement Exchange Rate"""
        endpoint = 'EURGBFXDATA'
        query_parameters = {
            'SettlementDayFrom': SettlementDayFrom,
            'SettlementDayTo': SettlementDayTo
        }
        return self.query(endpoint, query_parameters)

    # Replacement Reserve Data
    def RRBidData(self):
        """RR Bid Data"""
        pass

    def RRAggregatedInfo(self):
        """RR Aggregated Information Data"""
        pass

    def RRActivation(self):
        """RR Activation Data"""
        pass

    def RRINTCON(self):
        """RR Interconnector Schedule"""
        pass

    def RRGBNM(self):
        """RR GB Need Met"""
        pass

    def RRCashflow(self):
        """RR Indicative Cashflow"""
        pass

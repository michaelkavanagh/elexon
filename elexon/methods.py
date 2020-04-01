from datetime import date, time, datetime

METHODS = {
    # Transparency Data
    'Transparency': {
        'B1720': [
            ('SettlementDate', date, []),
            ('Period', str, [])
        ],
        'B1730': [
            ('SettlementDate', date, []),
            ('Period', str, [])
        ],
        'B1740': [
            ('SettlementDate', date, []),
            ('Period', str, [])
        ],
        'B1750': [
            ('SettlementDate', date, []),
            ('Period', str, [])
        ],
        'B1760': [
            ('SettlementDate', date, []),
            ('Period', str, [])
        ],
        'B1770': [
            ('SettlementDate', date, []),
            ('Period', str, [])
        ],
        'B1780': [
            ('SettlementDate', date, []),
            ('Period', str, [])
        ],
        'B1790': [
            ('Year', int, []),
            ('Month', str, [])
        ],
        'B1810': [
            ('SettlementDate', date, []),
            ('Period', str, [])
        ],
        'B1820': [
            ('SettlementDate', date, []),
            ('Period', str, [])
        ],
        'B1830': [
            ('SettlementDate', date, []),
            ('Period', str, [])
        ],
        'B0610': [
            ('SettlementDate', date, []),
            ('Period', str, [])
        ],
        'B0620': [
            ('SettlementDate', date, []),
            ('Period', str, [])
        ],
        'B0630': [
            ('Year', int, []),
            ('Week', int, [])
        ],
        'B0640': [
            ('Year', int, []),
            ('Month', str, [])  # either format MMM or MM(01-12)?
        ],
        'B0650': [
            ('Year', int, [])
        ],
        'B0810': [
            ('Year', int, [])
        ],
        'B1410': [
            ('Year', int, [])
        ],
        'B1420': [
            ('Year', int, [])
        ],
        'B1430': [
            ('SettlementDate', date, []),
            ('Period', str, [])
        ],
        'B1440': [
            ('SettlementDate', date, []),
            ('Period', str, [])
        ],
        'B1610': [
            ('SettlementDate', date, []),
            ('Period', str, []),
            ('NGCBMUnitID', str, [])
        ],
        'B1620': [
            ('SettlementDate', date, []),
            ('Period', str, [])
        ],
        'B1630': [
            ('SettlementDate', date, []),
            ('Period', str, [])
        ],
        'B0910': [
            ('Year', int, [])
        ],
        'B1320': [
            ('SettlementDate', date, []),
            ('Period', str, [])
        ],
        'B1330': [
            ('Year', int, []),
            ('Month', int, [])
        ],
        'B0710': [
            ('StartDate', date, []),
            ('StartTime', time, []),
            ('EndDate', date, []),
            ('EndTime', time, [])
        ],
        'B0720': [
            ('StartDate', date, []),
            ('StartTime', time, []),
            ('EndDate', date, []),
            ('EndTime', time, [])
        ],
        'B1010': [
            ('StartDate', date, []),
            ('StartTime', time, []),
            ('EndDate', date, []),
            ('EndTime', time, [])
        ],
        'B1020': [
            ('StartDate', date, []),
            ('StartTime', time, []),
            ('EndDate', date, []),
            ('EndTime', time, [])
        ],
        'B1030': [
            ('StartDate', date, []),
            ('StartTime', time, []),
            ('EndDate', date, []),
            ('EndTime', time, [])
        ],
        'B1510': [
            ('StartDate', date, []),
            ('StartTime', time, []),
            ('EndDate', date, []),
            ('EndTime', time, [])
        ],
        'B1520': [
            ('StartDate', date, []),
            ('StartTime', time, []),
            ('EndDate', date, []),
            ('EndTime', time, [])
        ],
        'B1530': [
            ('StartDate', date, []),
            ('StartTime', time, []),
            ('EndDate', date, []),
            ('EndTime', time, [])
        ],
        'B1540': [
            ('StartDate', date, []),
            ('StartTime', time, []),
            ('EndDate', date, []),
            ('EndTime', time, [])
        ]
    },

    # REMIT
    'REMIT': {
        'MessageListRetrieval': [
            ('EventStart', date, ['optional']),
            ('EventEnd', date, ['optional']),
            ('PublicationFrom', date, ['optional']),
            ('PublicationTo', date, ['optional']),
            ('ParticipantId', str, ['optional']),
            ('MessageID', str, ['optional']),
            ('AssetID', str, ['optional']),
            ('EventType', str, ['optional']),
            ('FuelType', str, ['optional']),
            ('MessageType', str, ['optional']),
            ('UnavailabilityType', str, ['optional']),
            ('AffectedUnitID', str, ['optional']),
            ('ActiveFlag', str, ['optional'])
        ],
        'MessageDetailRetrieval': [
            ('MessageId', str, []),
            ('ParticipantId', str, []),
            ('SequenceId', str, ['optional']),
            ('ActiveFlag', str, ['optional'])
        ]
    },

    # Legacy BMRS Data
    'Legacy': {
        'TEMP': [
            ('FromDate', date, ['optional']),
            ('ToDate', date, ['optional'])
        ],
        'BOD': [
            ('SettlementDate', date, ['optional']),
            ('SettlementPeriod', str, ['optional']),
            ('BMUnitId', str, ['optional']),
            ('BMUnitType', str, ['optional']),
            ('LeadPartyName', str, ['optional']),
            ('NGCBMUnitName', str, ['optional'])
        ],
        'CDN': [
            ('FromClearedDate', date, ['optional']),
            ('ToClearedDate', date, ['optional'])
        ],
        'SYSWARN': [
            ('FromDate', date, ['optional']),
            ('ToDate', date, ['optional'])
        ],
        'DISBSAD': [
            ('SettlementDate', date, ['optional']),
            ('SettlementPeriod', str, ['optional'])
        ],
        'NETBSAD': [
            ('SettlementDate', date, ['optional']),
            ('SettlementPeriod', str, ['optional']),
            ('IsTwoDayWindow', bool, ['optional'])
        ],
        'FREQ': [
            ('FromDateTime', datetime, ['optional']),
            ('ToDateTime', datetime, ['optional'])
        ],
        'MID': [
            ('FromSettlementDate', date, ['optional']),
            ('ToSettlementDate', date, ['optional']),
            ('Period', str, ['optional'])
        ],
        'DEVINDOD': [
            ('FromDate', date, ['optional']),
            ('ToDate', date, ['optional'])
        ],
        'NONBM': [
            ('FromDate', date, ['optional']),
            ('ToDate', date, ['optional'])
        ],
        'QAS': [
            ('SettlementDate', date, ['optional']),
            ('SettlementPeriod', str, ['optional']),
            ('BmUnitId', str, ['optional']),
            ('BMUnitType', str, ['optional']),
            ('LeadPartyName', str, ['optional']),
            ('NgcBmUnitName', str, ['optional'])
        ],
        'ROLSYSDEM': [
            ('FromDateTime', datetime, ['optional']),
            ('ToDateTime', datetime, ['optional'])
        ],
        'WINDFORPK': [
            ('FromDate', date, ['optional']),
            ('ToDate', date, ['optional'])
        ],
        'WINDFORFUELHH': [
            ('FromDate', date, ['optional']),
            ('ToDate', date, ['optional'])
        ],
        'FUELINSTHHCUR': [
            ('FuelType', str, ['optional'])
        ],
        'FUELINST': [
            ('FromDateTime', datetime, ['optional']),
            ('ToDateTime', datetime, ['optional'])
        ],
        'FUELHH': [
            ('FromDate', date, ['optional']),
            ('ToDate', date, ['optional'])
        ],
        'INTERFUELHH': [
            ('FromDate', date, ['optional']),
            ('ToDate', date, ['optional'])
        ],
        'NOU2T14D': [],
        'FOU2T14D': [],
        'UOU2T14D': [],
        'NOU2T52W': [],
        'FOU2T52W': [],
        'UOU2T52W': [],
        'NOUY1': [],
        'NOUY2': [],
        'NOUY3': [],
        'NOUY4': [],
        'NOUY5': [],
        'ZOU2T14D': [],
        'ZOU2T52W': [],
        'ZOUY1': [],
        'ZOUY2': [],
        'ZOUY3': [],
        'ZOUY4': [],
        'ZOUY5': [],
        'INDOITSDO': [
            ('FromDate', date, ['optional']),
            ('ToDate', date, ['optional'])
        ],
        'MELIMBALNGC': [
            ('ZoneIdentifier', str, ['optional']),
            ('FromDate', date, ['optional']),
            ('ToDate', date, ['optional'])
        ],
        'FORDAYDEM': [
            ('ZoneIdentifier', str, ['optional']),
            ('FromDate', date, ['optional']),
            ('ToDate', date, ['optional'])
        ],
        'DEMMF2T14D': [],
        'DEMMF2T52W': [],
        'SOSOP': [
            ('SettlementDate', date, ['optional']),
            ('StartTime', time, ['optional']),
            ('TradeType', str, ['optional']),
            ('IsTwoDayWindow', bool, ['optional'])
        ],
        'SOSOT': [],
        'PKDEMYESTTDYTOM': [],
        'INDPKDEMINFO': [],
        'SYSDEM': [
            ('FromDate', date, ['optional']),
            ('ToDate', date, ['optional'])
        ],
        'INDTRIADDEMINFO': [],
        'PHYBMDATA': [
            ('SettlementDate', date, ['optional']),
            ('SettlementPeriod', str, ['optional']),
            ('BMUnitId', str, ['optional']),
            ('BMUnitType', str, ['optional']),
            ('LeadPartyName', str, ['optional']),
            ('NGCBMUnitName', str, ['optional'])
        ],
        'DYNBMDATA': [
            ('SettlementDate', date, ['optional']),
            ('SettlementPeriod', str, ['optional']),
            ('BMUnitId', str, ['optional']),
            ('BMUnitType', str, ['optional']),
            ('LeadPartyName', str, ['optional']),
            ('NGCBMUnitName', str, ['optional'])
        ],
        'DERBMDATA': [
            ('SettlementDate', date, ['optional']),
            ('SettlementPeriod', str, ['optional']),
            ('BMUnitId', str, ['optional']),
            ('BMUnitType', str, ['optional']),
            ('LeadPartyName', str, ['optional']),
            ('NGCBMUnitName', str, ['optional'])
        ],
        'DERSYSDATA': [
            ('FromSettlementDate', date, ['optional']),
            ('ToSettlementDate', date, ['optional']),
            ('SettlementPeriod', str, ['optional'])
        ],
        'DETSYSPRICES': [
            ('SettlementDate', date, ['optional']),
            ('SettlementPeriod', str, ['optional'])
        ],
        'MKTDEPTHDATA': [
            ('SettlementDate', date, ['optional'])
        ],
        'LATESTACCEPTS': [],
        'HISTACCEPTS': [
            ('SettlementDate', date, ['optional']),
            ('SettlementPeriod', str, ['optional'])
        ],
        'SYSMSG': [],
        'BMUNITSEARCH': [
            ('BMUnitId', str, ['optional']),
            ('BMUnitType', str, ['optional']),
            ('LeadPartyName', str, ['optional']),
            ('NGCBMUnitName', str, ['optional'])
        ],
        'SYSWARNTDYTOM': [],
        'HISTSYSWARN': [],
        'LOLPDRM': [
            ('FromSettlementDate', date, ['optional']),
            ('ToSettlementDate', date, ['optional'])
        ],
        'DEMCI': [
            ('FromSettlementDate', date, ['optional']),
            ('ToSettlementDate', date, ['optional'])
        ],
        'STORAW': [
            ('FromSettlementDate', date, ['optional'])
        ],
        'TRADINGUNIT': [
            ('SettlementDate', date, []),
            ('SettlementPeriod', str, []),
            ('TradeType', str, ['optional']),
            ('TradeName', str, ['optional'])
        ],
        'EURGBFXDATA': [
            ('SettlementDayFrom', date, []),
            ('SettlementDayTo', date, ['optional'])
        ]
    },

    # Replacement Reserve Data
    'ReplacementReserveData': {
        'RRBidData': [
            ('SettlementDate', date, []),
            ('SettlementPeriod', str, ['optional']),
            ('BMUnitId', str, ['optional']),
            ('BMUnitType', str, ['optional']),
            ('NGCBMUnitName', str, ['optional']),
            ('ParticipantId', str, ['optional'])
        ],
        'RRAggregatedInfo': [
            ('DateTimeFrom', datetime, []),
            ('DateTimeTo', datetime, ['optional'])
        ],
        'RRActivation': [
            ('SettlementDate', date, []),
            ('SettlementPeriod', str, ['optional']),
            ('BMUnitId', str, ['optional'])
        ],
        'RRINTCON': [
            ('SettlementDate', date, []),
            ('SettlementPeriod', str, ['optional']),
            ('InterconnectorId', str, ['optional'])
        ],
        'RRGBNM': [
            ('SettlementDate', date, []),
            ('SettlementPeriod', str, ['optional'])
        ],
        'RRCashflow': [
            ('SettlementDate', date, []),
            ('SettlementPeriod', str, ['optional']),
            ('BMUnitId', str, ['optional'])
        ]
    }
}

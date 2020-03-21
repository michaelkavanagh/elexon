METHODS = {
    # Transparency Data
    'Transparency': {
        'B1720': [
            ('SettlementDate', str, []),
            ('Period', str, [])
        ],
        'B1730': [
            ('SettlementDate', str, []),
            ('Period', str, [])
        ],
        'B1740': [
            ('SettlementDate', str, []),
            ('Period', str, [])
        ],
        'B1750': [
            ('SettlementDate', str, []),
            ('Period', str, [])
        ],
        'B1760': [
            ('SettlementDate', str, []),
            ('Period', str, [])
        ],
        'B1770': [
            ('SettlementDate', str, []),
            ('Period', str, [])
        ],
        'B1780': [
            ('SettlementDate', str, []),
            ('Period', str, [])
        ],
        'B1790': [
            ('SettlementDate', str, []),
            ('Period', str, [])
        ],
        'B1810': [
            ('SettlementDate', str, []),
            ('Period', str, [])
        ],
        'B1820': [
            ('SettlementDate', str, []),
            ('Period', str, [])
        ],
        'B1830': [
            ('SettlementDate', str, []),
            ('Period', str, [])
        ],
        'B0610': [
            ('SettlementDate', str, []),
            ('Period', str, [])
        ],
        'B0620': [
            ('SettlementDate', str, []),
            ('Period', str, [])
        ],
        'B0630': [
            ('Year', str, []),
            ('Week', str, [])
        ],
        'B0640': [
            ('Year', str, []),
            ('Month', str, [])
        ],
        'B0650': [
            ('Year', str, [])
        ],
        'B0810': [
            ('Year', str, [])
        ],
        'B1410': [
            ('Year', str, [])
        ],
        'B1420': [
            ('Year', str, [])
        ],
        'B1430': [
            ('SettlementDate', str, []),
            ('Period', str, [])
        ],
        'B1440': [
            ('SettlementDate', str, []),
            ('Period', str, [])
        ],
        'B1610': [
            ('SettlementDate', str, []),
            ('NGCBMUnitID', str, []),
            ('Period', str, [])
        ],
        'B1620': [
            ('SettlementDate', str, []),
            ('Period', str, [])
        ],
        'B1630': [
            ('SettlementDate', str, []),
            ('Period', str, [])
        ],
        'B0910': [
            ('Year', str, [])
        ],
        'B1320': [
            ('SettlementDate', str, []),
            ('Period', str, [])
        ],
        'B1330': [
            ('Year', str, []),
            ('Month', str, [])
        ],
        'B0710': [
            ('StartDate', str, []),
            ('StartTime', str, []),
            ('EndDate', str, []),
            ('EndTime', str, [])
        ],
        'B0720': [
            ('StartDate', str, []),
            ('StartTime', str, []),
            ('EndDate', str, []),
            ('EndTime', str, [])
        ],
        'B1010': [
            ('StartDate', str, []),
            ('StartTime', str, []),
            ('EndDate', str, []),
            ('EndTime', str, [])
        ],
        'B1020': [
            ('StartDate', str, []),
            ('StartTime', str, []),
            ('EndDate', str, []),
            ('EndTime', str, [])
        ],
        'B1030': [
            ('StartDate', str, []),
            ('StartTime', str, []),
            ('EndDate', str, []),
            ('EndTime', str, [])
        ],
        'B1510': [
            ('StartDate', str, []),
            ('StartTime', str, []),
            ('EndDate', str, []),
            ('EndTime', str, [])
        ],
        'B1520': [
            ('StartDate', str, []),
            ('StartTime', str, []),
            ('EndDate', str, []),
            ('EndTime', str, [])
        ],
        'B1530': [
            ('StartDate', str, []),
            ('StartTime', str, []),
            ('EndDate', str, []),
            ('EndTime', str, [])
        ],
        'B1540': [
            ('StartDate', str, []),
            ('StartTime', str, []),
            ('EndDate', str, []),
            ('EndTime', str, [])
        ]
    },

    # REMIT
    'REMIT': {
        'MessageListRetrieval': [
            ('EventStart', str, ['optional']),
            ('EventEnd', str, ['optional']),
            ('PublicationFrom', str, ['optional']),
            ('PublicationTo', str, ['optional']),
            ('ParticipantId', str, ['optional']),
            ('MessageID', str, ['optional']),
            ('AssetID', str, ['optional']),
            ('EventType', str, ['optional']),
            ('FuelType', str, ['optional']),
            ('MessageType', str, ['optional']),
            ('UnavailabilityType', str, ['optional'])
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
            ('FromDate', str, ['optional']),
            ('ToDate', str, ['optional'])
        ],
        'BOD': [
            ('SettlementDate', str, ['optional']),
            ('SettlementPeriod', str, ['optional']),
            ('BMUnitId', str, ['optional']),
            ('BMUnitType', str, ['optional']),
            ('LeadPartyName', str, ['optional']),
            ('NGCBMUnitName', str, ['optional'])
        ],
        'CDN': [
            ('FromClearedDate', str, ['optional']),
            ('ToClearedDate', str, ['optional'])
        ],
        'SYSWARN': [
            ('FromDate', str, ['optional']),
            ('ToDate', str, ['optional'])
        ],
        'DISBSAD': [
            ('SettlementDate', str, ['optional']),
            ('SettlementPeriod', str, ['optional'])
        ],
        'NETBSAD': [
            ('SettlementDate', str, ['optional']),
            ('SettlementPeriod', str, ['optional']),
            ('IsTwoDayWindow', str, ['optional'])
        ],
        'FREQ': [
            ('FromDateTime', str, ['optional']),
            ('ToDateTime', str, ['optional'])
        ],
        'MID': [
            ('FromSettlementDate', str, ['optional']),
            ('ToSettlementDate', str, ['optional']),
            ('Period', str, ['optional'])
        ],
        'DEVINDOD': [
            ('FromDateTime', str, ['optional']),
            ('ToDateTime', str, ['optional'])
        ],
        'NONBM': [
            ('FromDateTime', str, ['optional']),
            ('ToDateTime', str, ['optional'])
        ],
        'QAS': [
            ('SettlementDate', str, ['optional']),
            ('SettlementPeriod', str, ['optional']),
            ('BmUnitId', str, ['optional']),
            ('BMUnitType', str, ['optional']),
            ('LeadPartyName', str, ['optional']),
            ('NgcBmUnitName', str, ['optional'])
        ],
        'ROLSYSDEM': [
            ('FromDateTime', str, ['optional']),
            ('ToDateTime', str, ['optional'])
        ],
        'WINDFORPK': [
            ('FromDate', str, ['optional']),
            ('ToDate', str, ['optional'])
        ],
        'WINDFORFUELHH': [
            ('FromDate', str, ['optional']),
            ('ToDate', str, ['optional'])
        ],
        'FUELINSTHHCUR': [
            ('FuelType', str, ['optional'])
        ],
        'FUELINST': [
            ('FromDateTime', str, ['optional']),
            ('ToDateTime', str, ['optional'])
        ],
        'FUELHH': [
            ('FromDate', str, ['optional']),
            ('ToDate', str, ['optional'])
        ],
        'INTERFUELHH': [
            ('FromDate', str, ['optional']),
            ('ToDate', str, ['optional'])
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
            ('FromDate', str, ['optional']),
            ('ToDate', str, ['optional'])
        ],
        'MELIMBALNGC': [
            ('ZoneIdentifier', str, ['optional']),
            ('FromDate', str, ['optional']),
            ('ToDate', str, ['optional'])
        ],
        'FORDAYDEM': [
            ('ZoneIdentifier', str, ['optional']),
            ('FromDate', str, ['optional']),
            ('ToDate', str, ['optional'])
        ],
        'DEMMF2T14D': [],
        'DEMMF2T52W': [],
        'SOSOP': [
            ('SettlementDate', str, ['optional']),
            ('StartTime', str, ['optional']),
            ('TradeType', str, ['optional']),
            ('IsTwoDayWindow', str, ['optional'])
        ],
        'SOSOT': [],
        'PKDEMYESTTDYTOM': [],
        'INDPKDEMINFO': [],
        'SYSDEM': [
            ('FromDate', str, ['optional']),
            ('ToDate', str, ['optional'])
        ],
        'INDTRIADDEMINFO': [],
        'PHYBMDATA': [
            ('SettlementDate', str, ['optional']),
            ('SettlementPeriod', str, ['optional']),
            ('BMUnitId', str, ['optional']),
            ('BMUnitType', str, ['optional']),
            ('LeadPartyName', str, ['optional']),
            ('NGCBMUnitName', str, ['optional'])
        ],
        'DYNBMDATA': [
            ('SettlementDate', str, ['optional']),
            ('SettlementPeriod', str, ['optional']),
            ('BMUnitId', str, ['optional']),
            ('BMUnitType', str, ['optional']),
            ('LeadPartyName', str, ['optional']),
            ('NGCBMUnitName', str, ['optional'])
        ],
        'DERBMDATA': [
            ('SettlementDate', str, ['optional']),
            ('SettlementPeriod', str, ['optional']),
            ('BMUnitId', str, ['optional']),
            ('BMUnitType', str, ['optional']),
            ('LeadPartyName', str, ['optional']),
            ('NGCBMUnitName', str, ['optional'])
        ],
        'DERSYSDATA': [
            ('FromSettlementDate', str, ['optional']),
            ('ToSettlementDate', str, ['optional']),
            ('SettlementPeriod', str, ['optional'])
        ],
        'DETSYSPRICES': [
            ('SettlementDate', str, ['optional']),
            ('SettlementPeriod', str, ['optional'])
        ],
        'MKTDEPTHDATA': [
            ('SettlementDate', str, ['optional'])
        ],
        'LATESTACCEPTS': [],
        'HISTACCEPTS': [
            ('SettlementDate', str, ['optional']),
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
            ('FromSettlementDate', str, ['optional']),
            ('ToSettlementDate', str, ['optional'])
        ],
        'DEMCI': [
            ('FromSettlementDate', str, ['optional']),
            ('ToSettlementDate', str, ['optional'])
        ],
        'STORAW': [
            ('FromSettlementDate', str, ['optional'])
        ],
        'TRADINGUNIT': [
            ('SettlementDate', str, []),
            ('SettlementPeriod', str, []),
            ('TradeType', str, ['optional']),
            ('TradeName', str, ['optional'])
        ],
        'EURGBFXDATA': [
            ('SettlementDayFrom', str, []),
            ('SettlementDayTo', str, ['optional'])
        ]
    },

    # Replacement Reserve Data
    'ReplacementReserveData': {
        'RRBidData': [
            ('SettlementDate', str, []),
            ('SettlementPeriod', str, ['optional']),
            ('BMUnitId', str, ['optional']),
            ('BMUnitType', str, ['optional']),
            ('NGCBMUnitName', str, ['optional']),
            ('ParticipantId', str, ['optional'])
        ],
        'RRAggregatedInfo': [
            ('DateTimeFrom', str, []),
            ('DateTimeTo', str, ['optional'])
        ],
        'RRActivation': [
            ('SettlementDate', str, []),
            ('SettlementPeriod', str, ['optional']),
            ('BMUnitId', str, ['optional'])
        ],
        'RRINTCON': [
            ('SettlementDate', str, []),
            ('SettlementPeriod', str, ['optional']),
            ('InterconnectorId', str, ['optional'])
        ],
        'RRGBNM': [
            ('SettlementDate', str, []),
            ('SettlementPeriod', str, ['optional'])
        ],
        'RRCashflow': [
            ('SettlementDate', str, []),
            ('SettlementPeriod', str, ['optional']),
            ('BMUnitId', str, ['optional'])
        ]
    }
}

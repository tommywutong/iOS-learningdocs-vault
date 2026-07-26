---
title: CWLinkQualityDidChangeNotification
framework: Core WLAN
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.7+（10.10 起废弃）]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/corewlan/cwlinkqualitydidchangenotification
source_url: 'https://developer.apple.com/documentation/corewlan/cwlinkqualitydidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corewlan/cwlinkqualitydidchangenotification.json'
content_hash: 'sha256:e23ab74f17b3ce44'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core WLAN](../corewlan.md)

# CWLinkQualityDidChangeNotification

<sub>Global Variable</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
extern NSString * const CWLinkQualityDidChangeNotification;
```

## Discussion

Posted when the link quality for any WLAN interface changes. The _object_ for this notification is the corresponding BSD interface name. The _userInfo_ dictionary for this notification contains the current RSSI and current transmit rate for the given CoreWLAN interface.

## See Also

### Constants

- [CWBSSIDDidChangeNotification](cwbssiddidchangenotification.md) _(deprecated)_
- [CWCountryCodeDidChangeNotification](cwcountrycodedidchangenotification.md) _(deprecated)_
- [CWErrorDomain](cwerrordomain.md)
- [CWLinkDidChangeNotification](cwlinkdidchangenotification.md) _(deprecated)_
- [CWLinkQualityNotificationRSSIKey](cwlinkqualitynotificationrssikey.md) _(deprecated)_
- [CWLinkQualityNotificationTransmitRateKey](cwlinkqualitynotificationtransmitratekey.md) _(deprecated)_
- [CWModeDidChangeNotification](cwmodedidchangenotification.md) _(deprecated)_
- [CWPowerDidChangeNotification](cwpowerdidchangenotification.md) _(deprecated)_
- [CWScanCacheDidUpdateNotification](cwscancachedidupdatenotification.md) _(deprecated)_
- [CWSSIDDidChangeNotification](cwssiddidchangenotification.md) _(deprecated)_

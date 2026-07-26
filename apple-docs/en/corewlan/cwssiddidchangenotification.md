---
title: CWSSIDDidChangeNotification
framework: Core WLAN
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.6+（10.10 起废弃）]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/corewlan/cwssiddidchangenotification
source_url: 'https://developer.apple.com/documentation/corewlan/cwssiddidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corewlan/cwssiddidchangenotification.json'
content_hash: 'sha256:2432ac4a81c64e24'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core WLAN](../corewlan.md)

# CWSSIDDidChangeNotification

<sub>Global Variable</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
extern NSString * const CWSSIDDidChangeNotification;
```

## Discussion

Posted when the SSID of any WLAN interface changes. The _object_ for this notification is the corresponding BSD interface name. This notification does not contain a _userInfo_ dictionary.

## See Also

### Constants

- [CWBSSIDDidChangeNotification](cwbssiddidchangenotification.md) _(deprecated)_
- [CWCountryCodeDidChangeNotification](cwcountrycodedidchangenotification.md) _(deprecated)_
- [CWErrorDomain](cwerrordomain.md)
- [CWLinkDidChangeNotification](cwlinkdidchangenotification.md) _(deprecated)_
- [CWLinkQualityDidChangeNotification](cwlinkqualitydidchangenotification.md) _(deprecated)_
- [CWLinkQualityNotificationRSSIKey](cwlinkqualitynotificationrssikey.md) _(deprecated)_
- [CWLinkQualityNotificationTransmitRateKey](cwlinkqualitynotificationtransmitratekey.md) _(deprecated)_
- [CWModeDidChangeNotification](cwmodedidchangenotification.md) _(deprecated)_
- [CWPowerDidChangeNotification](cwpowerdidchangenotification.md) _(deprecated)_
- [CWScanCacheDidUpdateNotification](cwscancachedidupdatenotification.md) _(deprecated)_

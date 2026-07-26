---
title: CWLinkDidChangeNotification
framework: Core WLAN
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.6+（10.10 起废弃）]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/corewlan/cwlinkdidchangenotification
source_url: 'https://developer.apple.com/documentation/corewlan/cwlinkdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corewlan/cwlinkdidchangenotification.json'
content_hash: 'sha256:5bc7238d3871f646'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core WLAN](../corewlan.md)

# CWLinkDidChangeNotification

<sub>Global Variable</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
extern NSString * const CWLinkDidChangeNotification;
```

## Discussion

Posted when the link state of any WLAN interface changes. The _object_ for this notification is the corresponding BSD interface name. This notification does not contain a _userInfo_ dictionary.

## See Also

### Constants

- [CWBSSIDDidChangeNotification](cwbssiddidchangenotification.md) _(deprecated)_
- [CWCountryCodeDidChangeNotification](cwcountrycodedidchangenotification.md) _(deprecated)_
- [CWErrorDomain](cwerrordomain.md)
- [CWLinkQualityDidChangeNotification](cwlinkqualitydidchangenotification.md) _(deprecated)_
- [CWLinkQualityNotificationRSSIKey](cwlinkqualitynotificationrssikey.md) _(deprecated)_
- [CWLinkQualityNotificationTransmitRateKey](cwlinkqualitynotificationtransmitratekey.md) _(deprecated)_
- [CWModeDidChangeNotification](cwmodedidchangenotification.md) _(deprecated)_
- [CWPowerDidChangeNotification](cwpowerdidchangenotification.md) _(deprecated)_
- [CWScanCacheDidUpdateNotification](cwscancachedidupdatenotification.md) _(deprecated)_
- [CWSSIDDidChangeNotification](cwssiddidchangenotification.md) _(deprecated)_

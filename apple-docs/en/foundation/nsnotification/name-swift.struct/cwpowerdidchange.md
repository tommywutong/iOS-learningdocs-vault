---
title: CWPowerDidChange
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.6+（10.10 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsnotification/name-swift.struct/cwpowerdidchange
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/cwpowerdidchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/cwpowerdidchange.json'
content_hash: 'sha256:ce66d373ab9689a0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# CWPowerDidChange

<sub>Type Property</sub>

> [!warning] Deprecated
> Use -[CWWiFiClient startMonitoringEventWithType:error:] with the CWEventTypePowerDidChange event type

<sub>macOS</sub>

```swift
static let CWPowerDidChange: NSNotification.Name
```

## Discussion

Posted when the power state of any WLAN interface changes. The _object_ for this notification is the corresponding BSD interface name. This notification does not contain a _userInfo_ dictionary.

## See Also

### Core WLAN

- [CWBSSIDDidChange](cwbssiddidchange.md) _(deprecated)_
- [CWCountryCodeDidChange](cwcountrycodedidchange.md) _(deprecated)_
- [CWLinkDidChange](cwlinkdidchange.md) _(deprecated)_
- [CWLinkQualityDidChange](cwlinkqualitydidchange.md) _(deprecated)_
- [CWModeDidChange](cwmodedidchange.md) _(deprecated)_
- [CWSSIDDidChange](cwssiddidchange.md) _(deprecated)_
- [CWScanCacheDidUpdate](cwscancachedidupdate.md) _(deprecated)_

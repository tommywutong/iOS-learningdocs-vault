---
title: CWScanCacheDidUpdate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.7+（10.10 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsnotification/name-swift.struct/cwscancachedidupdate
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/cwscancachedidupdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/cwscancachedidupdate.json'
content_hash: 'sha256:fc8eec3ea3414588'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# CWScanCacheDidUpdate

<sub>Type Property</sub>

> [!warning] Deprecated
> Use -[CWWiFiClient startMonitoringEventWithType:error:] with the CWEventTypeScanCacheUpdated event type

<sub>macOS</sub>

```swift
static let CWScanCacheDidUpdate: NSNotification.Name
```

## Discussion

Posted when new entries are added to the scan cache, or existing entries are updated with more current information. The _object_ for this notification is the corresponding BSD interface name. This notification does not contain a _userInfo_ dictionary.

## See Also

### Core WLAN

- [CWBSSIDDidChange](cwbssiddidchange.md) _(deprecated)_
- [CWCountryCodeDidChange](cwcountrycodedidchange.md) _(deprecated)_
- [CWLinkDidChange](cwlinkdidchange.md) _(deprecated)_
- [CWLinkQualityDidChange](cwlinkqualitydidchange.md) _(deprecated)_
- [CWModeDidChange](cwmodedidchange.md) _(deprecated)_
- [CWPowerDidChange](cwpowerdidchange.md) _(deprecated)_
- [CWSSIDDidChange](cwssiddidchange.md) _(deprecated)_

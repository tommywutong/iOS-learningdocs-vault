---
title: thermalStateDidChangeNotification
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.10.3+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/processinfo/thermalstatedidchangenotification
source_url: 'https://developer.apple.com/documentation/foundation/processinfo/thermalstatedidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo/thermalstatedidchangenotification.json'
content_hash: 'sha256:974a0e8b554e25d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProcessInfo](../processinfo.md)

# thermalStateDidChangeNotification

<sub>Type Property</sub>

Posts when the thermal state of the system changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class let thermalStateDidChangeNotification: NSNotification.Name
```

## Discussion

The notification object is a [ProcessInfo](../processinfo.md) instance.

To receive [NSProcessInfoThermalStateDidChangeNotification](thermalstatedidchangenotification.md), you must access the [thermalState](thermalstate-swift.property.md) prior to registering for the notification.

## See Also

### Working with notifications

- [NSProcessInfoPowerStateDidChangeNotification](../nsnotification/name-swift.struct/nsprocessinfopowerstatedidchange.md) — Posts when the power state of a device changes.

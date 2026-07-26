---
title: HKUserPreferencesDidChange
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.2+, iPadOS 8.2+, Mac Catalyst 8.2+, macOS 13.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/hkuserpreferencesdidchange
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/hkuserpreferencesdidchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/hkuserpreferencesdidchange.json'
content_hash: 'sha256:d2b4e5d9e5d2c653'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# HKUserPreferencesDidChange

<sub>Type Property</sub>

Notifies observers whenever the user changes his or her preferred units.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
static let HKUserPreferencesDidChange: NSNotification.Name
```

## Discussion

The preferred units are the units that the user prefers for a given measurement type. By default, the preferred units are based on the device’s current locale. For example, in the US, the preferred units for the [bodyMass](../../../healthkit/hkquantitytypeidentifier/bodymass.md) identifier are pounds. Other regions may use kilograms or stones. However, users can change their preferred units in the Health app at any time.

Each `HKHealthStore` object posts its own `HKUserPreferencesDidChangeNotification` notification. To avoid receiving duplicate notifications, always pass a health store instance to the notification center when adding observers.

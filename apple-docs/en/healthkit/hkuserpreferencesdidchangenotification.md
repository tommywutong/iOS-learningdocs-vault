---
title: HKUserPreferencesDidChangeNotification
framework: HealthKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 8.2+, iPadOS 8.2+, Mac Catalyst 13.0+, macOS 13.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/healthkit/hkuserpreferencesdidchangenotification
source_url: 'https://developer.apple.com/documentation/healthkit/hkuserpreferencesdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/healthkit/hkuserpreferencesdidchangenotification.json'
content_hash: 'sha256:a7563b14ad6962c8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [HealthKit](../healthkit.md)

# HKUserPreferencesDidChangeNotification

<sub>Global Variable</sub>

Notifies observers whenever the user changes his or her preferred units.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```objc
extern NSString * const HKUserPreferencesDidChangeNotification;
```

## Discussion

The preferred units are the units that the user prefers for a given measurement type. By default, the preferred units are based on the device’s current locale. For example, in the US, the preferred units for the [HKQuantityTypeIdentifierBodyMass](hkquantitytypeidentifier/bodymass.md) identifier are pounds. Other regions may use kilograms or stones. However, users can change their preferred units in the Health app at any time.

Each `HKHealthStore` object posts its own `HKUserPreferencesDidChangeNotification` notification. To avoid receiving duplicate notifications, always pass a health store instance to the notification center when adding observers.

## See Also

### Accessing the preferred units

- [- preferredUnitsForQuantityTypes:completion:](<hkhealthstore/preferredunits(for_completion_).md>) — Returns the user’s preferred units for the given quantity types.

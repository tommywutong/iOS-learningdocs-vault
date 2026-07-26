---
title: kCLLocationAccuracyBestForNavigation
framework: Core Location
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/kcllocationaccuracybestfornavigation
source_url: 'https://developer.apple.com/documentation/corelocation/kcllocationaccuracybestfornavigation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/kcllocationaccuracybestfornavigation.json'
content_hash: 'sha256:afe040257353f588'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# kCLLocationAccuracyBestForNavigation

<sub>Global Variable</sub>

The highest possible accuracy that uses additional sensor data to facilitate navigation apps.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCLLocationAccuracyBestForNavigation: CLLocationAccuracy
```

## Discussion

This level of accuracy is intended for use in navigation apps that require precise position information at all times. Because of the extra power requirements, use this level of accuracy only while the device is plugged in.

This level of accurate is available only if `isAuthorizedForPreciseLocation` is [true](../swift/true.md).

## See Also

### Desired Accuracy Constants

- [kCLLocationAccuracyBest](kcllocationaccuracybest.md) — The best level of accuracy available.
- [kCLLocationAccuracyNearestTenMeters](kcllocationaccuracynearesttenmeters.md) — Accurate to within ten meters of the desired target.
- [kCLLocationAccuracyHundredMeters](kcllocationaccuracyhundredmeters.md) — Accurate to within one hundred meters.
- [kCLLocationAccuracyKilometer](kcllocationaccuracykilometer.md) — Accurate to the nearest kilometer.
- [kCLLocationAccuracyThreeKilometers](kcllocationaccuracythreekilometers.md) — Accurate to the nearest three kilometers.
- [kCLLocationAccuracyReduced](kcllocationaccuracyreduced.md) — The level of accuracy used when an app isn’t authorized for full accuracy location data.

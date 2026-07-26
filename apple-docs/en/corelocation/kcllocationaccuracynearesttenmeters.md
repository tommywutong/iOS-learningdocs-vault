---
title: kCLLocationAccuracyNearestTenMeters
framework: Core Location
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/kcllocationaccuracynearesttenmeters
source_url: 'https://developer.apple.com/documentation/corelocation/kcllocationaccuracynearesttenmeters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/kcllocationaccuracynearesttenmeters.json'
content_hash: 'sha256:25f52e4a587eab4d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# kCLLocationAccuracyNearestTenMeters

<sub>Global Variable</sub>

Accurate to within ten meters of the desired target.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCLLocationAccuracyNearestTenMeters: CLLocationAccuracy
```

## Discussion

This level of accurate is available only if `isAuthorizedForPreciseLocation` is [true](../swift/true.md).

## See Also

### Desired Accuracy Constants

- [kCLLocationAccuracyBestForNavigation](kcllocationaccuracybestfornavigation.md) — The highest possible accuracy that uses additional sensor data to facilitate navigation apps.
- [kCLLocationAccuracyBest](kcllocationaccuracybest.md) — The best level of accuracy available.
- [kCLLocationAccuracyHundredMeters](kcllocationaccuracyhundredmeters.md) — Accurate to within one hundred meters.
- [kCLLocationAccuracyKilometer](kcllocationaccuracykilometer.md) — Accurate to the nearest kilometer.
- [kCLLocationAccuracyThreeKilometers](kcllocationaccuracythreekilometers.md) — Accurate to the nearest three kilometers.
- [kCLLocationAccuracyReduced](kcllocationaccuracyreduced.md) — The level of accuracy used when an app isn’t authorized for full accuracy location data.

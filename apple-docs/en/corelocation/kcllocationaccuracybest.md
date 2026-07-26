---
title: kCLLocationAccuracyBest
framework: Core Location
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/kcllocationaccuracybest
source_url: 'https://developer.apple.com/documentation/corelocation/kcllocationaccuracybest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/kcllocationaccuracybest.json'
content_hash: 'sha256:43044c67242ba77a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# kCLLocationAccuracyBest

<sub>Global Variable</sub>

The best level of accuracy available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCLLocationAccuracyBest: CLLocationAccuracy
```

## Discussion

Specify this constant when you want very high accuracy but don’t need the same level of accuracy required for navigation apps.

This level of accurate is available only if `isAuthorizedForPreciseLocation` is [true](../swift/true.md).

## See Also

### Desired Accuracy Constants

- [kCLLocationAccuracyBestForNavigation](kcllocationaccuracybestfornavigation.md) — The highest possible accuracy that uses additional sensor data to facilitate navigation apps.
- [kCLLocationAccuracyNearestTenMeters](kcllocationaccuracynearesttenmeters.md) — Accurate to within ten meters of the desired target.
- [kCLLocationAccuracyHundredMeters](kcllocationaccuracyhundredmeters.md) — Accurate to within one hundred meters.
- [kCLLocationAccuracyKilometer](kcllocationaccuracykilometer.md) — Accurate to the nearest kilometer.
- [kCLLocationAccuracyThreeKilometers](kcllocationaccuracythreekilometers.md) — Accurate to the nearest three kilometers.
- [kCLLocationAccuracyReduced](kcllocationaccuracyreduced.md) — The level of accuracy used when an app isn’t authorized for full accuracy location data.

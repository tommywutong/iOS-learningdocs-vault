---
title: CLLocationDistanceMax
framework: Core Location
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationdistancemax
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationdistancemax'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationdistancemax.json'
content_hash: 'sha256:fa3af79a1e3b0e76'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLLocationDistanceMax

<sub>Global Variable</sub>

A constant indicating the maximum distance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let CLLocationDistanceMax: CLLocationDistance
```

## Discussion

When scheduling deferred updates, you can use this constant to indicate that a new update should be triggered only after the device moves a significantly large distance.

## See Also

### Specifying distance and accuracy

- [distanceFilter](cllocationmanager/distancefilter.md) — The minimum distance in meters the device must move horizontally before an update event is generated.
- [kCLDistanceFilterNone](kcldistancefilternone.md) — A constant indicating that all movement should be reported.
- [CLLocationDistance](cllocationdistance.md) — A distance in meters from an existing location.
- [desiredAccuracy](cllocationmanager/desiredaccuracy.md) — The accuracy of the location data that your app wants to receive.
- [CLLocationAccuracy](cllocationaccuracy.md) — The accuracy of a geographical coordinate.

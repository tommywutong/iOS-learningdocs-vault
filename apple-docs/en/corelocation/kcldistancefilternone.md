---
title: kCLDistanceFilterNone
framework: Core Location
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/kcldistancefilternone
source_url: 'https://developer.apple.com/documentation/corelocation/kcldistancefilternone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/kcldistancefilternone.json'
content_hash: 'sha256:c890fa51cf0ed607'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# kCLDistanceFilterNone

<sub>Global Variable</sub>

A constant indicating that all movement should be reported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCLDistanceFilterNone: CLLocationDistance
```

## Discussion

Use this constant to specify that any change in location should trigger a new location update.

## See Also

### Specifying distance and accuracy

- [distanceFilter](cllocationmanager/distancefilter.md) — The minimum distance in meters the device must move horizontally before an update event is generated.
- [CLLocationDistanceMax](cllocationdistancemax.md) — A constant indicating the maximum distance.
- [CLLocationDistance](cllocationdistance.md) — A distance in meters from an existing location.
- [desiredAccuracy](cllocationmanager/desiredaccuracy.md) — The accuracy of the location data that your app wants to receive.
- [CLLocationAccuracy](cllocationaccuracy.md) — The accuracy of a geographical coordinate.

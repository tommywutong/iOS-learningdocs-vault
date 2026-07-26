---
title: advisoryNotices
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkroute/advisorynotices
source_url: 'https://developer.apple.com/documentation/mapkit/mkroute/advisorynotices'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkroute/advisorynotices.json'
content_hash: 'sha256:c362e9019889edae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKRoute](../mkroute.md)

# advisoryNotices

<sub>Instance Property</sub>

An array of advisory notice strings for the route.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var advisoryNotices: [String] { get }
```

## Discussion

This property contains an array of [NSString](../../foundation/nsstring.md) objects. The framework localizes each string according to the user’s language preferences. The strings contain additional information that’s important for the user to know about the route. For example, a string might note the closing of a portion of the route during the winter or after big storms.

## See Also

### Getting additional route details

- [name](name.md) — The assigned name for the route.
- [hasHighways](hashighways.md) — A Boolean value that indicates whether the route contains highways.
- [hasTolls](hastolls.md) — A Boolean value that indicates whether the route has tolls.
- [distance](distance.md) — The route distance, in meters.
- [expectedTravelTime](expectedtraveltime.md) — The expected travel time, in seconds.
- [transportType](transporttype.md) — The overall route transport type.

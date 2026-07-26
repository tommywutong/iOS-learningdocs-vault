---
title: name
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkroute/name
source_url: 'https://developer.apple.com/documentation/mapkit/mkroute/name'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkroute/name.json'
content_hash: 'sha256:784a073d3af9ba15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKRoute](../mkroute.md)

# name

<sub>Instance Property</sub>

The assigned name for the route.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var name: String { get }
```

## Discussion

The framework localizes the string in this property according to the user’s language preferences. You can display this string to the user from your app’s user interface so that the user can distinguish one route from another.

The string itself describes the route using one of the route’s significant features. For example, a route that uses a major highway for a significant portion of the route might use that highway for its name.

## See Also

### Getting additional route details

- [hasHighways](hashighways.md) — A Boolean value that indicates whether the route contains highways.
- [hasTolls](hastolls.md) — A Boolean value that indicates whether the route has tolls.
- [advisoryNotices](advisorynotices.md) — An array of advisory notice strings for the route.
- [distance](distance.md) — The route distance, in meters.
- [expectedTravelTime](expectedtraveltime.md) — The expected travel time, in seconds.
- [transportType](transporttype.md) — The overall route transport type.

---
title: distance
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkroute/distance
source_url: 'https://developer.apple.com/documentation/mapkit/mkroute/distance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkroute/distance.json'
content_hash: 'sha256:0e2b50ad2f6665f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKRoute](../mkroute.md)

# distance

<sub>Instance Property</sub>

The route distance, in meters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var distance: CLLocationDistance { get }
```

## Discussion

This property reflects the distance that the user covers while traversing the path of the route. It’s not a linear distance between the start and end points of the route.

## See Also

### Getting additional route details

- [name](name.md) — The assigned name for the route.
- [hasHighways](hashighways.md) — A Boolean value that indicates whether the route contains highways.
- [hasTolls](hastolls.md) — A Boolean value that indicates whether the route has tolls.
- [advisoryNotices](advisorynotices.md) — An array of advisory notice strings for the route.
- [expectedTravelTime](expectedtraveltime.md) — The expected travel time, in seconds.
- [transportType](transporttype.md) — The overall route transport type.

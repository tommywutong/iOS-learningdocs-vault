---
title: expectedTravelTime
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkroute/expectedtraveltime
source_url: 'https://developer.apple.com/documentation/mapkit/mkroute/expectedtraveltime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkroute/expectedtraveltime.json'
content_hash: 'sha256:fcf94ea27af76356'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKRoute](../mkroute.md)

# expectedTravelTime

<sub>Instance Property</sub>

The expected travel time, in seconds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var expectedTravelTime: TimeInterval { get }
```

## Discussion

This expected travel time reflects the time it takes to traverse the route under ideal conditions. The actual amount of time may vary based on conditions.

## See Also

### Getting additional route details

- [name](name.md) — The assigned name for the route.
- [hasHighways](hashighways.md) — A Boolean value that indicates whether the route contains highways.
- [hasTolls](hastolls.md) — A Boolean value that indicates whether the route has tolls.
- [advisoryNotices](advisorynotices.md) — An array of advisory notice strings for the route.
- [distance](distance.md) — The route distance, in meters.
- [transportType](transporttype.md) — The overall route transport type.

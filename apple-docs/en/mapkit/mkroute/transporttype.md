---
title: transportType
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkroute/transporttype
source_url: 'https://developer.apple.com/documentation/mapkit/mkroute/transporttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkroute/transporttype.json'
content_hash: 'sha256:e4c6afb492de4db8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKRoute](../mkroute.md)

# transportType

<sub>Instance Property</sub>

The overall route transport type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var transportType: MKDirectionsTransportType { get }
```

## Discussion

This property reflects the primary transport type used for the route. Individual steps of the route might use different transport types.

## See Also

### Getting additional route details

- [name](name.md) — The assigned name for the route.
- [hasHighways](hashighways.md) — A Boolean value that indicates whether the route contains highways.
- [hasTolls](hastolls.md) — A Boolean value that indicates whether the route has tolls.
- [advisoryNotices](advisorynotices.md) — An array of advisory notice strings for the route.
- [distance](distance.md) — The route distance, in meters.
- [expectedTravelTime](expectedtraveltime.md) — The expected travel time, in seconds.

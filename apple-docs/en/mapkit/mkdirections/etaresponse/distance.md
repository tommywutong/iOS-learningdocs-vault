---
title: distance
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkdirections/etaresponse/distance
source_url: 'https://developer.apple.com/documentation/mapkit/mkdirections/etaresponse/distance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkdirections/etaresponse/distance.json'
content_hash: 'sha256:7d4f64535dfd7aa1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKDirections](../../mkdirections.md) · [ETAResponse](../etaresponse.md)

# distance

<sub>Instance Property</sub>

The expected travel distance, in meters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var distance: CLLocationDistance { get }
```

## Discussion

This property contains the overall distance traversed by the route.

## See Also

### Getting the travel information

- [expectedTravelTime](expectedtraveltime.md) — The expected travel time, in seconds.
- [expectedDepartureDate](expecteddeparturedate.md) — The expected departure time.
- [expectedArrivalDate](expectedarrivaldate.md) — The expected arrival time.
- [transportType](transporttype.md) — The type of conveyance to use for determining the travel time.

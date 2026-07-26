---
title: expectedTravelTime
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkdirections/etaresponse/expectedtraveltime
source_url: 'https://developer.apple.com/documentation/mapkit/mkdirections/etaresponse/expectedtraveltime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkdirections/etaresponse/expectedtraveltime.json'
content_hash: 'sha256:1a63e202b345ea3c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKDirections](../../mkdirections.md) · [ETAResponse](../etaresponse.md)

# expectedTravelTime

<sub>Instance Property</sub>

The expected travel time, in seconds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var expectedTravelTime: TimeInterval { get }
```

## Discussion

The expected travel time reflects the time it takes to traverse the route, taking expected traffic into account. The actual amount of time may vary based on changes in traffic and other travel conditions.

## See Also

### Getting the travel information

- [expectedDepartureDate](expecteddeparturedate.md) — The expected departure time.
- [expectedArrivalDate](expectedarrivaldate.md) — The expected arrival time.
- [distance](distance.md) — The expected travel distance, in meters.
- [transportType](transporttype.md) — The type of conveyance to use for determining the travel time.

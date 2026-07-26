---
title: transportType
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkdirections/etaresponse/transporttype
source_url: 'https://developer.apple.com/documentation/mapkit/mkdirections/etaresponse/transporttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkdirections/etaresponse/transporttype.json'
content_hash: 'sha256:ba99513b36cad537'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKDirections](../../mkdirections.md) · [ETAResponse](../etaresponse.md)

# transportType

<sub>Instance Property</sub>

The type of conveyance to use for determining the travel time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var transportType: MKDirectionsTransportType { get }
```

## Discussion

You specify the desired transportation type in your [Request](../request.md) object. If you specified [MKDirectionsTransportTypeAny](../../mkdirectionstransporttype/any.md), this property contains the transportation type used to generate the estimated information.

## See Also

### Getting the travel information

- [expectedTravelTime](expectedtraveltime.md) — The expected travel time, in seconds.
- [expectedDepartureDate](expecteddeparturedate.md) — The expected departure time.
- [expectedArrivalDate](expectedarrivaldate.md) — The expected arrival time.
- [distance](distance.md) — The expected travel distance, in meters.

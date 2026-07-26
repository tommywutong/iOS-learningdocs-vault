---
title: expectedDepartureDate
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkdirections/etaresponse/expecteddeparturedate
source_url: 'https://developer.apple.com/documentation/mapkit/mkdirections/etaresponse/expecteddeparturedate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkdirections/etaresponse/expecteddeparturedate.json'
content_hash: 'sha256:0e255243760b5696'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKDirections](../../mkdirections.md) · [ETAResponse](../etaresponse.md)

# expectedDepartureDate

<sub>Instance Property</sub>

The expected departure time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var expectedDepartureDate: Date { get }
```

## Discussion

The value of this property is dependent on whether you specify a departure date or arrival date in your [Request](../request.md) object. If you specify a departure date, the framework copies that date to this property. If you specify an arrival date, but not a departure date, the framework computes the departure date by subtracting the expected travel time from your arrival date. If you don’t specify an arrival date or departure date, the framework sets this property to the current time.

## See Also

### Getting the travel information

- [expectedTravelTime](expectedtraveltime.md) — The expected travel time, in seconds.
- [expectedArrivalDate](expectedarrivaldate.md) — The expected arrival time.
- [distance](distance.md) — The expected travel distance, in meters.
- [transportType](transporttype.md) — The type of conveyance to use for determining the travel time.

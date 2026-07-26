---
title: transportType
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkdirections/request/transporttype
source_url: 'https://developer.apple.com/documentation/mapkit/mkdirections/request/transporttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkdirections/request/transporttype.json'
content_hash: 'sha256:2aacdf0db56db1a3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKDirections](../../mkdirections.md) · [Request](../request.md)

# transportType

<sub>Instance Property</sub>

The type of conveyance that the directions apply to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var transportType: MKDirectionsTransportType { get set }
```

## Discussion

You can use this property to specify whether you want directions suited to a particular type of transportation. For example, you can use this to specify that you want walking directions or driving directions.

The default value of this property is [MKDirectionsTransportTypeAny](../../mkdirectionstransporttype/any.md).

## See Also

### Specifying transportation options

- [highwayPreference](highwaypreference.md) — The value that indicates whether the framework uses or avoids highways when providing directions.
- [tollPreference](tollpreference.md) — The value that indicates whether the framework avoids routes that have tolls when providing directions.
- [RoutePreference](../routepreference.md) — Options that modify how the framework selects routes when calculating directions.
- [requestsAlternateRoutes](requestsalternateroutes.md) — A Boolean value that indicates whether your app requests multiple routes when they’re available.
- [departureDate](departuredate.md) — The departure date for the trip.
- [arrivalDate](arrivaldate.md) — The arrival date for the trip.

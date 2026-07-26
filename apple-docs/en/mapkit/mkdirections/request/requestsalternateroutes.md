---
title: requestsAlternateRoutes
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkdirections/request/requestsalternateroutes
source_url: 'https://developer.apple.com/documentation/mapkit/mkdirections/request/requestsalternateroutes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkdirections/request/requestsalternateroutes.json'
content_hash: 'sha256:052d7e579b0eee7b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKDirections](../../mkdirections.md) · [Request](../request.md)

# requestsAlternateRoutes

<sub>Instance Property</sub>

A Boolean value that indicates whether your app requests multiple routes when they’re available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var requestsAlternateRoutes: Bool { get set }
```

## Discussion

When this property is [false](../../../swift/false.md), the server returns a single route between the start and end points. When this property is [true](../../../swift/true.md), the server may return additional routes for the user to follow. The server returns additional routes only if they’re available and represent a reasonable path that the user might take.

The default value of this property is [false](../../../swift/false.md).

## See Also

### Specifying transportation options

- [transportType](transporttype.md) — The type of conveyance that the directions apply to.
- [highwayPreference](highwaypreference.md) — The value that indicates whether the framework uses or avoids highways when providing directions.
- [tollPreference](tollpreference.md) — The value that indicates whether the framework avoids routes that have tolls when providing directions.
- [RoutePreference](../routepreference.md) — Options that modify how the framework selects routes when calculating directions.
- [departureDate](departuredate.md) — The departure date for the trip.
- [arrivalDate](arrivaldate.md) — The arrival date for the trip.

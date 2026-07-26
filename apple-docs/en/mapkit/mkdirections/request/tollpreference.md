---
title: tollPreference
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkdirections/request/tollpreference
source_url: 'https://developer.apple.com/documentation/mapkit/mkdirections/request/tollpreference'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkdirections/request/tollpreference.json'
content_hash: 'sha256:6a0dc8720eb43215'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKDirections](../../mkdirections.md) · [Request](../request.md)

# tollPreference

<sub>Instance Property</sub>

The value that indicates whether the framework avoids routes that have tolls when providing directions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var tollPreference: MKDirections.RoutePreference { get set }
```

## See Also

### Specifying transportation options

- [transportType](transporttype.md) — The type of conveyance that the directions apply to.
- [highwayPreference](highwaypreference.md) — The value that indicates whether the framework uses or avoids highways when providing directions.
- [RoutePreference](../routepreference.md) — Options that modify how the framework selects routes when calculating directions.
- [requestsAlternateRoutes](requestsalternateroutes.md) — A Boolean value that indicates whether your app requests multiple routes when they’re available.
- [departureDate](departuredate.md) — The departure date for the trip.
- [arrivalDate](arrivaldate.md) — The arrival date for the trip.

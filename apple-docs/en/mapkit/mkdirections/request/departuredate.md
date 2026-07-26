---
title: departureDate
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkdirections/request/departuredate
source_url: 'https://developer.apple.com/documentation/mapkit/mkdirections/request/departuredate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkdirections/request/departuredate.json'
content_hash: 'sha256:5ee863d73e13c464'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKDirections](../../mkdirections.md) · [Request](../request.md)

# departureDate

<sub>Instance Property</sub>

The departure date for the trip.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var departureDate: Date? { get set }
```

## Discussion

Specifying a departure date provides the server with extra information that it can use to optimize the returned routes. For example, for a trip that takes place during commute hours, the server might consider alternatives to routes that are typically congested at that time.

The use of this property is optional.

## See Also

### Specifying transportation options

- [transportType](transporttype.md) — The type of conveyance that the directions apply to.
- [highwayPreference](highwaypreference.md) — The value that indicates whether the framework uses or avoids highways when providing directions.
- [tollPreference](tollpreference.md) — The value that indicates whether the framework avoids routes that have tolls when providing directions.
- [RoutePreference](../routepreference.md) — Options that modify how the framework selects routes when calculating directions.
- [requestsAlternateRoutes](requestsalternateroutes.md) — A Boolean value that indicates whether your app requests multiple routes when they’re available.
- [arrivalDate](arrivaldate.md) — The arrival date for the trip.

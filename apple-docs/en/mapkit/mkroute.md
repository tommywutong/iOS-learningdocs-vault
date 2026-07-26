---
title: MKRoute
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkroute
source_url: 'https://developer.apple.com/documentation/mapkit/mkroute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkroute.json'
content_hash: 'sha256:117bedaef1976f49'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKRoute

<sub>Class</sub>

A single route between a requested start and end point.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class MKRoute
```

## Overview

An `MKRoute` object defines the geometry for the route — that is, it contains line segments associated with specific map coordinates. A route object may also include other information, such as the name of the route, its distance, and the expected travel time.

You don’t create instances of this class directly. When you use an [MKDirections](mkdirections.md) object to request directions from Apple, the returned [Response](mkdirections/response.md) object contains the possible routes.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting the route geometry

- [polyline](mkroute/polyline.md) — The detailed route geometry.
- [steps](mkroute/steps.md) — The array of steps that create the overall route.
- [Step](mkroute/step.md) — One portion of an overall route.

### Getting additional route details

- [name](mkroute/name.md) — The assigned name for the route.
- [hasHighways](mkroute/hashighways.md) — A Boolean value that indicates whether the route contains highways.
- [hasTolls](mkroute/hastolls.md) — A Boolean value that indicates whether the route has tolls.
- [advisoryNotices](mkroute/advisorynotices.md) — An array of advisory notice strings for the route.
- [distance](mkroute/distance.md) — The route distance, in meters.
- [expectedTravelTime](mkroute/expectedtraveltime.md) — The expected travel time, in seconds.
- [transportType](mkroute/transporttype.md) — The overall route transport type.

## See Also

### Directions

- [MKDirections](mkdirections.md) — A utility object that computes directions and travel-time information based on the route information you provide.
- [Request](mkdirections/request.md) — The start and end points of a route, along with the planned mode of transportation.
- [Response](mkdirections/response.md) — The route information that Apple servers return in response to your request for directions.
- [ETAResponse](mkdirections/etaresponse.md) — The travel-time information that Apple servers return.
- [Step](mkroute/step.md) — One portion of an overall route.

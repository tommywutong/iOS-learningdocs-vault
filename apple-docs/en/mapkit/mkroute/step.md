---
title: MKRoute.Step
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkroute/step
source_url: 'https://developer.apple.com/documentation/mapkit/mkroute/step'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkroute/step.json'
content_hash: 'sha256:fb8310d42b620778'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKRoute](../mkroute.md)

# MKRoute.Step

<sub>Class</sub>

One portion of an overall route.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class Step
```

## Overview

Each `MKRoute.Step` object corresponds to a single instruction that the person needs to follow when navigating between two points. For example, a step might involve following a single road until continuing along the route requires a turn.

You don’t create instances of this class directly. An [MKRoute](../mkroute.md) object contains the `MKRoute.Step` objects associated with a route. For more information about requesting directions, see [MKDirections](../mkdirections.md).

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md)

## Topics

### Getting the step geometry

- [polyline](step/polyline.md) — The detailed step geometry.

### Getting additional step details

- [instructions](step/instructions.md) — The written instructions for following the path that the step represents.
- [notice](step/notice.md) — Additional notices that apply to the step.
- [distance](step/distance.md) — The step distance, in meters.
- [transportType](step/transporttype.md) — The transport type of the step.

## See Also

### Directions

- [MKDirections](../mkdirections.md) — A utility object that computes directions and travel-time information based on the route information you provide.
- [Request](../mkdirections/request.md) — The start and end points of a route, along with the planned mode of transportation.
- [Response](../mkdirections/response.md) — The route information that Apple servers return in response to your request for directions.
- [ETAResponse](../mkdirections/etaresponse.md) — The travel-time information that Apple servers return.
- [MKRoute](../mkroute.md) — A single route between a requested start and end point.

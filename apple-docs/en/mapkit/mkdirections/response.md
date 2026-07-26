---
title: MKDirections.Response
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkdirections/response
source_url: 'https://developer.apple.com/documentation/mapkit/mkdirections/response'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkdirections/response.json'
content_hash: 'sha256:d1a68953318418ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKDirections](../mkdirections.md)

# MKDirections.Response

<sub>Class</sub>

The route information that Apple servers return in response to your request for directions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class Response
```

## Overview

You don’t create instances of this class directly. Instead, you initiate a request for directions by calling the [- calculateDirectionsWithCompletionHandler:](<calculate(completionhandler_).md>) method of an [MKDirections](../mkdirections.md) object. The completion handler you pass to that method receives an `MKDirections.Response` object with the results.

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md)

## Topics

### Getting the end points

- [source](response/source.md) — The start point of the route.
- [destination](response/destination.md) — The end point of the route.

### Getting the route information

- [routes](response/routes.md) — An array of route objects representing the directions between the start and end points.

## See Also

### Directions

- [MKDirections](../mkdirections.md) — A utility object that computes directions and travel-time information based on the route information you provide.
- [Request](request.md) — The start and end points of a route, along with the planned mode of transportation.
- [ETAResponse](etaresponse.md) — The travel-time information that Apple servers return.
- [MKRoute](../mkroute.md) — A single route between a requested start and end point.
- [Step](../mkroute/step.md) — One portion of an overall route.

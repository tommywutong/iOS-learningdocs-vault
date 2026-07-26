---
title: MKDirections
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkdirections
source_url: 'https://developer.apple.com/documentation/mapkit/mkdirections'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkdirections.json'
content_hash: 'sha256:26274e4defd51545'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKDirections

<sub>Class</sub>

A utility object that computes directions and travel-time information based on the route information you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class MKDirections
```

## Overview

You use an `MKDirections` object to ask the Apple servers to provide walking or driving directions for a route, which you specify using an [Request](mkdirections/request.md) object. After making a request, MapKit delivers the results asynchronously to the completion handler that you provide. You can also get the estimated travel time for the route.

Each `MKDirections` object handles a single request for directions, although you can cancel and restart that request as needed. You can create multiple instances of this class and process different route requests at the same time, but make requests only when you plan to present the corresponding route information to the user. Apps may receive an [MKErrorLoadingThrottled](mkerror/code/loadingthrottled.md) error if the device makes too many requests in too short a time period.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a directions object

- [- initWithRequest:](<mkdirections/init(request_).md>) — Creates and returns a directions object using the specified request.
- [Request](mkdirections/request.md) — The start and end points of a route, along with the planned mode of transportation.
- [RoutePreference](mkdirections/routepreference.md) — Options that modify how the framework selects routes when calculating directions.

### Getting the directions

- [- calculateDirectionsWithCompletionHandler:](<mkdirections/calculate(completionhandler_).md>) — Begins calculating the requested route information asynchronously.
- [DirectionsHandler](mkdirections/directionshandler.md) — The block to use for processing the requested route information.
- [Response](mkdirections/response.md) — The route information that Apple servers return in response to your request for directions.

### Getting the ETA

- [- calculateETAWithCompletionHandler:](<mkdirections/calculateeta(completionhandler_).md>) — Begins calculating the requested travel-time information asynchronously.
- [ETAHandler](mkdirections/etahandler.md) — The block to use for processing travel-time information.
- [ETAResponse](mkdirections/etaresponse.md) — The travel-time information that Apple servers return.

### Managing the request

- [- cancel](<mkdirections/cancel().md>) — Cancels a pending request.
- [calculating](mkdirections/iscalculating.md) — A Boolean value that indicates whether a request is in process.

## See Also

### Directions

- [Request](mkdirections/request.md) — The start and end points of a route, along with the planned mode of transportation.
- [Response](mkdirections/response.md) — The route information that Apple servers return in response to your request for directions.
- [ETAResponse](mkdirections/etaresponse.md) — The travel-time information that Apple servers return.
- [MKRoute](mkroute.md) — A single route between a requested start and end point.
- [Step](mkroute/step.md) — One portion of an overall route.

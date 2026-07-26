---
title: 'init(request:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkdirections/init(request:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkdirections/init(request:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkdirections/init%28request%3A%29.json'
content_hash: 'sha256:9e1e9f6a93b2b6f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKDirections](../mkdirections.md)

# init(request:)

<sub>Initializer</sub>

Creates and returns a directions object using the specified request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(request: MKDirections.Request)
```

## Parameters

- `request` — The request object containing the start and end points of the route. This parameter must not be `nil`.

## Return Value

An initialized directions object.

## Discussion

After initializing your directions object, you must call the [- calculateDirectionsWithCompletionHandler:](<calculate(completionhandler_).md>) or [- calculateETAWithCompletionHandler:](<calculateeta(completionhandler_).md>) method to perform the request.

## See Also

### Related Documentation

- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)

### Creating a directions object

- [Request](request.md) — The start and end points of a route, along with the planned mode of transportation.
- [RoutePreference](routepreference.md) — Options that modify how the framework selects routes when calculating directions.

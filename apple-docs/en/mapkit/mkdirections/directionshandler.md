---
title: MKDirections.DirectionsHandler
framework: MapKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkdirections/directionshandler
source_url: 'https://developer.apple.com/documentation/mapkit/mkdirections/directionshandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkdirections/directionshandler.json'
content_hash: 'sha256:3b77cdf2e67c6986'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKDirections](../mkdirections.md)

# MKDirections.DirectionsHandler

<sub>Type Alias</sub>

The block to use for processing the requested route information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias DirectionsHandler = (MKDirections.Response?, (any Error)?) -> Void
```

## Parameters

- `response` — The `response` parameter contains the route information for the request. If an error occurs or the framework can’t determine a route, this parameter is `nil`.

- `error` — The `error` parameter contains information about any errors that occur. If no errors occur, this parameter is `nil`.

## Discussion

The implementation of your block needs to check for a value in the `error` parameter and, if that parameter is `nil`, incorporate the route information from the `response` parameter.

## See Also

### Getting the directions

- [- calculateDirectionsWithCompletionHandler:](<calculate(completionhandler_).md>) — Begins calculating the requested route information asynchronously.
- [Response](response.md) — The route information that Apple servers return in response to your request for directions.

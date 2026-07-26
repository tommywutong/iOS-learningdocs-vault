---
title: MKDirections.ETAHandler
framework: MapKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkdirections/etahandler
source_url: 'https://developer.apple.com/documentation/mapkit/mkdirections/etahandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkdirections/etahandler.json'
content_hash: 'sha256:6c023ed9cba79d5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKDirections](../mkdirections.md)

# MKDirections.ETAHandler

<sub>Type Alias</sub>

The block to use for processing travel-time information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias ETAHandler = (MKDirections.ETAResponse?, (any Error)?) -> Void
```

## Parameters

- `response` — The `response` parameter contains the travel-time response. If an error occurs or the framework can’t determine the travel time, this parameter is `nil`.

- `error` — The `error` parameter contains information about any errors that occur. If no errors occur, this parameter is `nil`.

## Discussion

The implementation of your block needs to check for a value in the `error` parameter and, if that parameter is `nil`, incorporate the travel-time information from the `response` parameter.

## See Also

### Getting the ETA

- [- calculateETAWithCompletionHandler:](<calculateeta(completionhandler_).md>) — Begins calculating the requested travel-time information asynchronously.
- [ETAResponse](etaresponse.md) — The travel-time information that Apple servers return.

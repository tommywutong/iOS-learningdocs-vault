---
title: MKLocalSearch.CompletionHandler
framework: MapKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mklocalsearch/completionhandler
source_url: 'https://developer.apple.com/documentation/mapkit/mklocalsearch/completionhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklocalsearch/completionhandler.json'
content_hash: 'sha256:28ff12058e9e6963'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKLocalSearch](../mklocalsearch.md)

# MKLocalSearch.CompletionHandler

<sub>Type Alias</sub>

A completion handler block for a search operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CompletionHandler = (MKLocalSearch.Response?, (any Error)?) -> Void
```

## Discussion

This block takes two parameters:

- The `response` parameter contains the search results. If an error occurs, this parameter is `nil` and the framework provides an appropriate error object in the `error` parameter.
- The `error` parameter is `nil` if the search is successful. If an error occurs during the operation, the framework sets this parameter to an appropriate error object.

This block has no return value.

## See Also

### Performing the search

- [- startWithCompletionHandler:](<start(completionhandler_).md>) — Starts the search and delivers the results to the specified completion handler.
- [searching](issearching.md) — A Boolean value that indicates whether the search is in progress.
- [- cancel](<cancel().md>) — Cancels an in-progress search operation.

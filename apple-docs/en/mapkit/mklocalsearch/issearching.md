---
title: isSearching
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.1+, iPadOS 6.1+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mklocalsearch/issearching
source_url: 'https://developer.apple.com/documentation/mapkit/mklocalsearch/issearching'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklocalsearch/issearching.json'
content_hash: 'sha256:c5fa0fb7d989aa61'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKLocalSearch](../mklocalsearch.md)

# isSearching

<sub>Instance Property</sub>

A Boolean value that indicates whether the search is in progress.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isSearching: Bool { get }
```

## Discussion

The search object sets the value of this property to [true](../../swift/true.md) when you initiate a search. It remains in that state until the search object delivers search results (or an appropriate error), at which time the search object sets the value of the property to [false](../../swift/false.md).

## See Also

### Performing the search

- [- startWithCompletionHandler:](<start(completionhandler_).md>) — Starts the search and delivers the results to the specified completion handler.
- [CompletionHandler](completionhandler.md) — A completion handler block for a search operation.
- [- cancel](<cancel().md>) — Cancels an in-progress search operation.

---
title: cancel()
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.1+, iPadOS 6.1+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mklocalsearch/cancel()
source_url: 'https://developer.apple.com/documentation/mapkit/mklocalsearch/cancel()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklocalsearch/cancel%28%29.json'
content_hash: 'sha256:30b8caff4f3f0b2e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKLocalSearch](../mklocalsearch.md)

# cancel()

<sub>Instance Method</sub>

Cancels an in-progress search operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cancel()
```

## Discussion

If no search operation is in progress, this method does nothing.

## See Also

### Performing the search

- [- startWithCompletionHandler:](<start(completionhandler_).md>) — Starts the search and delivers the results to the specified completion handler.
- [CompletionHandler](completionhandler.md) — A completion handler block for a search operation.
- [searching](issearching.md) — A Boolean value that indicates whether the search is in progress.

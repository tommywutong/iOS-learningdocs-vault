---
title: 'start(completionHandler:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.1+, iPadOS 6.1+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mklocalsearch/start(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mklocalsearch/start(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklocalsearch/start%28completionhandler%3A%29.json'
content_hash: 'sha256:969eb6839eeb5b09'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKLocalSearch](../mklocalsearch.md)

# start(completionHandler:)

<sub>Instance Method</sub>

Starts the search and delivers the results to the specified completion handler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func start(completionHandler: @escaping @MainActor @Sendable (MKLocalSearch.Response?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func start() async throws -> MKLocalSearch.Response
```

## Parameters

- `completionHandler` — The completion handler block that processes the results. This parameter can’t be `nil`.

## Discussion

You use this method to initiate a map-based search operation. The search runs until the framework delivers the results, at which point the framework calls the specified completion handler.

Call this method only once to start the search operation. Calling this method while the search is running doesn’t stop the original search operation from finishing. However, for each subsequent call, the search object executes your completion handler and passes an error object to it.

The provided completion handler executes on your app’s main thread. The local search object keeps a reference to the completion handler block until the search object delivers the results (or an error), at which point, it relinquishes that reference.

## See Also

### Performing the search

- [CompletionHandler](completionhandler.md) — A completion handler block for a search operation.
- [searching](issearching.md) — A Boolean value that indicates whether the search is in progress.
- [- cancel](<cancel().md>) — Cancels an in-progress search operation.

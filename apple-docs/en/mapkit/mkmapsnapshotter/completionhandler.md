---
title: MKMapSnapshotter.CompletionHandler
framework: MapKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapsnapshotter/completionhandler
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/completionhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapsnapshotter/completionhandler.json'
content_hash: 'sha256:7857afd715428e1e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapSnapshotter](../mkmapsnapshotter.md)

# MKMapSnapshotter.CompletionHandler

<sub>Type Alias</sub>

A block that processes the results of a snapshot request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CompletionHandler = (MKMapSnapshotter.Snapshot?, (any Error)?) -> Void
```

## Parameters

- `snapshot` — The image data that the snapshotter generates, or `nil` if an error occurs.

- `error` — The error that occurs, or `nil` if the framework generates the snapshot successfully.

## See Also

### Generating a snapshot

- [- startWithCompletionHandler:](<start(completionhandler_).md>) — Submits the request to create a snapshot and delivers the results to the specified block.
- [- startWithQueue:completionHandler:](<start(with_completionhandler_).md>) — Submits the request to create a snapshot and executes the resulting block on the specified queue.
- [- cancel](<cancel().md>) — Cancels the request to create a snapshot.
- [loading](isloading.md) — A Boolean value that indicates whether the snapshotter is generating an image.

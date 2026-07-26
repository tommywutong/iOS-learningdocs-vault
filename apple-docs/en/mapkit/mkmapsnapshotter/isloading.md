---
title: isLoading
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapsnapshotter/isloading
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/isloading'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapsnapshotter/isloading.json'
content_hash: 'sha256:c78c28767080ce4d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapSnapshotter](../mkmapsnapshotter.md)

# isLoading

<sub>Instance Property</sub>

A Boolean value that indicates whether the snapshotter is generating an image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isLoading: Bool { get }
```

## See Also

### Generating a snapshot

- [- startWithCompletionHandler:](<start(completionhandler_).md>) — Submits the request to create a snapshot and delivers the results to the specified block.
- [- startWithQueue:completionHandler:](<start(with_completionhandler_).md>) — Submits the request to create a snapshot and executes the resulting block on the specified queue.
- [CompletionHandler](completionhandler.md) — A block that processes the results of a snapshot request.
- [- cancel](<cancel().md>) — Cancels the request to create a snapshot.

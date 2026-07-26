---
title: cancel()
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapsnapshotter/cancel()
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/cancel()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapsnapshotter/cancel%28%29.json'
content_hash: 'sha256:bfb024b53c777896'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapSnapshotter](../mkmapsnapshotter.md)

# cancel()

<sub>Instance Method</sub>

Cancels the request to create a snapshot.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cancel()
```

## Discussion

If the snapshotter isn’t in the process of generating the snapshot, calling this method does nothing.

## See Also

### Generating a snapshot

- [- startWithCompletionHandler:](<start(completionhandler_).md>) — Submits the request to create a snapshot and delivers the results to the specified block.
- [- startWithQueue:completionHandler:](<start(with_completionhandler_).md>) — Submits the request to create a snapshot and executes the resulting block on the specified queue.
- [CompletionHandler](completionhandler.md) — A block that processes the results of a snapshot request.
- [loading](isloading.md) — A Boolean value that indicates whether the snapshotter is generating an image.

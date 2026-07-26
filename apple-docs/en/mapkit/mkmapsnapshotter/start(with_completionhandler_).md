---
title: 'start(with:completionHandler:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapsnapshotter/start(with:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/start(with:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapsnapshotter/start%28with%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:4259f4301e7a8869'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapSnapshotter](../mkmapsnapshotter.md)

# start(with:completionHandler:)

<sub>Instance Method</sub>

Submits the request to create a snapshot and executes the resulting block on the specified queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func start(with queue: dispatch_queue_t, completionHandler: @escaping @Sendable (MKMapSnapshotter.Snapshot?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func start(with queue: dispatch_queue_t) async throws -> MKMapSnapshotter.Snapshot
```

## Parameters

- `queue` — The dispatch queue on which to execute the block that the `completionHandler` parameter specifies.

- `completionHandler` — The block to call with the resulting snapshot. This block can’t be `nil`.

## Discussion

Call this method to begin generating a snapshot image based on the specified parameters. This method executes the request asynchronously. When rendering is complete, the snapshotter delivers the results to your block on the dispatch queue in the `queue` parameter.

The snapshotter delivers the final image to your app only when it’s running in the foreground. The snapshotter needs to render the final image while your app is in the foreground. If you start generating a snapshot while the app is in the background, or if your app moves to the background while a snapshot is in progress, this behavior delays the delivery of the snapshot until your app returns to the foreground.

In macOS, this method creates both standard and high-resolution representations of the map data and includes both in the returned image object. In iOS, you need to specify the image scale you want using the snapshot options, which defaults to the scale on the current device.

## See Also

### Generating a snapshot

- [- startWithCompletionHandler:](<start(completionhandler_).md>) — Submits the request to create a snapshot and delivers the results to the specified block.
- [CompletionHandler](completionhandler.md) — A block that processes the results of a snapshot request.
- [- cancel](<cancel().md>) — Cancels the request to create a snapshot.
- [loading](isloading.md) — A Boolean value that indicates whether the snapshotter is generating an image.

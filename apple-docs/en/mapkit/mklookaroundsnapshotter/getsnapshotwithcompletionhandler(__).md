---
title: 'getSnapshotWithCompletionHandler(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mklookaroundsnapshotter/getsnapshotwithcompletionhandler(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mklookaroundsnapshotter/getsnapshotwithcompletionhandler(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklookaroundsnapshotter/getsnapshotwithcompletionhandler%28_%3A%29.json'
content_hash: 'sha256:5ca89601d3348366'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKLookAroundSnapshotter](../mklookaroundsnapshotter.md)

# getSnapshotWithCompletionHandler(_:)

<sub>Instance Method</sub>

Requests a new snapshot and calls the completion handler you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func getSnapshotWithCompletionHandler(_ completionHandler: @escaping @MainActor @Sendable (MKLookAroundSnapshotter.Snapshot?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var snapshot: MKLookAroundSnapshotter.Snapshot { get async throws }
```

## Parameters

- `completionHandler` — A completion handler the framework calls to indicate the success or failure of the snapshot request.

## See Also

### Starting and stopping a snapshot

- [- cancel](<cancel().md>) — Cancels an in-progress snapshot request.

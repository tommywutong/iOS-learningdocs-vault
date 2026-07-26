---
title: 'getSceneWithCompletionHandler(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mklookaroundscenerequest/getscenewithcompletionhandler(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mklookaroundscenerequest/getscenewithcompletionhandler(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklookaroundscenerequest/getscenewithcompletionhandler%28_%3A%29.json'
content_hash: 'sha256:c3e380f358fcc478'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKLookAroundSceneRequest](../mklookaroundscenerequest.md)

# getSceneWithCompletionHandler(_:)

<sub>Instance Method</sub>

Requests a LookAround scene and calls the specified completion handler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func getSceneWithCompletionHandler(_ completionHandler: @escaping @MainActor @Sendable (MKLookAroundScene?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var scene: MKLookAroundScene? { get async throws }
```

## Parameters

- `completionHandler` — A completion handler the framework calls when the scene request completes to indicate the success or failure of the request.

## See Also

### Starting and stopping scene requests

- [- cancel](<cancel().md>) — Cancels the pending scene request.

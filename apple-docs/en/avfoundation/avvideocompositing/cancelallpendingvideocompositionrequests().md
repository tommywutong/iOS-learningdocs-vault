---
title: cancelAllPendingVideoCompositionRequests()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocompositing/cancelallpendingvideocompositionrequests()
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositing/cancelallpendingvideocompositionrequests()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositing/cancelallpendingvideocompositionrequests%28%29.json'
content_hash: 'sha256:373077c4d3b9e740'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositing](../avvideocompositing.md)

# cancelAllPendingVideoCompositionRequests()

<sub>Instance Method</sub>

Directs a custom video compositor object to cancel or finish all pending video composition requests.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func cancelAllPendingVideoCompositionRequests()
```

## Discussion

Upon receiving this message, a custom video compositor must block until it has either cancelled all pending frame requests, and called the [- finishCancelledRequest](<../avasynchronousvideocompositionrequest/finishcancelledrequest().md>) method for each of them. If cancellation is not possible, the method must block until it has finished processing of all the frames and called the [- finishWithComposedVideoFrame:](<../avasynchronousvideocompositionrequest/finish(withcomposedvideoframe_).md>) method for each of them.

## See Also

### Rendering the composition

- [- startVideoCompositionRequest:](<startrequest(__).md>) — Directs a custom video compositor object to create a new pixel buffer composed asynchronously from a collection of sources.
- [AVAsynchronousVideoCompositionRequest](../avasynchronousvideocompositionrequest.md) — An object that contains information a video compositor needs to render an output pixel buffer.

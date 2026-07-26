---
title: 'startRequest(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avvideocompositing/startrequest(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositing/startrequest(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositing/startrequest%28_%3A%29.json'
content_hash: 'sha256:5e57a10fb4565820'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositing](../avvideocompositing.md)

# startRequest(_:)

<sub>Instance Method</sub>

Directs a custom video compositor object to create a new pixel buffer composed asynchronously from a collection of sources.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func startRequest(_ asyncVideoCompositionRequest: AVAsynchronousVideoCompositionRequest)
```

## Parameters

- `asyncVideoCompositionRequest` — An instance of [AVAsynchronousVideoCompositionRequest](../avasynchronousvideocompositionrequest.md) that provides context for the requested composition.

## Discussion

The custom compositor is expected to invoke, either subsequently or immediately,  the `asyncVideoCompositionRequest` object’s [- finishWithComposedVideoFrame:](<../avasynchronousvideocompositionrequest/finish(withcomposedvideoframe_).md>) or [- finishWithError:](<../avasynchronousvideocompositionrequest/finish(with_).md>) methods.

If you intend to finish rendering the frame after  handling of this message returns, you must retain `asyncVideoCompositionRequest` until after composition is finished.

Note that if the custom compositor’s implementation of this method returns without finishing the composition immediately, it may be invoked again with another composition request before the prior request is finished; in such cases the custom compositor should be prepared to manage multiple composition requests.

If the rendered frame is exactly the same as one of the source frames, with no letterboxing, pillboxing or cropping needed, then the appropriate source pixel buffer may be returned, after [CFRetain](../../corefoundation/cfretain.md) has been called on it).

## See Also

### Rendering the composition

- [AVAsynchronousVideoCompositionRequest](../avasynchronousvideocompositionrequest.md) — An object that contains information a video compositor needs to render an output pixel buffer.
- [- cancelAllPendingVideoCompositionRequests](<cancelallpendingvideocompositionrequests().md>) — Directs a custom video compositor object to cancel or finish all pending video composition requests.

---
title: 'finish(withComposedTaggedBuffers:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avasynchronousvideocompositionrequest/finish(withcomposedtaggedbuffers:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/finish(withcomposedtaggedbuffers:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasynchronousvideocompositionrequest/finish%28withcomposedtaggedbuffers%3A%29.json'
content_hash: 'sha256:e32b147e06dd51ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsynchronousVideoCompositionRequest](../avasynchronousvideocompositionrequest.md)

# finish(withComposedTaggedBuffers:)

<sub>Instance Method</sub>

The method that the custom compositor calls when composition succeeds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func finish(withComposedTaggedBuffers taggedBuffers: [CMTaggedDynamicBuffer])
```

## Parameters

- `taggedBuffers` — The tagged buffers containing the composed tagged buffers. The tagged buffers must be compatible with the outputBufferDescription specified in the video composition. The outputBufferDescription must not be nil when calling this function. NOTE: If `AVVideoComposition/spatialConfigurations` is not empty, then `attach(spatialVideoConfiguration:to:)` must be called with one of the spatial configurations. An exception will be thrown otherwise. Also, all pixel buffers must be associated with the same spatial configuration. An exception will be thrown otherwise.

## See Also

### Finishing the request

- [- finishWithComposedVideoFrame:](<finish(withcomposedvideoframe_).md>) — Finishes the request to compose the frame. _(deprecated)_
- [finish(withComposedPixelBuffer:)](<finish(withcomposedpixelbuffer_).md>) — The method that the custom compositor calls when composition succeeds.
- [- finishWithError:](<finish(with_).md>) — Finishes the request with an error.
- [- finishCancelledRequest](<finishcancelledrequest().md>) — Cancels the request to compose a video frame.

---
title: 'finish(with:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avasynchronousvideocompositionrequest/finish(with:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/finish(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasynchronousvideocompositionrequest/finish%28with%3A%29.json'
content_hash: 'sha256:72f79b5deff332c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsynchronousVideoCompositionRequest](../avasynchronousvideocompositionrequest.md)

# finish(with:)

<sub>Instance Method</sub>

Finishes the request with an error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func finish(with error: any Error)
```

## Parameters

- `error` — Returns the error encountered during the compositing.

## Discussion

A custom compositor calls this method to indicate that the attempt to compose a frame failed.

## See Also

### Finishing the request

- [- finishWithComposedVideoFrame:](<finish(withcomposedvideoframe_).md>) — Finishes the request to compose the frame. _(deprecated)_
- [finish(withComposedPixelBuffer:)](<finish(withcomposedpixelbuffer_).md>) — The method that the custom compositor calls when composition succeeds.
- [finish(withComposedTaggedBuffers:)](<finish(withcomposedtaggedbuffers_).md>) — The method that the custom compositor calls when composition succeeds.
- [- finishCancelledRequest](<finishcancelledrequest().md>) — Cancels the request to compose a video frame.

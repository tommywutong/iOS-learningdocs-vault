---
title: 'finish(withComposedPixelBuffer:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avasynchronousvideocompositionrequest/finish(withcomposedpixelbuffer:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/finish(withcomposedpixelbuffer:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasynchronousvideocompositionrequest/finish%28withcomposedpixelbuffer%3A%29.json'
content_hash: 'sha256:42e5d3f292fad625'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsynchronousVideoCompositionRequest](../avasynchronousvideocompositionrequest.md)

# finish(withComposedPixelBuffer:)

<sub>Instance Method</sub>

The method that the custom compositor calls when composition succeeds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func finish(withComposedPixelBuffer readOnlyPixelBuffer: CVReadOnlyPixelBuffer)
```

## See Also

### Finishing the request

- [- finishWithComposedVideoFrame:](<finish(withcomposedvideoframe_).md>) — Finishes the request to compose the frame. _(deprecated)_
- [finish(withComposedTaggedBuffers:)](<finish(withcomposedtaggedbuffers_).md>) — The method that the custom compositor calls when composition succeeds.
- [- finishWithError:](<finish(with_).md>) — Finishes the request with an error.
- [- finishCancelledRequest](<finishcancelledrequest().md>) — Cancels the request to compose a video frame.

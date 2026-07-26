---
title: finishCancelledRequest()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avasynchronousvideocompositionrequest/finishcancelledrequest()
source_url: 'https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/finishcancelledrequest()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasynchronousvideocompositionrequest/finishcancelledrequest%28%29.json'
content_hash: 'sha256:c178cd50315de507'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsynchronousVideoCompositionRequest](../avasynchronousvideocompositionrequest.md)

# finishCancelledRequest()

<sub>Instance Method</sub>

Cancels the request to compose a video frame.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func finishCancelledRequest()
```

## See Also

### Finishing the request

- [- finishWithComposedVideoFrame:](<finish(withcomposedvideoframe_).md>) — Finishes the request to compose the frame. _(deprecated)_
- [finish(withComposedPixelBuffer:)](<finish(withcomposedpixelbuffer_).md>) — The method that the custom compositor calls when composition succeeds.
- [finish(withComposedTaggedBuffers:)](<finish(withcomposedtaggedbuffers_).md>) — The method that the custom compositor calls when composition succeeds.
- [- finishWithError:](<finish(with_).md>) — Finishes the request with an error.

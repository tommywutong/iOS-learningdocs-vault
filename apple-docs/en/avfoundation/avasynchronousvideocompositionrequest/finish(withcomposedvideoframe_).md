---
title: 'finish(withComposedVideoFrame:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+（27.0 起废弃）, iPadOS 7.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.9+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avasynchronousvideocompositionrequest/finish(withcomposedvideoframe:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/finish(withcomposedvideoframe:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasynchronousvideocompositionrequest/finish%28withcomposedvideoframe%3A%29.json'
content_hash: 'sha256:c3758a293e481f98'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsynchronousVideoCompositionRequest](../avasynchronousvideocompositionrequest.md)

# finish(withComposedVideoFrame:)

<sub>Instance Method</sub>

Finishes the request to compose the frame.

> [!warning] Deprecated
> Use finish(withComposedVideoFrame: CVReadOnlyPixelBuffer) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func finish(withComposedVideoFrame composedVideoFrame: CVPixelBuffer)
```

## Parameters

- `composedVideoFrame` — The successfully composed pixel buffer.

## Discussion

A custom compositor calls this method to indicate that it’s composed a frame successfully.

## See Also

### Finishing the request

- [finish(withComposedPixelBuffer:)](<finish(withcomposedpixelbuffer_).md>) — The method that the custom compositor calls when composition succeeds.
- [finish(withComposedTaggedBuffers:)](<finish(withcomposedtaggedbuffers_).md>) — The method that the custom compositor calls when composition succeeds.
- [- finishWithError:](<finish(with_).md>) — Finishes the request with an error.
- [- finishCancelledRequest](<finishcancelledrequest().md>) — Cancels the request to compose a video frame.

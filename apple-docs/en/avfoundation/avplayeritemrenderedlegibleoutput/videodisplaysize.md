---
title: videoDisplaySize
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemrenderedlegibleoutput/videodisplaysize
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemrenderedlegibleoutput/videodisplaysize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemrenderedlegibleoutput/videodisplaysize.json'
content_hash: 'sha256:e668d7bd39b53b4e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemRenderedLegibleOutput](../avplayeritemrenderedlegibleoutput.md)

# videoDisplaySize

<sub>Instance Property</sub>

Set the video display size to use for rendering of pixel buffers.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var videoDisplaySize: CGSize { get set }
```

## Discussion

The output renders the pixel buffers according to the width and height of display area. If you set this property during the presentation time of a vended caption image, the output vends a new image rendered at the new size.

> [!important] Important
> Attempting to set a video display size of [zero](../../corefoundation/cgsize/zero.md) results in the system throwing an exception.

## See Also

### Configuring an output

- [advanceIntervalForDelegateInvocation](advanceintervalfordelegateinvocation.md) — Permits advance invocation of the associated delegate, if any.

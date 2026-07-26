---
title: 'renderedLegibleOutput(_:didOutputRenderedCaptionImages:forItemTime:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritemrenderedlegibleoutputpushdelegate/renderedlegibleoutput(_:didoutputrenderedcaptionimages:foritemtime:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemrenderedlegibleoutputpushdelegate/renderedlegibleoutput(_:didoutputrenderedcaptionimages:foritemtime:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemrenderedlegibleoutputpushdelegate/renderedlegibleoutput%28_%3Adidoutputrenderedcaptionimages%3Aforitemtime%3A%29.json'
content_hash: 'sha256:de4c2fe7cd2bd2d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemRenderedLegibleOutputPushDelegate](../avplayeritemrenderedlegibleoutputpushdelegate.md)

# renderedLegibleOutput(_:didOutputRenderedCaptionImages:forItemTime:)

<sub>Instance Method</sub>

Tells the delegate that new rendered caption images are available.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
optional func renderedLegibleOutput(_ output: AVPlayerItemRenderedLegibleOutput, didOutputRenderedCaptionImages captionImages: [AVRenderedCaptionImage], forItemTime itemTime: CMTime)
```

## Parameters

- `output` — The rendered legible output object.

- `captionImages` — An array of [AVRenderedCaptionImage](../avrenderedcaptionimage.md) objects. A caption object consists of a [CVPixelBuffer](../../corevideo/cvpixelbuffer-q2e.md) and its associated position, in pixels, relative to the video frame.

- `itemTime` — The item time at which to present the caption images.

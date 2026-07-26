---
title: pixelBuffer
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+（27.0 起废弃）, iPadOS 18.0+（27.0 起废弃）, Mac Catalyst 18.0+（27.0 起废弃）, macOS 15.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avrenderedcaptionimage/pixelbuffer
source_url: 'https://developer.apple.com/documentation/avfoundation/avrenderedcaptionimage/pixelbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avrenderedcaptionimage/pixelbuffer.json'
content_hash: 'sha256:827771d0a6387b42'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVRenderedCaptionImage](../avrenderedcaptionimage.md)

# pixelBuffer

<sub>Instance Property</sub>

An object that contains pixel data for the rendered caption.

> [!warning] Deprecated
> Use readOnlyPixelBuffer instead

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var pixelBuffer: CVPixelBuffer { get }
```

## See Also

### Inspecting the image

- [readOnlyPixelBuffer](readonlypixelbuffer.md) — A CVReadOnlyPixelBuffer that contains pixel data for the rendered caption
- [position](position.md) — A point that defines the position, in pixels, of the rendered caption image relative to the video frame.

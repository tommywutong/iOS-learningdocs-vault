---
title: pixelBufferAttributes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerlayer/pixelbufferattributes
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerlayer/pixelbufferattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerlayer/pixelbufferattributes.json'
content_hash: 'sha256:ba1bb6f2a07f9b27'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerLayer](../avplayerlayer.md)

# pixelBufferAttributes

<sub>Instance Property</sub>

The attributes of the visual output that displays in the player layer during playback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var pixelBufferAttributes: [String : Any]? { get set }
```

## Discussion

Use this property to customize the format of the pixel buffers that the player layer vends.

## See Also

### Processing pixel buffers

- [- copyDisplayedPixelBuffer](<displayedpixelbuffer().md>) — Returns the pixel buffer that the player layer currently displays. _(deprecated)_
- [displayedReadOnlyPixelBuffer()](<displayedreadonlypixelbuffer().md>) — Returns the pixel buffer which is currently being displayed.

---
title: displayedReadOnlyPixelBuffer()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerlayer/displayedreadonlypixelbuffer()
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerlayer/displayedreadonlypixelbuffer()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerlayer/displayedreadonlypixelbuffer%28%29.json'
content_hash: 'sha256:f471dbbecd5db1aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerLayer](../avplayerlayer.md)

# displayedReadOnlyPixelBuffer()

<sub>Instance Method</sub>

Returns the pixel buffer which is currently being displayed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func displayedReadOnlyPixelBuffer() -> CVReadOnlyPixelBuffer?
```

## Return Value

A CVReadOnlyPixelBuffer object.

## Discussion

CVReadOnlyPixelBuffer can be nil if the current player’s rate is non-zero, displayed pixel buffer is protected, no image is currently being displayed, or if the image is unavailable.

## See Also

### Processing pixel buffers

- [pixelBufferAttributes](pixelbufferattributes.md) — The attributes of the visual output that displays in the player layer during playback.
- [- copyDisplayedPixelBuffer](<displayedpixelbuffer().md>) — Returns the pixel buffer that the player layer currently displays. _(deprecated)_

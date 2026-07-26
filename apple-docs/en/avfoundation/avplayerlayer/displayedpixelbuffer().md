---
title: displayedPixelBuffer()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+（27.0 起废弃）, iPadOS 16.0+（27.0 起废弃）, Mac Catalyst 16.0+（27.0 起废弃）, macOS 13.0+（27.0 起废弃）, tvOS 16.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avplayerlayer/displayedpixelbuffer()
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerlayer/displayedpixelbuffer()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerlayer/displayedpixelbuffer%28%29.json'
content_hash: 'sha256:02812cf5dc35bf67'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerLayer](../avplayerlayer.md)

# displayedPixelBuffer()

<sub>Instance Method</sub>

Returns the pixel buffer that the player layer currently displays.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func displayedPixelBuffer() -> CVPixelBuffer?
```

## Return Value

The currently displayed pixel buffer, or `nil` if one isn’t available.

## Discussion

This method only returns an image when playback is in a paused state, and otherwise returns `nil`. It also returns `nil` when displaying protected content or if the layer isn’t currently displaying an image.

## See Also

### Processing pixel buffers

- [pixelBufferAttributes](pixelbufferattributes.md) — The attributes of the visual output that displays in the player layer during playback.
- [displayedReadOnlyPixelBuffer()](<displayedreadonlypixelbuffer().md>) — Returns the pixel buffer which is currently being displayed.

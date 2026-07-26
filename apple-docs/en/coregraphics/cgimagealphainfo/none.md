---
title: CGImageAlphaInfo.none
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgimagealphainfo/none
source_url: 'https://developer.apple.com/documentation/coregraphics/cgimagealphainfo/none'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgimagealphainfo/none.json'
content_hash: 'sha256:b31911284b77f153'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGImageAlphaInfo](../cgimagealphainfo.md)

# CGImageAlphaInfo.none

<sub>Case</sub>

There is no alpha channel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case none
```

## See Also

### Constants

- [kCGImageAlphaFirst](first.md) — The alpha component is stored in the most significant bits of each pixel. For example, non-premultiplied ARGB.
- [kCGImageAlphaLast](last.md) — The alpha component is stored in the least significant bits of each pixel. For example, non-premultiplied RGBA.
- [kCGImageAlphaNoneSkipFirst](noneskipfirst.md) — There is no alpha channel. If the total size of the pixel is greater than the space required for the number of color components in the color space, the most significant bits are ignored.
- [kCGImageAlphaOnly](alphaonly.md) — There is no color data, only an alpha channel.
- [kCGImageAlphaNoneSkipLast](noneskiplast.md) — There is no alpha channel.
- [kCGImageAlphaPremultipliedFirst](premultipliedfirst.md) — The alpha component is stored in the most significant bits of each pixel and the color components have already been multiplied by this alpha value. For example, premultiplied ARGB.
- [kCGImageAlphaPremultipliedLast](premultipliedlast.md) — The alpha component is stored in the least significant bits of each pixel and the color components have already been multiplied by this alpha value. For example, premultiplied RGBA.

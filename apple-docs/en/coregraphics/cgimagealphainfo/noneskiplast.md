---
title: CGImageAlphaInfo.noneSkipLast
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgimagealphainfo/noneskiplast
source_url: 'https://developer.apple.com/documentation/coregraphics/cgimagealphainfo/noneskiplast'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgimagealphainfo/noneskiplast.json'
content_hash: 'sha256:734c5b53460f5b5f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGImageAlphaInfo](../cgimagealphainfo.md)

# CGImageAlphaInfo.noneSkipLast

<sub>Case</sub>

There is no alpha channel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case noneSkipLast
```

## See Also

### Constants

- [kCGImageAlphaFirst](first.md) — The alpha component is stored in the most significant bits of each pixel. For example, non-premultiplied ARGB.
- [kCGImageAlphaLast](last.md) — The alpha component is stored in the least significant bits of each pixel. For example, non-premultiplied RGBA.
- [kCGImageAlphaNone](none.md) — There is no alpha channel.
- [kCGImageAlphaNoneSkipFirst](noneskipfirst.md) — There is no alpha channel. If the total size of the pixel is greater than the space required for the number of color components in the color space, the most significant bits are ignored.
- [kCGImageAlphaOnly](alphaonly.md) — There is no color data, only an alpha channel.
- [kCGImageAlphaPremultipliedFirst](premultipliedfirst.md) — The alpha component is stored in the most significant bits of each pixel and the color components have already been multiplied by this alpha value. For example, premultiplied ARGB.
- [kCGImageAlphaPremultipliedLast](premultipliedlast.md) — The alpha component is stored in the least significant bits of each pixel and the color components have already been multiplied by this alpha value. For example, premultiplied RGBA.

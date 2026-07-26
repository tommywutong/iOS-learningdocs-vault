---
title: framebufferOnly
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cametallayer/framebufferonly
source_url: 'https://developer.apple.com/documentation/quartzcore/cametallayer/framebufferonly'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cametallayer/framebufferonly.json'
content_hash: 'sha256:f5a3841700683426'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAMetalLayer](../cametallayer.md)

# framebufferOnly

<sub>Instance Property</sub>

A Boolean value that determines whether the layer’s textures are used only for rendering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var framebufferOnly: Bool { get set }
```

## Discussion

If the value is [true](../../swift/true.md) (the default), the [CAMetalLayer](../cametallayer.md) class allocates its [MTLTexture](../../metal/mtltexture.md) objects with only the [renderTarget](../../metal/mtltextureusage/rendertarget.md) usage flag. Core Animation can then optimize the texture for display purposes. However, you may not sample, read from, or write to those textures. To support sampling and pixel read/write operations (at a cost to performance), set this value to [false](../../swift/false.md).

## See Also

### Configuring the Layer’s Drawable Objects

- [pixelFormat](pixelformat.md) — The pixel format of the layer’s textures.
- [colorspace](colorspace.md) — The color space of the rendered content.
- [drawableSize](drawablesize.md) — The size, in pixels, of textures for rendering layer content.

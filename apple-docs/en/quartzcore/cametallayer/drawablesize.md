---
title: drawableSize
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cametallayer/drawablesize
source_url: 'https://developer.apple.com/documentation/quartzcore/cametallayer/drawablesize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cametallayer/drawablesize.json'
content_hash: 'sha256:b718bd18b2d2db5a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAMetalLayer](../cametallayer.md)

# drawableSize

<sub>Instance Property</sub>

The size, in pixels, of textures for rendering layer content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var drawableSize: CGSize { get set }
```

## Discussion

By default, a layer creates textures sized to match its content—that is, this property’s value is the layer’s [bounds](../calayer/bounds.md) size multiplied by its [contentsScale](../calayer/contentsscale.md) factor.

## See Also

### Configuring the Layer’s Drawable Objects

- [pixelFormat](pixelformat.md) — The pixel format of the layer’s textures.
- [colorspace](colorspace.md) — The color space of the rendered content.
- [framebufferOnly](framebufferonly.md) — A Boolean value that determines whether the layer’s textures are used only for rendering.

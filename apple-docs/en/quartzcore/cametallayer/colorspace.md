---
title: colorspace
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cametallayer/colorspace
source_url: 'https://developer.apple.com/documentation/quartzcore/cametallayer/colorspace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cametallayer/colorspace.json'
content_hash: 'sha256:8ceda733114246c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAMetalLayer](../cametallayer.md)

# colorspace

<sub>Instance Property</sub>

The color space of the rendered content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var colorspace: CGColorSpace? { get set }
```

## Discussion

Set this value to specify a color space for the contents of the layer. When a color space is present, Core Animation performs any necessary color space transformations when compositing this content.

The default value is `nil`, indicating that the rendered content isn’t color-matched.

## See Also

### Configuring the Layer’s Drawable Objects

- [pixelFormat](pixelformat.md) — The pixel format of the layer’s textures.
- [framebufferOnly](framebufferonly.md) — A Boolean value that determines whether the layer’s textures are used only for rendering.
- [drawableSize](drawablesize.md) — The size, in pixels, of textures for rendering layer content.

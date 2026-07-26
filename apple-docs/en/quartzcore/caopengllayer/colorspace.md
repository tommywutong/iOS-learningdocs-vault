---
title: colorspace
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.5+（10.14 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/quartzcore/caopengllayer/colorspace
source_url: 'https://developer.apple.com/documentation/quartzcore/caopengllayer/colorspace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caopengllayer/colorspace.json'
content_hash: 'sha256:39a81d46731b953c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAOpenGLLayer](../caopengllayer.md)

# colorspace

<sub>Instance Property</sub>

The layer’s colorspace in Core Graphics.

> [!warning] Deprecated
> OpenGL is deprecated. (Define GL_SILENCE_DEPRECATION to silence these warnings)

<sub>Mac Catalyst, macOS</sub>

```swift
var colorspace: CGColorSpace? { get set }
```

## See Also

### Determining Layer Properties

- [wantsExtendedDynamicRangeContent](wantsextendeddynamicrangecontent.md) — Tells whether or not the layer supports content with extended dynamic range. _(deprecated)_

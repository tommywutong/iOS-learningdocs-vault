---
title: allowsFontSubpixelQuantization
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/catextlayer/allowsfontsubpixelquantization
source_url: 'https://developer.apple.com/documentation/quartzcore/catextlayer/allowsfontsubpixelquantization'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catextlayer/allowsfontsubpixelquantization.json'
content_hash: 'sha256:ae08ec03aa843a73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CATextLayer](../catextlayer.md)

# allowsFontSubpixelQuantization

<sub>Instance Property</sub>

Determines whether to allow subpixel quantization for the graphics context used for text rendering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var allowsFontSubpixelQuantization: Bool { get set }
```

## Discussion

When enabled, the graphics context used for text rendering may quantize the subpixel positions of glyphs.

## See Also

### Text Visual Properties

- [font](font.md) — The font used to render the receiver’s text.
- [fontSize](fontsize.md) — The font size used to render the receiver’s text. Animatable.
- [foregroundColor](foregroundcolor.md) — The color used to render the receiver’s text. Animatable.

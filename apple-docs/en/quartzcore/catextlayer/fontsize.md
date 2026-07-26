---
title: fontSize
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/catextlayer/fontsize
source_url: 'https://developer.apple.com/documentation/quartzcore/catextlayer/fontsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catextlayer/fontsize.json'
content_hash: 'sha256:d006ddfe0c152864'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CATextLayer](../catextlayer.md)

# fontSize

<sub>Instance Property</sub>

The font size used to render the receiver’s text. Animatable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var fontSize: CGFloat { get set }
```

## Discussion

Defaults to 36.0.

The `fontSize` property is only used when the [string](string.md) property is not an `NSAttributedString`.

> [!note] Note
> Implicit animation of this property is only enabled in applications compiled for macOS 10.6 and later.

## See Also

### Text Visual Properties

- [font](font.md) — The font used to render the receiver’s text.
- [foregroundColor](foregroundcolor.md) — The color used to render the receiver’s text. Animatable.
- [allowsFontSubpixelQuantization](allowsfontsubpixelquantization.md) — Determines whether to allow subpixel quantization for the graphics context used for text rendering.

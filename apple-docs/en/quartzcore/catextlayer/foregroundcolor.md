---
title: foregroundColor
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/catextlayer/foregroundcolor
source_url: 'https://developer.apple.com/documentation/quartzcore/catextlayer/foregroundcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catextlayer/foregroundcolor.json'
content_hash: 'sha256:d230adea8fd45e46'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CATextLayer](../catextlayer.md)

# foregroundColor

<sub>Instance Property</sub>

The color used to render the receiver’s text. Animatable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var foregroundColor: CGColor? { get set }
```

## Discussion

Defaults to opaque white.

The `foregroundColor` property is only used when the [string](string.md) property is not an `NSAttributedString`.

> [!note] Note
> Implicit animation of this property is only enabled in applications compiled for macOS 10.6 and later.

## See Also

### Text Visual Properties

- [font](font.md) — The font used to render the receiver’s text.
- [fontSize](fontsize.md) — The font size used to render the receiver’s text. Animatable.
- [allowsFontSubpixelQuantization](allowsfontsubpixelquantization.md) — Determines whether to allow subpixel quantization for the graphics context used for text rendering.

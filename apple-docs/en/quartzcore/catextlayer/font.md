---
title: font
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/catextlayer/font
source_url: 'https://developer.apple.com/documentation/quartzcore/catextlayer/font'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catextlayer/font.json'
content_hash: 'sha256:c14f328a58d9f103'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CATextLayer](../catextlayer.md)

# font

<sub>Instance Property</sub>

The font used to render the receiver’s text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var font: CFTypeRef? { get set }
```

## Discussion

May be either a [CTFont](../../coretext/ctfont.md), a [CGFont](../../coregraphics/cgfont.md), an instance of `NSFont` (macOS only), or a string naming the font. In iOS, you cannot assign a [UIFont](../../uikit/uifont.md) object to this property. Defaults to Helvetica.

The `font` property is only used when the [string](string.md) property is not an `NSAttributedString`.

> [!note] Note
> If the font property is a `CTFontRef`, a `CGFontRef`, or an instance of `NSFont`, the font size of the property is ignored.

## See Also

### Text Visual Properties

- [fontSize](fontsize.md) — The font size used to render the receiver’s text. Animatable.
- [foregroundColor](foregroundcolor.md) — The color used to render the receiver’s text. Animatable.
- [allowsFontSubpixelQuantization](allowsfontsubpixelquantization.md) — Determines whether to allow subpixel quantization for the graphics context used for text rendering.

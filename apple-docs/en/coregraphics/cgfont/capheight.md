---
title: capHeight
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgfont/capheight
source_url: 'https://developer.apple.com/documentation/coregraphics/cgfont/capheight'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgfont/capheight.json'
content_hash: 'sha256:4dbce96da7c41748'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGFont](../cgfont.md)

# capHeight

<sub>Instance Property</sub>

Returns the cap height of a font.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var capHeight: Int32 { get }
```

## Discussion

The cap height is the distance above the baseline of the top of flat capital letters of glyphs in a font. The value is specified in glyph space units.

## See Also

### Examining Font Metrics

- [CGFontGetAscent](ascent.md) — Returns the ascent of a font.
- [CGFontGetDescent](descent.md) — Returns the descent of a font.
- [CGFontGetFontBBox](fontbbox.md) — Returns the bounding box of a font.
- [CGFontGetItalicAngle](italicangle.md) — Returns the italic angle of a font.
- [CGFontGetLeading](leading.md) — Returns the leading of a font.
- [CGFontGetStemV](stemv.md) — Returns the thickness of the dominant vertical stems of glyphs in a font.
- [CGFontGetUnitsPerEm](unitsperem.md) — Returns the number of glyph space units per em for the provided font.
- [CGFontGetXHeight](xheight.md) — Returns the x-height of a font.

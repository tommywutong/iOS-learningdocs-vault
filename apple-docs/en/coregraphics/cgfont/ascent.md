---
title: ascent
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgfont/ascent
source_url: 'https://developer.apple.com/documentation/coregraphics/cgfont/ascent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgfont/ascent.json'
content_hash: 'sha256:dfe9151af91489b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGFont](../cgfont.md)

# ascent

<sub>Instance Property</sub>

Returns the ascent of a font.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var ascent: Int32 { get }
```

## Discussion

The ascent is the maximum distance above the baseline of glyphs in a font. The value is specified in glyph space  units.

## See Also

### Examining Font Metrics

- [CGFontGetCapHeight](capheight.md) — Returns the cap height of a font.
- [CGFontGetDescent](descent.md) — Returns the descent of a font.
- [CGFontGetFontBBox](fontbbox.md) — Returns the bounding box of a font.
- [CGFontGetItalicAngle](italicangle.md) — Returns the italic angle of a font.
- [CGFontGetLeading](leading.md) — Returns the leading of a font.
- [CGFontGetStemV](stemv.md) — Returns the thickness of the dominant vertical stems of glyphs in a font.
- [CGFontGetUnitsPerEm](unitsperem.md) — Returns the number of glyph space units per em for the provided font.
- [CGFontGetXHeight](xheight.md) — Returns the x-height of a font.

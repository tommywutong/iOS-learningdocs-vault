---
title: 'cgGlyph(at:isValidIndex:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/cgglyph(at:isvalidindex:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/cgglyph(at:isvalidindex:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/cgglyph%28at%3Aisvalidindex%3A%29.json'
content_hash: 'sha256:fbb15d7784ca8672'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# cgGlyph(at:isValidIndex:)

<sub>Instance Method</sub>

Returns the glyph at the specified index along with information about whether the glyph index is valid.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func cgGlyph(at glyphIndex: Int, isValidIndex: UnsafeMutablePointer<ObjCBool>?) -> CGGlyph
```

## Parameters

- `glyphIndex` — The index of the glyph that you want.

- `isValidIndex` — An optional Boolean variable. On return, the variable is set to [true](../../swift/true.md) if the glyph index is valid or [false](../../swift/false.md) if it is not.

## Return Value

The glyph at the specified index or [kCGFontIndexInvalid](../../coregraphics/kcgfontindexinvalid.md) if the index is out of range.

## Discussion

If noncontiguous layout is disabled, calling this method generates all glyphs up to and including the one at `glyphIndex`.

## See Also

### Accessing glyphs

- [- getGlyphsInRange:glyphs:properties:characterIndexes:bidiLevels:](<getglyphs(in_glyphs_properties_characterindexes_bidilevels_).md>) — Fills a passed-in buffer with a sequence of glyphs.
- [- CGGlyphAtIndex:](<cgglyph(at_).md>) — Returns the glyph at the specified index.
- [- setGlyphs:properties:characterIndexes:font:forGlyphRange:](<setglyphs(__properties_characterindexes_font_forglyphrange_).md>) — Stores the initial glyphs and glyph properties for a character range.
- [- characterIndexForGlyphAtIndex:](<characterindexforglyph(at_).md>) — Returns the index in the text storage for the first character of the specified glyph.
- [- glyphIndexForCharacterAtIndex:](<glyphindexforcharacter(at_).md>) — Returns the index of the first glyph of the character at the specified index.
- [- isValidGlyphIndex:](<isvalidglyphindex(__).md>) — Indicates whether the specified index refers to a valid glyph.
- [numberOfGlyphs](numberofglyphs.md) — The number of glyphs in the layout manager.
- [- propertyForGlyphAtIndex:](<propertyforglyph(at_).md>) — Returns the glyph property of the glyph at the specified index.
- [GlyphProperty](glyphproperty.md) — Glyph properties.

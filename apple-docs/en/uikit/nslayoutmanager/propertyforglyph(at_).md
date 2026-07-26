---
title: 'propertyForGlyph(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/propertyforglyph(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/propertyforglyph(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/propertyforglyph%28at%3A%29.json'
content_hash: 'sha256:9f7c373dc40f414d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# propertyForGlyph(at:)

<sub>Instance Method</sub>

Returns the glyph property of the glyph at the specified index.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func propertyForGlyph(at glyphIndex: Int) -> NSLayoutManager.GlyphProperty
```

## Parameters

- `glyphIndex` — The glyph whose glyph property is returned.

## Return Value

The glyph property associated with the specified glyph. [GlyphProperty](glyphproperty.md) lists the values that can be returned.

## Discussion

If noncontiguous layout is not enabled, this method causes generation of all glyphs up to and including the one at `glyphIndex`.

## See Also

### Accessing glyphs

- [- getGlyphsInRange:glyphs:properties:characterIndexes:bidiLevels:](<getglyphs(in_glyphs_properties_characterindexes_bidilevels_).md>) — Fills a passed-in buffer with a sequence of glyphs.
- [- CGGlyphAtIndex:](<cgglyph(at_).md>) — Returns the glyph at the specified index.
- [- CGGlyphAtIndex:isValidIndex:](<cgglyph(at_isvalidindex_).md>) — Returns the glyph at the specified index along with information about whether the glyph index is valid.
- [- setGlyphs:properties:characterIndexes:font:forGlyphRange:](<setglyphs(__properties_characterindexes_font_forglyphrange_).md>) — Stores the initial glyphs and glyph properties for a character range.
- [- characterIndexForGlyphAtIndex:](<characterindexforglyph(at_).md>) — Returns the index in the text storage for the first character of the specified glyph.
- [- glyphIndexForCharacterAtIndex:](<glyphindexforcharacter(at_).md>) — Returns the index of the first glyph of the character at the specified index.
- [- isValidGlyphIndex:](<isvalidglyphindex(__).md>) — Indicates whether the specified index refers to a valid glyph.
- [numberOfGlyphs](numberofglyphs.md) — The number of glyphs in the layout manager.
- [GlyphProperty](glyphproperty.md) — Glyph properties.

---
title: 'characterIndexForGlyph(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/characterindexforglyph(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/characterindexforglyph(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/characterindexforglyph%28at%3A%29.json'
content_hash: 'sha256:48751ce8702e93a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# characterIndexForGlyph(at:)

<sub>Instance Method</sub>

Returns the index in the text storage for the first character of the specified glyph.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func characterIndexForGlyph(at glyphIndex: Int) -> Int
```

## Parameters

- `glyphIndex` — The index of the glyph for which to return the associated character.

## Return Value

The index of the first character associated with the glyph at the specified index.

## Discussion

If noncontiguous layout is not enabled, this method causes generation of all glyphs up to and including `glyphIndex`. This method accepts an index beyond the last glyph, returning an index extrapolated from the last actual glyph index.

In many cases it’s better to use the range-mapping methods, [- characterRangeForGlyphRange:actualGlyphRange:](<characterrange(forglyphrange_actualglyphrange_).md>) and [- glyphRangeForCharacterRange:actualCharacterRange:](<glyphrange(forcharacterrange_actualcharacterrange_).md>), which provide more comprehensive information.

## See Also

### Accessing glyphs

- [- getGlyphsInRange:glyphs:properties:characterIndexes:bidiLevels:](<getglyphs(in_glyphs_properties_characterindexes_bidilevels_).md>) — Fills a passed-in buffer with a sequence of glyphs.
- [- CGGlyphAtIndex:](<cgglyph(at_).md>) — Returns the glyph at the specified index.
- [- CGGlyphAtIndex:isValidIndex:](<cgglyph(at_isvalidindex_).md>) — Returns the glyph at the specified index along with information about whether the glyph index is valid.
- [- setGlyphs:properties:characterIndexes:font:forGlyphRange:](<setglyphs(__properties_characterindexes_font_forglyphrange_).md>) — Stores the initial glyphs and glyph properties for a character range.
- [- glyphIndexForCharacterAtIndex:](<glyphindexforcharacter(at_).md>) — Returns the index of the first glyph of the character at the specified index.
- [- isValidGlyphIndex:](<isvalidglyphindex(__).md>) — Indicates whether the specified index refers to a valid glyph.
- [numberOfGlyphs](numberofglyphs.md) — The number of glyphs in the layout manager.
- [- propertyForGlyphAtIndex:](<propertyforglyph(at_).md>) — Returns the glyph property of the glyph at the specified index.
- [GlyphProperty](glyphproperty.md) — Glyph properties.

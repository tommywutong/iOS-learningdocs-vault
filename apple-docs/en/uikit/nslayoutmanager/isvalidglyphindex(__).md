---
title: 'isValidGlyphIndex(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/isvalidglyphindex(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/isvalidglyphindex(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/isvalidglyphindex%28_%3A%29.json'
content_hash: 'sha256:0e0504807e9d04fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# isValidGlyphIndex(_:)

<sub>Instance Method</sub>

Indicates whether the specified index refers to a valid glyph.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func isValidGlyphIndex(_ glyphIndex: Int) -> Bool
```

## Parameters

- `glyphIndex` — The index of a glyph in the receiver.

## Return Value

[true](../../swift/true.md) if the specified `glyphIndex` refers to a valid glyph, otherwise [false](../../swift/false.md).

## See Also

### Accessing glyphs

- [- getGlyphsInRange:glyphs:properties:characterIndexes:bidiLevels:](<getglyphs(in_glyphs_properties_characterindexes_bidilevels_).md>) — Fills a passed-in buffer with a sequence of glyphs.
- [- CGGlyphAtIndex:](<cgglyph(at_).md>) — Returns the glyph at the specified index.
- [- CGGlyphAtIndex:isValidIndex:](<cgglyph(at_isvalidindex_).md>) — Returns the glyph at the specified index along with information about whether the glyph index is valid.
- [- setGlyphs:properties:characterIndexes:font:forGlyphRange:](<setglyphs(__properties_characterindexes_font_forglyphrange_).md>) — Stores the initial glyphs and glyph properties for a character range.
- [- characterIndexForGlyphAtIndex:](<characterindexforglyph(at_).md>) — Returns the index in the text storage for the first character of the specified glyph.
- [- glyphIndexForCharacterAtIndex:](<glyphindexforcharacter(at_).md>) — Returns the index of the first glyph of the character at the specified index.
- [numberOfGlyphs](numberofglyphs.md) — The number of glyphs in the layout manager.
- [- propertyForGlyphAtIndex:](<propertyforglyph(at_).md>) — Returns the glyph property of the glyph at the specified index.
- [GlyphProperty](glyphproperty.md) — Glyph properties.

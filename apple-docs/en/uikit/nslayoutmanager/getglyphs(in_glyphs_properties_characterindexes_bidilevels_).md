---
title: 'getGlyphs(in:glyphs:properties:characterIndexes:bidiLevels:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/getglyphs(in:glyphs:properties:characterindexes:bidilevels:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/getglyphs(in:glyphs:properties:characterindexes:bidilevels:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/getglyphs%28in%3Aglyphs%3Aproperties%3Acharacterindexes%3Abidilevels%3A%29.json'
content_hash: 'sha256:4c3a832e557224b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# getGlyphs(in:glyphs:properties:characterIndexes:bidiLevels:)

<sub>Instance Method</sub>

Fills a passed-in buffer with a sequence of glyphs.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func getGlyphs(in glyphRange: NSRange, glyphs glyphBuffer: UnsafeMutablePointer<CGGlyph>?, properties props: UnsafeMutablePointer<NSLayoutManager.GlyphProperty>?, characterIndexes charIndexBuffer: UnsafeMutablePointer<Int>?, bidiLevels bidiLevelBuffer: UnsafeMutablePointer<UInt8>?) -> Int
```

## Parameters

- `glyphRange` — The range of glyphs to fill in.

- `glyphBuffer` — On output, the sequence of glyphs in the given glyph range.

- `props` — If not `NULL`, on output, the glyph properties corresponding to the filled-in glyphs.

- `charIndexBuffer` — If not `NULL`, on output, the indexes of the original characters corresponding to the given glyph range. Note that a glyph at index 1 is not necessarily mapped to the character at index 1, since a glyph may be for a ligature or accent.

- `bidiLevelBuffer` — If not `NULL`, on output, the direction of each glyph for bidirectional text. The values range from 0 to 61 as defined by Unicode Standard Annex #9. An even value means the glyph goes left-to-right, and an odd value means the glyph goes right-to-left.

## Return Value

The number of glyphs returned in `glyphBuffer`.

## Discussion

Each pointer passed in should either be `NULL` or else point to sufficient memory to hold `glyphRange.length` elements.

## See Also

### Accessing glyphs

- [- CGGlyphAtIndex:](<cgglyph(at_).md>) — Returns the glyph at the specified index.
- [- CGGlyphAtIndex:isValidIndex:](<cgglyph(at_isvalidindex_).md>) — Returns the glyph at the specified index along with information about whether the glyph index is valid.
- [- setGlyphs:properties:characterIndexes:font:forGlyphRange:](<setglyphs(__properties_characterindexes_font_forglyphrange_).md>) — Stores the initial glyphs and glyph properties for a character range.
- [- characterIndexForGlyphAtIndex:](<characterindexforglyph(at_).md>) — Returns the index in the text storage for the first character of the specified glyph.
- [- glyphIndexForCharacterAtIndex:](<glyphindexforcharacter(at_).md>) — Returns the index of the first glyph of the character at the specified index.
- [- isValidGlyphIndex:](<isvalidglyphindex(__).md>) — Indicates whether the specified index refers to a valid glyph.
- [numberOfGlyphs](numberofglyphs.md) — The number of glyphs in the layout manager.
- [- propertyForGlyphAtIndex:](<propertyforglyph(at_).md>) — Returns the glyph property of the glyph at the specified index.
- [GlyphProperty](glyphproperty.md) — Glyph properties.

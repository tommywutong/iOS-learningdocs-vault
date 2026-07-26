---
title: 'setGlyphs(_:properties:characterIndexes:font:forGlyphRange:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/setglyphs(_:properties:characterindexes:font:forglyphrange:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/setglyphs(_:properties:characterindexes:font:forglyphrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/setglyphs%28_%3Aproperties%3Acharacterindexes%3Afont%3Aforglyphrange%3A%29.json'
content_hash: 'sha256:a66609bf8b2cc089'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# setGlyphs(_:properties:characterIndexes:font:forGlyphRange:)

<sub>Instance Method</sub>

Stores the initial glyphs and glyph properties for a character range.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setGlyphs(_ glyphs: UnsafePointer<CGGlyph>, properties props: UnsafePointer<NSLayoutManager.GlyphProperty>, characterIndexes charIndexes: UnsafePointer<Int>, font aFont: UIFont, forGlyphRange glyphRange: NSRange)
```

## Parameters

- `glyphs` — A pointer to the layout manager’s glyph cache.

- `props` — A pointer to a buffer containing glyph properties for the glyphs in the cache.

- `charIndexes` — A pointer to the starting index for the characters in the text storage for which glyphs are generated.

- `aFont` — A font to override the font attributes in the text storage for the specified character range.

- `glyphRange` — The range of glyphs in the glyph cache to set.

## Discussion

This method is invoked by text system during the glyph generation process. The only place apps are allowed to call this method directly is from an implementation of the `NSLayoutManagerDelegate` protocol method [- layoutManager:shouldGenerateGlyphs:properties:characterIndexes:font:forGlyphRange:](<../nslayoutmanagerdelegate/layoutmanager(__shouldgenerateglyphs_properties_characterindexes_font_forglyphrange_).md>).

Each array has `glyphRange.length` items. The specified `charIndexes` must be contiguous (no skipped indexes), enabling multiple items to have a same character index (as when one character index generates multiple glyph IDs). Due to font substitution, `aFont` passed into this method might not match the font in the attributes dictionary. Calling this method for a character range that has previously calculated layout information invalidates the layout and display.

## See Also

### Accessing glyphs

- [- getGlyphsInRange:glyphs:properties:characterIndexes:bidiLevels:](<getglyphs(in_glyphs_properties_characterindexes_bidilevels_).md>) — Fills a passed-in buffer with a sequence of glyphs.
- [- CGGlyphAtIndex:](<cgglyph(at_).md>) — Returns the glyph at the specified index.
- [- CGGlyphAtIndex:isValidIndex:](<cgglyph(at_isvalidindex_).md>) — Returns the glyph at the specified index along with information about whether the glyph index is valid.
- [- characterIndexForGlyphAtIndex:](<characterindexforglyph(at_).md>) — Returns the index in the text storage for the first character of the specified glyph.
- [- glyphIndexForCharacterAtIndex:](<glyphindexforcharacter(at_).md>) — Returns the index of the first glyph of the character at the specified index.
- [- isValidGlyphIndex:](<isvalidglyphindex(__).md>) — Indicates whether the specified index refers to a valid glyph.
- [numberOfGlyphs](numberofglyphs.md) — The number of glyphs in the layout manager.
- [- propertyForGlyphAtIndex:](<propertyforglyph(at_).md>) — Returns the glyph property of the glyph at the specified index.
- [GlyphProperty](glyphproperty.md) — Glyph properties.

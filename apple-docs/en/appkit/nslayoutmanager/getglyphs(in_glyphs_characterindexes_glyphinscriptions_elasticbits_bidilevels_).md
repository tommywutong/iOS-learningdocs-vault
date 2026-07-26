---
title: 'getGlyphs(in:glyphs:characterIndexes:glyphInscriptions:elasticBits:bidiLevels:)'
framework: AppKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.11 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/appkit/nslayoutmanager/getglyphs(in:glyphs:characterindexes:glyphinscriptions:elasticbits:bidilevels:)'
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutmanager/getglyphs(in:glyphs:characterindexes:glyphinscriptions:elasticbits:bidilevels:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutmanager/getglyphs%28in%3Aglyphs%3Acharacterindexes%3Aglyphinscriptions%3Aelasticbits%3Abidilevels%3A%29.json'
content_hash: 'sha256:97da92d0ba06a072'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutManager](../nslayoutmanager.md)

# getGlyphs(in:glyphs:characterIndexes:glyphInscriptions:elasticBits:bidiLevels:)

<sub>Instance Method</sub>

Returns the glyphs and information needed to perform layout for the given glyph range.

> [!warning] Deprecated
> Use -getGlyphsInRange:glyphs:properties:characterIndexes:bidiLevels: instead

<sub>macOS</sub>

```swift
func getGlyphs(in glyphRange: NSRange, glyphs glyphBuffer: UnsafeMutablePointer<NSGlyph>?, characterIndexes charIndexBuffer: UnsafeMutablePointer<Int>?, glyphInscriptions inscribeBuffer: UnsafeMutablePointer<NSGlyphInscription>?, elasticBits elasticBuffer: UnsafeMutablePointer<ObjCBool>?, bidiLevels bidiLevelBuffer: UnsafeMutablePointer<UInt8>?) -> Int
```

## Parameters

- `glyphRange` — The range of glyphs to lay out.

- `glyphBuffer` — On output, the sequence of glyphs needed to lay out the given glyph range.

- `charIndexBuffer` — On output, the indexes of the original characters corresponding to the given glyph range. Note that a glyph at index 1 is not necessarily mapped to the character at index 1, since a glyph may be for a ligature or accent.

- `inscribeBuffer` — On output, the inscription attributes for each glyph, which are used to lay out characters that are combined together. The possible values are described in `Constants`.

- `elasticBuffer` — On output, values indicating whether a glyph is elastic for each glyph. An elastic glyph can be made longer at the end of a line or when needed for justification.

- `bidiLevelBuffer` — On output, the direction of each glyph for bidirectional text. The values range from 0 to 61 as defined by Unicode Standard Annex #9. An even value means the glyph goes left-to-right, and an odd value means the glyph goes right-to-left.

## Return Value

The number of glyphs returned in `glyphBuffer`.

## Discussion

This method and [- getGlyphsInRange:glyphs:characterIndexes:glyphInscriptions:elasticBits:](<getglyphs(in_glyphs_characterindexes_glyphinscriptions_elasticbits_).md>) are intended primarily to enable the typesetter to obtain in bulk the glyphs and other information that it needs to perform layout. These methods return all glyphs in the range, including `NSNullGlyph` and not-shown glyphs.  They do not null-terminate the results. Each pointer passed in should either be `NULL`, or else point to sufficient memory to hold `glyphRange.length` elements.

## See Also

### Methods

- [- showCGGlyphs:positions:count:font:matrix:attributes:inContext:](<showcgglyphs(__positions_count_font_matrix_attributes_in_).md>) — Renders the glyphs at the specified positions, using the specified attributes. _(deprecated)_
- [- invalidateGlyphsOnLayoutInvalidationForGlyphRange:](<invalidateglyphs(onlayoutinvalidationforglyphrange_).md>) — Specifies explicitly when portions of the glyph stream depend on layout. _(deprecated)_
- [- invalidateLayoutForCharacterRange:isSoft:actualCharacterRange:](<invalidatelayout(forcharacterrange_issoft_actualcharacterrange_).md>) — Invalidates the layout information for the glyphs mapped to the given range of characters. _(deprecated)_
- [- textStorage:edited:range:changeInLength:invalidatedRange:](<textstorage(__edited_range_changeinlength_invalidatedrange_).md>) — Invalidates glyph and layout information for a portion of the text in the given text storage object. _(deprecated)_
- [- insertGlyph:atGlyphIndex:characterIndex:](<insertglyph(__atglyphindex_characterindex_).md>) — Inserts a single glyph into the glyph stream at the given index and maps it to the character at the given character index. _(deprecated)_
- [- insertGlyphs:length:forStartingGlyphAtIndex:characterIndex:](<insertglyphs(__length_forstartingglyphat_characterindex_).md>) — Inserts the given glyphs into the glyph cache at the given index and maps them to characters beginning at the given character index. _(deprecated)_
- [- glyphAtIndex:](<glyph(at_).md>) — Returns the glyph at the specified index. _(deprecated)_
- [- glyphAtIndex:isValidIndex:](<glyph(at_isvalidindex_).md>) — Returns the glyph at a specified index, and optionally returns a flag indicating whether the requested index is valid. _(deprecated)_
- [- replaceGlyphAtIndex:withGlyph:](<replaceglyph(at_withglyph_).md>) — Replaces the glyph at the given index with a new glyph. _(deprecated)_
- [- getGlyphs:range:](<getglyphs(__range_).md>) — Fills the passed-in buffer with a sequence of glyphs. _(deprecated)_
- [- getGlyphsInRange:glyphs:characterIndexes:glyphInscriptions:elasticBits:](<getglyphs(in_glyphs_characterindexes_glyphinscriptions_elasticbits_).md>) — Returns the glyphs and information needed to perform layout for the given glyph range. _(deprecated)_
- [- deleteGlyphsInRange:](<deleteglyphs(in_).md>) — Deletes the glyphs in the given range from the receiver’s glyph store. _(deprecated)_
- [- setCharacterIndex:forGlyphAtIndex:](<setcharacterindex(__forglyphat_).md>) — Sets the index of the character corresponding to the glyph at the given glyph index. _(deprecated)_
- [- intAttribute:forGlyphAtIndex:](<intattribute(__forglyphat_).md>) — Returns the value of the attribute identified by the given attribute tag for the glyph at the given index. _(deprecated)_
- [- setIntAttribute:value:forGlyphAtIndex:](<setintattribute(__value_forglyphat_).md>) — Sets a custom attribute value for a given glyph. _(deprecated)_

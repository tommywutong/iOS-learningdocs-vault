---
title: 'setLocations(_:startingGlyphIndexes:count:forGlyphRange:)'
framework: AppKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.5+（10.11 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/appkit/nslayoutmanager/setlocations(_:startingglyphindexes:count:forglyphrange:)'
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutmanager/setlocations(_:startingglyphindexes:count:forglyphrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutmanager/setlocations%28_%3Astartingglyphindexes%3Acount%3Aforglyphrange%3A%29.json'
content_hash: 'sha256:574986a36c869f5c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutManager](../nslayoutmanager.md)

# setLocations(_:startingGlyphIndexes:count:forGlyphRange:)

<sub>Instance Method</sub>

Sets locations for many glyph ranges at once.

> [!warning] Deprecated
> Use -setLocation:forStartOfGlyphRange: instead

<sub>macOS</sub>

```swift
func setLocations(_ locations: NSPointArray, startingGlyphIndexes glyphIndexes: UnsafeMutablePointer<Int>, count: Int, forGlyphRange glyphRange: NSRange)
```

## Parameters

- `locations` — The locations to which the first glyph in each range is set, relative to the origin of the glyph’s line fragment origin.

- `glyphIndexes` — Indexes in `glyphRange` of the glyphs whose locations are set.

- `count` — The number of glyphs whose locations are set.

- `glyphRange` — The entire glyph range containing all the glyphs whose locations are set.

## Discussion

This method enables the typesetter to set locations for glyph ranges in bulk. All of the specified glyph indexes should lie within the specified glyph range. The first of them should be equal to `glyphRange.location`, and the remainder should increase monotonically. Each location is set as the location for the range beginning at the corresponding glyph index, and continuing until the subsequent glyph index, or until the end of the glyph range for the last location. Thus this method is equivalent to calling [- setLocation:forStartOfGlyphRange:](<setlocation(__forstartofglyphrange_).md>) for a set of ranges covering all of the glyphs in `glyphRange`.

This method is used by the layout mechanism and should be invoked only during typesetting, in almost all cases only by the typesetter. For example, a custom typesetter might invoke it.

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
- [- getGlyphsInRange:glyphs:characterIndexes:glyphInscriptions:elasticBits:bidiLevels:](<getglyphs(in_glyphs_characterindexes_glyphinscriptions_elasticbits_bidilevels_).md>) — Returns the glyphs and information needed to perform layout for the given glyph range. _(deprecated)_
- [- deleteGlyphsInRange:](<deleteglyphs(in_).md>) — Deletes the glyphs in the given range from the receiver’s glyph store. _(deprecated)_
- [- setCharacterIndex:forGlyphAtIndex:](<setcharacterindex(__forglyphat_).md>) — Sets the index of the character corresponding to the glyph at the given glyph index. _(deprecated)_
- [- intAttribute:forGlyphAtIndex:](<intattribute(__forglyphat_).md>) — Returns the value of the attribute identified by the given attribute tag for the glyph at the given index. _(deprecated)_

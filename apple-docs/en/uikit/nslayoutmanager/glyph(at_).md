---
title: 'glyph(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/nslayoutmanager/glyph(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/glyph(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/glyph%28at%3A%29.json'
content_hash: 'sha256:868dd0c4a08e0583'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# glyph(at:)

<sub>Instance Method</sub>

Returns the glyph at the specified index.

> [!warning] Deprecated
> Use [- CGGlyphAtIndex:](<cgglyph(at_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func glyph(at glyphIndex: Int) -> CGGlyph
```

## Parameters

- `glyphIndex` — The index of a glyph in the receiver. This value must not exceed the bounds of the receiver’s glyph array.

## Return Value

The glyph at `glyphIndex`.

## Discussion

Raises an `NSRangeException` if `glyphIndex` is out of bounds.

Performs glyph generation if needed. To avoid an exception with [- glyphAtIndex:](<glyph(at_).md>) you must first check the glyph index against the number of glyphs, which requires generating all glyphs. Another method, [- glyphAtIndex:isValidIndex:](<glyph(at_isvalidindex_).md>), generates glyphs only up to the one requested, so using it can be more efficient.

## See Also

### Methods

- [- showCGGlyphs:positions:count:font:matrix:attributes:inContext:](<showcgglyphs(__positions_count_font_matrix_attributes_in_).md>) — Renders the glyphs at the specified positions, using the specified attributes. _(deprecated)_
- [invalidateGlyphs(onLayoutInvalidationForGlyphRange:)](<../../appkit/nslayoutmanager/invalidateglyphs(onlayoutinvalidationforglyphrange_).md>) — Specifies explicitly when portions of the glyph stream depend on layout. _(deprecated)_
- [invalidateLayout(forCharacterRange:isSoft:actualCharacterRange:)](<../../appkit/nslayoutmanager/invalidatelayout(forcharacterrange_issoft_actualcharacterrange_).md>) — Invalidates the layout information for the glyphs mapped to the given range of characters. _(deprecated)_
- [textStorage(_:edited:range:changeInLength:invalidatedRange:)](<../../appkit/nslayoutmanager/textstorage(__edited_range_changeinlength_invalidatedrange_).md>) — Invalidates glyph and layout information for a portion of the text in the given text storage object. _(deprecated)_
- [insertGlyph(_:atGlyphIndex:characterIndex:)](<../../appkit/nslayoutmanager/insertglyph(__atglyphindex_characterindex_).md>) — Inserts a single glyph into the glyph stream at the given index and maps it to the character at the given character index. _(deprecated)_
- [insertGlyphs(_:length:forStartingGlyphAt:characterIndex:)](<../../appkit/nslayoutmanager/insertglyphs(__length_forstartingglyphat_characterindex_).md>) — Inserts the given glyphs into the glyph cache at the given index and maps them to characters beginning at the given character index. _(deprecated)_
- [- glyphAtIndex:isValidIndex:](<glyph(at_isvalidindex_).md>) — Returns the glyph at a specified index, and optionally returns a flag indicating whether the requested index is valid. _(deprecated)_
- [replaceGlyph(at:withGlyph:)](<../../appkit/nslayoutmanager/replaceglyph(at_withglyph_).md>) — Replaces the glyph at the given index with a new glyph. _(deprecated)_
- [getGlyphs(_:range:)](<../../appkit/nslayoutmanager/getglyphs(__range_).md>) — Fills the passed-in buffer with a sequence of glyphs. _(deprecated)_
- [getGlyphs(in:glyphs:characterIndexes:glyphInscriptions:elasticBits:)](<../../appkit/nslayoutmanager/getglyphs(in_glyphs_characterindexes_glyphinscriptions_elasticbits_).md>) — Returns the glyphs and information needed to perform layout for the given glyph range. _(deprecated)_
- [getGlyphs(in:glyphs:characterIndexes:glyphInscriptions:elasticBits:bidiLevels:)](<../../appkit/nslayoutmanager/getglyphs(in_glyphs_characterindexes_glyphinscriptions_elasticbits_bidilevels_).md>) — Returns the glyphs and information needed to perform layout for the given glyph range. _(deprecated)_
- [deleteGlyphs(in:)](<../../appkit/nslayoutmanager/deleteglyphs(in_).md>) — Deletes the glyphs in the given range from the receiver’s glyph store. _(deprecated)_
- [setCharacterIndex(_:forGlyphAt:)](<../../appkit/nslayoutmanager/setcharacterindex(__forglyphat_).md>) — Sets the index of the character corresponding to the glyph at the given glyph index. _(deprecated)_
- [intAttribute(_:forGlyphAt:)](<../../appkit/nslayoutmanager/intattribute(__forglyphat_).md>) — Returns the value of the attribute identified by the given attribute tag for the glyph at the given index. _(deprecated)_
- [setIntAttribute(_:value:forGlyphAt:)](<../../appkit/nslayoutmanager/setintattribute(__value_forglyphat_).md>) — Sets a custom attribute value for a given glyph. _(deprecated)_

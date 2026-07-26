---
title: 'rectArray(forGlyphRange:withinSelectedGlyphRange:in:rectCount:)'
framework: AppKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/appkit/nslayoutmanager/rectarray(forglyphrange:withinselectedglyphrange:in:rectcount:)'
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutmanager/rectarray(forglyphrange:withinselectedglyphrange:in:rectcount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutmanager/rectarray%28forglyphrange%3Awithinselectedglyphrange%3Ain%3Arectcount%3A%29.json'
content_hash: 'sha256:41572dd3b9d30a20'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutManager](../nslayoutmanager.md)

# rectArray(forGlyphRange:withinSelectedGlyphRange:in:rectCount:)

<sub>Instance Method</sub>

Returns an array of rectangles and, by reference, the number of such rectangles, that define the region in the given container enclosing the given glyph range.

<sub>macOS</sub>

```swift
func rectArray(forGlyphRange glyphRange: NSRange, withinSelectedGlyphRange selGlyphRange: NSRange, in container: NSTextContainer, rectCount: UnsafeMutablePointer<Int>) -> NSRectArray?
```

## Parameters

- `glyphRange` — The glyph range for which to return rectangles.

- `selGlyphRange` — Selected glyphs within `glyphRange`, which can affect the size of the rectangles; it must be equal to or contain `glyphRange`. If the caller is interested in this more from an enclosing point of view rather than a selection point of view, pass `{NSNotFound, 0}` as the selected range.

- `container` — The text container in which the text is laid out.

- `rectCount` — The number of rectangles returned.

## Return Value

The array of rectangles enclosing the given range.

## Discussion

These rectangles can be used to draw the text background or highlight for the given range of characters. If a selected range is given in `selGlyphRange`, the rectangles returned are correct for drawing the selection.  Selection rectangles are generally more complicated than enclosing rectangles and supplying a selected range is the clue this method uses to determine whether to go to the trouble of doing this special work.

The number of rectangles returned isn’t necessarily the number of lines enclosing the specified range. Contiguous lines can share an enclosing rectangle, and lines broken into several fragments have a separate enclosing rectangle for each fragment.

This method will do the minimum amount of work required to answer the question.  The resulting array is owned by the layout manager and will be reused when this method, [- rectArrayForCharacterRange:withinSelectedCharacterRange:inTextContainer:rectCount:](<rectarray(forcharacterrange_withinselectedcharacterrange_in_rectcount_).md>), or [- boundingRectForGlyphRange:inTextContainer:](<boundingrect(forglyphrange_in_).md>) is called.  One of these methods may be called indirectly. If you aren’t going to use the rectangles right away, you should copy them to another location. These rectangles are always in container coordinates.

The purpose of this method is to calculate line rectangles for drawing the text background and highlighting. These rectangles don’t necessarily enclose glyphs that draw outside their line fragment rectangles; use [- boundingRectForGlyphRange:inTextContainer:](<boundingrect(forglyphrange_in_).md>) to determine the area that contains all drawing performed for a range of glyphs.

Performs glyph generation and layout if needed.

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

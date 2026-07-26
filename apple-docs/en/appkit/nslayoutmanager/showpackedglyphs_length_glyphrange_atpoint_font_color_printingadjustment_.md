---
title: 'showPackedGlyphs:length:glyphRange:atPoint:font:color:printingAdjustment:'
framework: AppKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/appkit/nslayoutmanager/showpackedglyphs:length:glyphrange:atpoint:font:color:printingadjustment:'
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutmanager/showpackedglyphs:length:glyphrange:atpoint:font:color:printingadjustment:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutmanager/showpackedglyphs%3Alength%3Aglyphrange%3Aatpoint%3Afont%3Acolor%3Aprintingadjustment%3A.json'
content_hash: 'sha256:1526d57f74fcc53f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutManager](../nslayoutmanager.md)

# showPackedGlyphs:length:glyphRange:atPoint:font:color:printingAdjustment:

<sub>Instance Method</sub>

Draws a range of glyphs.

> [!warning] Deprecated
> You should instead use [- showCGGlyphs:positions:count:font:matrix:attributes:inContext:](<showcgglyphs(__positions_count_font_matrix_attributes_in_).md>).

<sub>macOS</sub>

```objc
- (void) showPackedGlyphs:(char *) glyphs length:(NSUInteger) glyphLen glyphRange:(NSRange) glyphRange atPoint:(NSPoint) point font:(NSFont *) font color:(NSColor *) color printingAdjustment:(NSSize) printingAdjustment;
```

## Parameters

- `glyphs` — The glyphs to draw; may contain embedded `NULL` bytes.

- `glyphLen` — The number of bytes pointed at by `glyphs`; this is twice the number of glyphs contained.

- `glyphRange` — The range of glyphs to draw.

- `point` — The point at which to draw the glyphs.

- `font` — The font of the glyphs to draw.

- `color` — Color of the glyphs to draw.

- `printingAdjustment` — `NSZeroSize` when drawing to the screen, but when printing may contain values by which the nominal spacing between the characters should be adjusted.

## Discussion

The  `glyphRange`, `point`, `font`, and `color` parameters are passed in merely for information purposes. They are already set in the graphics state. If for any reason you modify the set color or font, you must restore it before returning from this method.

You should never call this method, but you might override it.

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

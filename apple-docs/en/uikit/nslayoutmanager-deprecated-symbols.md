---
title: Deprecated symbols
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nslayoutmanager-deprecated-symbols
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager-deprecated-symbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager-deprecated-symbols.json'
content_hash: 'sha256:d4d1056292b44fc7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [TextKit](textkit.md) · [NSLayoutManager](nslayoutmanager.md)

# Deprecated symbols

<sub>API Collection</sub>

Review unsupported symbols and their replacements.

## Topics

### Methods

- [- showCGGlyphs:positions:count:font:matrix:attributes:inContext:](<nslayoutmanager/showcgglyphs(__positions_count_font_matrix_attributes_in_).md>) — Renders the glyphs at the specified positions, using the specified attributes. _(deprecated)_
- [invalidateGlyphs(onLayoutInvalidationForGlyphRange:)](<../appkit/nslayoutmanager/invalidateglyphs(onlayoutinvalidationforglyphrange_).md>) — Specifies explicitly when portions of the glyph stream depend on layout. _(deprecated)_
- [invalidateLayout(forCharacterRange:isSoft:actualCharacterRange:)](<../appkit/nslayoutmanager/invalidatelayout(forcharacterrange_issoft_actualcharacterrange_).md>) — Invalidates the layout information for the glyphs mapped to the given range of characters. _(deprecated)_
- [textStorage(_:edited:range:changeInLength:invalidatedRange:)](<../appkit/nslayoutmanager/textstorage(__edited_range_changeinlength_invalidatedrange_).md>) — Invalidates glyph and layout information for a portion of the text in the given text storage object. _(deprecated)_
- [insertGlyph(_:atGlyphIndex:characterIndex:)](<../appkit/nslayoutmanager/insertglyph(__atglyphindex_characterindex_).md>) — Inserts a single glyph into the glyph stream at the given index and maps it to the character at the given character index. _(deprecated)_
- [insertGlyphs(_:length:forStartingGlyphAt:characterIndex:)](<../appkit/nslayoutmanager/insertglyphs(__length_forstartingglyphat_characterindex_).md>) — Inserts the given glyphs into the glyph cache at the given index and maps them to characters beginning at the given character index. _(deprecated)_
- [- glyphAtIndex:](<nslayoutmanager/glyph(at_).md>) — Returns the glyph at the specified index. _(deprecated)_
- [- glyphAtIndex:isValidIndex:](<nslayoutmanager/glyph(at_isvalidindex_).md>) — Returns the glyph at a specified index, and optionally returns a flag indicating whether the requested index is valid. _(deprecated)_
- [replaceGlyph(at:withGlyph:)](<../appkit/nslayoutmanager/replaceglyph(at_withglyph_).md>) — Replaces the glyph at the given index with a new glyph. _(deprecated)_
- [getGlyphs(_:range:)](<../appkit/nslayoutmanager/getglyphs(__range_).md>) — Fills the passed-in buffer with a sequence of glyphs. _(deprecated)_
- [getGlyphs(in:glyphs:characterIndexes:glyphInscriptions:elasticBits:)](<../appkit/nslayoutmanager/getglyphs(in_glyphs_characterindexes_glyphinscriptions_elasticbits_).md>) — Returns the glyphs and information needed to perform layout for the given glyph range. _(deprecated)_
- [getGlyphs(in:glyphs:characterIndexes:glyphInscriptions:elasticBits:bidiLevels:)](<../appkit/nslayoutmanager/getglyphs(in_glyphs_characterindexes_glyphinscriptions_elasticbits_bidilevels_).md>) — Returns the glyphs and information needed to perform layout for the given glyph range. _(deprecated)_
- [deleteGlyphs(in:)](<../appkit/nslayoutmanager/deleteglyphs(in_).md>) — Deletes the glyphs in the given range from the receiver’s glyph store. _(deprecated)_
- [setCharacterIndex(_:forGlyphAt:)](<../appkit/nslayoutmanager/setcharacterindex(__forglyphat_).md>) — Sets the index of the character corresponding to the glyph at the given glyph index. _(deprecated)_
- [intAttribute(_:forGlyphAt:)](<../appkit/nslayoutmanager/intattribute(__forglyphat_).md>) — Returns the value of the attribute identified by the given attribute tag for the glyph at the given index. _(deprecated)_
- [setIntAttribute(_:value:forGlyphAt:)](<../appkit/nslayoutmanager/setintattribute(__value_forglyphat_).md>) — Sets a custom attribute value for a given glyph. _(deprecated)_
- [setLocations(_:startingGlyphIndexes:count:forGlyphRange:)](<../appkit/nslayoutmanager/setlocations(__startingglyphindexes_count_forglyphrange_).md>) — Sets locations for many glyph ranges at once. _(deprecated)_
- [rectArray(forCharacterRange:withinSelectedCharacterRange:in:rectCount:)](<../appkit/nslayoutmanager/rectarray(forcharacterrange_withinselectedcharacterrange_in_rectcount_).md>) — Returns an array of rectangles and, by reference, the number of such rectangles, that define the region in the given container enclosing the given character range.
- [rectArray(forGlyphRange:withinSelectedGlyphRange:in:rectCount:)](<../appkit/nslayoutmanager/rectarray(forglyphrange_withinselectedglyphrange_in_rectcount_).md>) — Returns an array of rectangles and, by reference, the number of such rectangles, that define the region in the given container enclosing the given glyph range.
- [substituteFont(for:)](<../appkit/nslayoutmanager/substitutefont(for_).md>) — Replaces the specified font with a suitable screen font if one is available. _(deprecated)_

### Properties

- [hyphenationFactor](nslayoutmanager/hyphenationfactor.md) — The threshold controlling when hyphenation is done. _(deprecated)_
- [attributedString](nslayoutmanager-attributedstring.md) — The text storage object from which the `NSGlyphGenerator` object procures characters for glyph generation.
- [layoutOptions](nslayoutmanager-layoutoptions.md) — The layout manager’s current layout options.
- [usesScreenFonts](../appkit/nslayoutmanager/usesscreenfonts.md) — A Boolean that controls using screen fonts to calculate layout and display text. _(deprecated)_

### Types

- [Glyph Attributes](../appkit/glyph-attributes.md) — Attributes that are used only inside the glyph generation machinery, but must also be shared between components.

---
title: 'showCGGlyphs(_:positions:count:font:matrix:attributes:in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+（13.0 起废弃）, iPadOS 7.0+（13.0 起废弃）, tvOS 9.0+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/nslayoutmanager/showcgglyphs(_:positions:count:font:matrix:attributes:in:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/showcgglyphs(_:positions:count:font:matrix:attributes:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/showcgglyphs%28_%3Apositions%3Acount%3Afont%3Amatrix%3Aattributes%3Ain%3A%29.json'
content_hash: 'sha256:5f59f1fabd0f3612'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# showCGGlyphs(_:positions:count:font:matrix:attributes:in:)

<sub>Instance Method</sub>

Renders the glyphs at the specified positions, using the specified attributes.

> [!warning] Deprecated
> Use [- showCGGlyphs:positions:count:font:textMatrix:attributes:inContext:](<showcgglyphs(__positions_count_font_textmatrix_attributes_in_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func showCGGlyphs(_ glyphs: UnsafePointer<CGGlyph>, positions: UnsafePointer<CGPoint>, count glyphCount: Int, font: UIFont, matrix textMatrix: CGAffineTransform, attributes: [NSAttributedString.Key : Any] = [:], in graphicsContext: CGContext)
```

## Parameters

- `glyphs` — The glyphs to draw; may contain embedded `NULL` bytes.

- `positions` — The positions at which to draw the glyphs in the user space coordinate system.

- `glyphCount` — The number of glyphs.

- `font` — The font applied to the graphics state. This value can be different from the `NSFontAttributeName` value in the `attributes` argument because of various font substitutions that the system automatically executes.

- `textMatrix` — The affine transform mapping the text space coordinate system to the user space coordinate system. The `tx` and `ty` components of `textMatrix` are ignored since Quartz overrides them with the glyph positions.

- `attributes` — A dictionary of glyph attributes. See [Glyph Attributes](../../appkit/glyph-attributes.md) for supported keys and values.

- `graphicsContext` — If non-`nil`, `graphicsContext` is already configured according to the text attributes arguments: `font`, `textMatrix`, and `attributes`.

## Discussion

`NSLayoutManager` invokes this primitive method unless an override implementation of the deprecated [showPackedGlyphs:length:glyphRange:atPoint:font:color:printingAdjustment:](../../appkit/nslayoutmanager/showpackedglyphs_length_glyphrange_atpoint_font_color_printingadjustment_.md) method exists and this method is not overridden.

## See Also

### Methods

- [invalidateGlyphs(onLayoutInvalidationForGlyphRange:)](<../../appkit/nslayoutmanager/invalidateglyphs(onlayoutinvalidationforglyphrange_).md>) — Specifies explicitly when portions of the glyph stream depend on layout. _(deprecated)_
- [invalidateLayout(forCharacterRange:isSoft:actualCharacterRange:)](<../../appkit/nslayoutmanager/invalidatelayout(forcharacterrange_issoft_actualcharacterrange_).md>) — Invalidates the layout information for the glyphs mapped to the given range of characters. _(deprecated)_
- [textStorage(_:edited:range:changeInLength:invalidatedRange:)](<../../appkit/nslayoutmanager/textstorage(__edited_range_changeinlength_invalidatedrange_).md>) — Invalidates glyph and layout information for a portion of the text in the given text storage object. _(deprecated)_
- [insertGlyph(_:atGlyphIndex:characterIndex:)](<../../appkit/nslayoutmanager/insertglyph(__atglyphindex_characterindex_).md>) — Inserts a single glyph into the glyph stream at the given index and maps it to the character at the given character index. _(deprecated)_
- [insertGlyphs(_:length:forStartingGlyphAt:characterIndex:)](<../../appkit/nslayoutmanager/insertglyphs(__length_forstartingglyphat_characterindex_).md>) — Inserts the given glyphs into the glyph cache at the given index and maps them to characters beginning at the given character index. _(deprecated)_
- [- glyphAtIndex:](<glyph(at_).md>) — Returns the glyph at the specified index. _(deprecated)_
- [- glyphAtIndex:isValidIndex:](<glyph(at_isvalidindex_).md>) — Returns the glyph at a specified index, and optionally returns a flag indicating whether the requested index is valid. _(deprecated)_
- [replaceGlyph(at:withGlyph:)](<../../appkit/nslayoutmanager/replaceglyph(at_withglyph_).md>) — Replaces the glyph at the given index with a new glyph. _(deprecated)_
- [getGlyphs(_:range:)](<../../appkit/nslayoutmanager/getglyphs(__range_).md>) — Fills the passed-in buffer with a sequence of glyphs. _(deprecated)_
- [getGlyphs(in:glyphs:characterIndexes:glyphInscriptions:elasticBits:)](<../../appkit/nslayoutmanager/getglyphs(in_glyphs_characterindexes_glyphinscriptions_elasticbits_).md>) — Returns the glyphs and information needed to perform layout for the given glyph range. _(deprecated)_
- [getGlyphs(in:glyphs:characterIndexes:glyphInscriptions:elasticBits:bidiLevels:)](<../../appkit/nslayoutmanager/getglyphs(in_glyphs_characterindexes_glyphinscriptions_elasticbits_bidilevels_).md>) — Returns the glyphs and information needed to perform layout for the given glyph range. _(deprecated)_
- [deleteGlyphs(in:)](<../../appkit/nslayoutmanager/deleteglyphs(in_).md>) — Deletes the glyphs in the given range from the receiver’s glyph store. _(deprecated)_
- [setCharacterIndex(_:forGlyphAt:)](<../../appkit/nslayoutmanager/setcharacterindex(__forglyphat_).md>) — Sets the index of the character corresponding to the glyph at the given glyph index. _(deprecated)_
- [intAttribute(_:forGlyphAt:)](<../../appkit/nslayoutmanager/intattribute(__forglyphat_).md>) — Returns the value of the attribute identified by the given attribute tag for the glyph at the given index. _(deprecated)_
- [setIntAttribute(_:value:forGlyphAt:)](<../../appkit/nslayoutmanager/setintattribute(__value_forglyphat_).md>) — Sets a custom attribute value for a given glyph. _(deprecated)_

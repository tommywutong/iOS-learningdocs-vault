---
title: 'setIntAttribute(_:value:forGlyphAt:)'
framework: AppKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.11 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/appkit/nslayoutmanager/setintattribute(_:value:forglyphat:)'
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutmanager/setintattribute(_:value:forglyphat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutmanager/setintattribute%28_%3Avalue%3Aforglyphat%3A%29.json'
content_hash: 'sha256:3e3a25161d1b36ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutManager](../nslayoutmanager.md)

# setIntAttribute(_:value:forGlyphAt:)

<sub>Instance Method</sub>

Sets a custom attribute value for a given glyph.

> [!warning] Deprecated
> Use -setGlyphs:properties:characterIndexes:font:forGlyphRange instead

<sub>macOS</sub>

```swift
func setIntAttribute(_ attributeTag: Int, value val: Int, forGlyphAt glyphIndex: Int)
```

## Parameters

- `attributeTag` — The custom attribute.

- `val` — The new attribute value.

- `glyphIndex` — Index of the glyph whose attribute is set.

## Discussion

Custom attributes are glyph attributes such as `NSGlyphInscription` or attributes defined by subclasses. Nonnegative tags are reserved by Apple; you can define your own attributes with negative tags and set values using this method.

This method is part of the `NSGlyphStorage` protocol, for use by the glyph generator to set attributes. It is not usually necessary for anyone but the glyph generator (and perhaps the typesetter) to call it. It is provided as a public method so subclasses can extend it to accept other glyph attributes. To add new glyph attributes to the text system you must do two things. First, you need to arrange for the glyph generator or typesetter to generate and interpret it. Second, you need to subclass `NSLayoutManager` to provide someplace to store the new attribute, overriding this method and [- intAttribute:forGlyphAtIndex:](<intattribute(__forglyphat_).md>) to recognize the new attribute tags and respond to them, while passing any other attributes to the superclass implementation. The `NSLayoutManager` implementation understands the glyph attributes which it is prepared to store, as enumerated in [Glyph Attributes](../glyph-attributes.md).

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

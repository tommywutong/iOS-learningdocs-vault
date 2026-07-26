---
title: 'textStorage(_:edited:range:changeInLength:invalidatedRange:)'
framework: AppKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.11 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/appkit/nslayoutmanager/textstorage(_:edited:range:changeinlength:invalidatedrange:)'
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutmanager/textstorage(_:edited:range:changeinlength:invalidatedrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutmanager/textstorage%28_%3Aedited%3Arange%3Achangeinlength%3Ainvalidatedrange%3A%29.json'
content_hash: 'sha256:422ece8d205691a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutManager](../nslayoutmanager.md)

# textStorage(_:edited:range:changeInLength:invalidatedRange:)

<sub>Instance Method</sub>

Invalidates glyph and layout information for a portion of the text in the given text storage object.

> [!warning] Deprecated
> Use [- processEditingForTextStorage:edited:range:changeInLength:invalidatedRange:](<processediting(for_edited_range_changeinlength_invalidatedrange_).md>) instead.

<sub>macOS</sub>

```swift
func textStorage(_ str: NSTextStorage, edited editedMask: Int = [], range newCharRange: NSRange, changeInLength delta: Int, invalidatedRange invalidatedCharRange: NSRange)
```

## Parameters

- `str` — The text storage whose information is invalidated.

- `editedMask` — Specifies the nature of the changes. Its value is made by combining with the C bitwise OR operator the constants described in “Change notifications” in [NSTextStorage](../nstextstorage.md) ([NSTextStorageEditedAttributes](../nstextstorageeditactions/editedattributes.md) and [NSTextStorageEditedCharacters](../nstextstorageeditactions/editedcharacters.md)).

- `newCharRange` — Indicates the extent of characters resulting from the edits.

- `delta` — If the `NSTextStorageEditedCharacters` bit of `mask` is set, gives the number of characters added to or removed from the original range (otherwise its value is irrelevant).

- `invalidatedCharRange` — Represents the range of characters affected after attributes have been fixed. Is either equal to `newCharRange` or larger. For example, deleting a paragraph separator character invalidates the layout information for all characters in the paragraphs that precede and follow the separator.

## Discussion

This message is sent from the `NSTextStorage`object’s [- processEditing](<../nstextstorage/processediting().md>) method to indicate that its characters or attributes have changed. This method invalidates glyphs and layout for the affected characters.

For example, after replacing “The” with “Several” to produce the string “Several files couldn’t be saved”, `newCharRange` is {0, 7} and `delta` is 4. The receiver uses this information to update its character-to-glyph mapping and to update the selection range based on the change.

The [- textStorage:edited:range:changeInLength:invalidatedRange:](<textstorage(__edited_range_changeinlength_invalidatedrange_).md>) messages are sent in a series to each `NSLayoutManager` object associated with the text storage object, so the layout managers receiving them shouldn’t edit `aTextStorage` while this method is executing. If one of them does, the `newCharRange`, `delta`, and `invalidatedCharRange` arguments are incorrect for all following layout managers that receive the message.

## See Also

### Methods

- [- showCGGlyphs:positions:count:font:matrix:attributes:inContext:](<showcgglyphs(__positions_count_font_matrix_attributes_in_).md>) — Renders the glyphs at the specified positions, using the specified attributes. _(deprecated)_
- [- invalidateGlyphsOnLayoutInvalidationForGlyphRange:](<invalidateglyphs(onlayoutinvalidationforglyphrange_).md>) — Specifies explicitly when portions of the glyph stream depend on layout. _(deprecated)_
- [- invalidateLayoutForCharacterRange:isSoft:actualCharacterRange:](<invalidatelayout(forcharacterrange_issoft_actualcharacterrange_).md>) — Invalidates the layout information for the glyphs mapped to the given range of characters. _(deprecated)_
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
- [- setIntAttribute:value:forGlyphAtIndex:](<setintattribute(__value_forglyphat_).md>) — Sets a custom attribute value for a given glyph. _(deprecated)_

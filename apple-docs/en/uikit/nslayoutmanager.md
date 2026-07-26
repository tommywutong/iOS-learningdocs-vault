---
title: NSLayoutManager
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nslayoutmanager
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager.json'
content_hash: 'sha256:a491a2a39f7773cd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSLayoutManager

<sub>Class</sub>

An object that coordinates the layout and display of text characters.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class NSLayoutManager
```

## Overview

[NSLayoutManager](nslayoutmanager.md) maps Unicode character codes to glyphs, sets the glyphs in a series of [NSTextContainer](nstextcontainer.md) objects, and displays them in a series of [NSTextView](../appkit/nstextview.md) objects. In addition to its core function of laying out text, a layout manager object coordinates its text view objects, provides services to those text views to support [NSRulerView](../appkit/nsrulerview.md) instances for editing paragraph styles, and handles the layout and display of text attributes not inherent in glyphs (such as underline or strikethrough). You can create a subclass of [NSLayoutManager](nslayoutmanager.md) to handle additional text attributes, whether inherent or not.

### Text Antialiasing

[NSLayoutManager](nslayoutmanager.md) provides the threshold for text antialiasing. It looks at the `AppleAntiAliasingThreshold` default value. If the font size is smaller than or equal to this threshold size, the text is rendered aliased by [NSLayoutManager](nslayoutmanager.md). In macOS, you can change the threshold value from the Appearance pane of System Preferences.

### Thread Safety of NSLayoutManager

Generally speaking, a specific layout manager (and associated objects) should not be used in more than one block, operation, or thread at a time. Most layout managers are used on the main thread, since it is the main thread on which their text views are displayed, and since background layout occurs on the main thread.

If you want to use a layout manager on a background thread, first make sure that text views associated with that layout manager (if any) are not displayed while the layout manager is being used on the background thread, and, second, turn off background layout for that layout manager while it is being used on the background thread. The most effective way to ensure that no text view is displayed, without knowing deep implementation, is just not to connect a text view to the layout manager.

### Noncontiguous Layout

Noncontiguous layout is an optional layout manager behavior. Previously, both glyph generation and layout were always performed, in order, from the beginning to the end of the document. When noncontiguous layout is turned on, however, the layout manager gains the option of performing glyph generation or layout for one portion of the document without having done so for previous sections. This can provide significant performance improvements for large documents.

Noncontiguous layout is not turned on automatically because direct clients of `NSLayoutManager` typically have relied on the previous behavior—for example, by forcing layout for a specific glyph range, and then assuming that previous glyphs would therefore be laid out. Clients who use [NSLayoutManager](nslayoutmanager.md) only indirectly—for example, those who use [NSTextView](../appkit/nstextview.md) without directly calling the underlying layout manager—can usually turn on noncontiguous layout without difficulty. Clients using [NSLayoutManager](nslayoutmanager.md) directly need to examine their usage before turning on noncontiguous layout.

Enable noncontiguous layout using the [allowsNonContiguousLayout](nslayoutmanager/allowsnoncontiguouslayout.md) property. In addition, see the other methods in [Causing glyph generation and layout](nslayoutmanager.md#Causing-glyph-generation-and-layout), many of which enable you to ensure that glyph generation and layout are performed for specified portions of the text. The behavior of a number of other layout manager methods is affected by the state of noncontiguous layout, as noted in the discussion sections of those method descriptions.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Creating a layout manager

- [- init](<nslayoutmanager/init().md>) — Initializes a newly created layout manager object.
- [- initWithCoder:](<nslayoutmanager/init(coder_).md>) — Creates a layout manager from data in an unarchiver.

### Managing the layout process

- [delegate](nslayoutmanager/delegate.md) — The layout manager’s delegate.
- [NSLayoutManagerDelegate](nslayoutmanagerdelegate.md) — A set of optional methods that delegates of layout manager objects implement.

### Accessing the text storage

- [textStorage](nslayoutmanager/textstorage.md) — The text storage object that contains the content to lay out.
- [replaceTextStorage(_:)](<../appkit/nslayoutmanager/replacetextstorage(__).md>) — Replaces the layout manager’s current text storage object with the specified object.

### Configuring the global layout manager options

- [allowsNonContiguousLayout](nslayoutmanager/allowsnoncontiguouslayout.md) — A Boolean value that indicates whether the layout manager allows noncontiguous layout.
- [hasNonContiguousLayout](nslayoutmanager/hasnoncontiguouslayout.md) — A Boolean value that indicates whether the layout manager currently has any areas of noncontiguous layout.
- [showsInvisibleCharacters](nslayoutmanager/showsinvisiblecharacters.md) — A Boolean value that indicates whether to substitute visible glyphs for whitespace and other typically invisible characters.
- [showsControlCharacters](nslayoutmanager/showscontrolcharacters.md) — A Boolean value that indicates whether the layout manager substitutes visible glyphs for control characters in the layout.
- [usesFontLeading](nslayoutmanager/usesfontleading.md) — A Boolean value that indicates whether the layout manager uses the leading of the font.
- [backgroundLayoutEnabled](../appkit/nslayoutmanager/backgroundlayoutenabled.md) — A Boolean value that indicates whether the layout manager generates glyphs and lays them out when the app’s run loop is idle.
- [limitsLayoutForSuspiciousContents](nslayoutmanager/limitslayoutforsuspiciouscontents.md) — A Boolean value that indicates whether the layout manager avoids laying out unusually long or suspicious input.
- [usesDefaultHyphenation](nslayoutmanager/usesdefaulthyphenation.md) — A Boolean value that indicates whether the layout manager uses the default hyphenation rules to wrap lines.

### Managing the text containers

- [textContainers](nslayoutmanager/textcontainers.md) — The current text containers of the layout manager.
- [- addTextContainer:](<nslayoutmanager/addtextcontainer(__).md>) — Appends the specified text container to the series of text containers where the layout manager arranges text.
- [- insertTextContainer:atIndex:](<nslayoutmanager/inserttextcontainer(__at_).md>) — Inserts a text container at the specified index in the list of text containers.
- [- removeTextContainerAtIndex:](<nslayoutmanager/removetextcontainer(at_).md>) — Removes the text container at the specified index and invalidates the layout as necessary.
- [- setTextContainer:forGlyphRange:](<nslayoutmanager/settextcontainer(__forglyphrange_).md>) — Associates a text container with the specified range of glyphs.
- [- textContainerChangedGeometry:](<nslayoutmanager/textcontainerchangedgeometry(__).md>) — Invalidates the layout information, and possibly glyphs, for the specified text container and all subsequent text container objects.
- [textContainerChangedTextView(_:)](<../appkit/nslayoutmanager/textcontainerchangedtextview(__).md>) — Updates the information necessary to manage text view objects for the specified text container.
- [- textContainerForGlyphAtIndex:effectiveRange:](<nslayoutmanager/textcontainer(forglyphat_effectiverange_).md>) — Returns the text container that manages the layout for the specified glyph, causing layout to happen as necessary.
- [- textContainerForGlyphAtIndex:effectiveRange:withoutAdditionalLayout:](<nslayoutmanager/textcontainer(forglyphat_effectiverange_withoutadditionallayout_).md>) — Returns the text container that manages the layout for the specified glyph.
- [- usedRectForTextContainer:](<nslayoutmanager/usedrect(for_).md>) — Returns the bounding rectangle for the glyphs in the specified text container.

### Invalidating glyphs and layout

- [- invalidateDisplayForCharacterRange:](<nslayoutmanager/invalidatedisplay(forcharacterrange_).md>) — Invalidates display for the specified character range.
- [- invalidateDisplayForGlyphRange:](<nslayoutmanager/invalidatedisplay(forglyphrange_).md>) — Invalidates a range of glyphs, requiring new layout information, and updates the appropriate regions of any text views that display those glyphs.
- [- invalidateGlyphsForCharacterRange:changeInLength:actualCharacterRange:](<nslayoutmanager/invalidateglyphs(forcharacterrange_changeinlength_actualcharacterrange_).md>) — Invalidates and adjusts the glyphs in the specified character range.
- [- invalidateLayoutForCharacterRange:actualCharacterRange:](<nslayoutmanager/invalidatelayout(forcharacterrange_actualcharacterrange_).md>) — Invalidates the layout information for the glyphs that map to the specified character range.
- [- processEditingForTextStorage:edited:range:changeInLength:invalidatedRange:](<nslayoutmanager/processediting(for_edited_range_changeinlength_invalidatedrange_).md>) — Notifies the layout manager when an edit action changes the contents of its text storage object.

### Causing glyph generation and layout

- [- ensureGlyphsForCharacterRange:](<nslayoutmanager/ensureglyphs(forcharacterrange_).md>) — Forces the layout manager to generate glyphs for the specified character range if it hasn’t already.
- [- ensureGlyphsForGlyphRange:](<nslayoutmanager/ensureglyphs(forglyphrange_).md>) — Forces the layout manager to generate glyphs for the specified glyph range if it hasn’t already.
- [- ensureLayoutForBoundingRect:inTextContainer:](<nslayoutmanager/ensurelayout(forboundingrect_in_).md>) — Forces the layout manager to perform layout for the specified area in the specified text container if it hasn’t already.
- [- ensureLayoutForCharacterRange:](<nslayoutmanager/ensurelayout(forcharacterrange_).md>) — Forces the layout manager to perform layout for the specified character range if it hasn’t already.
- [- ensureLayoutForGlyphRange:](<nslayoutmanager/ensurelayout(forglyphrange_).md>) — Forces the layout manager to perform layout for the specified glyph range if it hasn’t already.
- [- ensureLayoutForTextContainer:](<nslayoutmanager/ensurelayout(for_).md>) — Forces the layout manager to perform layout for the specified text container if it hasn’t already.
- [glyphGenerator](../appkit/nslayoutmanager/glyphgenerator.md) — The glyph generator that the layout manager uses.

### Accessing glyphs

- [- getGlyphsInRange:glyphs:properties:characterIndexes:bidiLevels:](<nslayoutmanager/getglyphs(in_glyphs_properties_characterindexes_bidilevels_).md>) — Fills a passed-in buffer with a sequence of glyphs.
- [- CGGlyphAtIndex:](<nslayoutmanager/cgglyph(at_).md>) — Returns the glyph at the specified index.
- [- CGGlyphAtIndex:isValidIndex:](<nslayoutmanager/cgglyph(at_isvalidindex_).md>) — Returns the glyph at the specified index along with information about whether the glyph index is valid.
- [- setGlyphs:properties:characterIndexes:font:forGlyphRange:](<nslayoutmanager/setglyphs(__properties_characterindexes_font_forglyphrange_).md>) — Stores the initial glyphs and glyph properties for a character range.
- [- characterIndexForGlyphAtIndex:](<nslayoutmanager/characterindexforglyph(at_).md>) — Returns the index in the text storage for the first character of the specified glyph.
- [- glyphIndexForCharacterAtIndex:](<nslayoutmanager/glyphindexforcharacter(at_).md>) — Returns the index of the first glyph of the character at the specified index.
- [- isValidGlyphIndex:](<nslayoutmanager/isvalidglyphindex(__).md>) — Indicates whether the specified index refers to a valid glyph.
- [numberOfGlyphs](nslayoutmanager/numberofglyphs.md) — The number of glyphs in the layout manager.
- [- propertyForGlyphAtIndex:](<nslayoutmanager/propertyforglyph(at_).md>) — Returns the glyph property of the glyph at the specified index.
- [GlyphProperty](nslayoutmanager/glyphproperty.md) — Glyph properties.

### Setting layout information

- [- setAttachmentSize:forGlyphRange:](<nslayoutmanager/setattachmentsize(__forglyphrange_).md>) — Sets the size to use when drawing a glyph that represents an attachment.
- [- setDrawsOutsideLineFragment:forGlyphAtIndex:](<nslayoutmanager/setdrawsoutsidelinefragment(__forglyphat_).md>) — Indicates whether the specified glyph exceeds the bounds of the line fragment for its layout.
- [- setExtraLineFragmentRect:usedRect:textContainer:](<nslayoutmanager/setextralinefragmentrect(__usedrect_textcontainer_).md>) — Sets the bounds and container for the extra line fragment.
- [- setLineFragmentRect:forGlyphRange:usedRect:](<nslayoutmanager/setlinefragmentrect(__forglyphrange_usedrect_).md>) — Associates the line fragment bounds for the specified range of glyphs.
- [- setLocation:forStartOfGlyphRange:](<nslayoutmanager/setlocation(__forstartofglyphrange_).md>) — Sets the location for the first glyph in the specified range.
- [- setNotShownAttribute:forGlyphAtIndex:](<nslayoutmanager/setnotshownattribute(__forglyphat_).md>) — Sets the visibility of the glyph at the specified index.

### Getting layout information

- [- attachmentSizeForGlyphAtIndex:](<nslayoutmanager/attachmentsize(forglyphat_).md>) — Returns the size of the attachment glyph at the specified index.
- [- drawsOutsideLineFragmentForGlyphAtIndex:](<nslayoutmanager/drawsoutsidelinefragment(forglyphat_).md>) — Indicates whether the glyph draws outside its line fragment rectangle.
- [extraLineFragmentRect](nslayoutmanager/extralinefragmentrect.md) — The rectangle for the extra line fragment at the end of a document.
- [extraLineFragmentTextContainer](nslayoutmanager/extralinefragmenttextcontainer.md) — The text container for the extra line fragment rectangle.
- [extraLineFragmentUsedRect](nslayoutmanager/extralinefragmentusedrect.md) — The rectangle that encloses the insertion point in the extra line fragment rectangle.
- [- firstUnlaidCharacterIndex](<nslayoutmanager/firstunlaidcharacterindex().md>) — Returns the index for the first character in the layout manager that isn’t in the layout.
- [- firstUnlaidGlyphIndex](<nslayoutmanager/firstunlaidglyphindex().md>) — Returns the index for the first glyph in the layout manager that isn’t in the layout.
- [- getFirstUnlaidCharacterIndex:glyphIndex:](<nslayoutmanager/getfirstunlaidcharacterindex(__glyphindex_).md>) — Returns the indexes for the first character and glyph that have invalid layout information.
- [- lineFragmentRectForGlyphAtIndex:effectiveRange:](<nslayoutmanager/linefragmentrect(forglyphat_effectiverange_).md>) — Returns the rectangle for the line fragment where the glyph lies and (optionally), by reference, the entire range of glyphs in that fragment.
- [- lineFragmentRectForGlyphAtIndex:effectiveRange:withoutAdditionalLayout:](<nslayoutmanager/linefragmentrect(forglyphat_effectiverange_withoutadditionallayout_).md>) — Returns the line fragment rectangle that contains the glyph at the specified glyph index.
- [- lineFragmentUsedRectForGlyphAtIndex:effectiveRange:](<nslayoutmanager/linefragmentusedrect(forglyphat_effectiverange_).md>) — Returns the usage rectangle for the line fragment and (optionally) returns the entire range of glyphs in that fragment.
- [- lineFragmentUsedRectForGlyphAtIndex:effectiveRange:withoutAdditionalLayout:](<nslayoutmanager/linefragmentusedrect(forglyphat_effectiverange_withoutadditionallayout_).md>) — Returns the usage rectangle for the line fragment and (optionally) returns the entire range of glyphs in that fragment.
- [- locationForGlyphAtIndex:](<nslayoutmanager/location(forglyphat_).md>) — Returns the location for the specified glyph within its line fragment.
- [- notShownAttributeForGlyphAtIndex:](<nslayoutmanager/notshownattribute(forglyphat_).md>) — Indicates whether the glyph at the specified index has a visible representation.
- [- truncatedGlyphRangeInLineFragmentForGlyphAtIndex:](<nslayoutmanager/truncatedglyphrange(inlinefragmentforglyphat_).md>) — Returns the range of truncated glyphs for a line fragment that contains the specified index.

### Performing advanced layout queries

- [- boundingRectForGlyphRange:inTextContainer:](<nslayoutmanager/boundingrect(forglyphrange_in_).md>) — Returns the bounding rectangle for the specified glyphs in a container.
- [- characterIndexForPoint:inTextContainer:fractionOfDistanceBetweenInsertionPoints:](<nslayoutmanager/characterindex(for_in_fractionofdistancebetweeninsertionpoints_).md>) — Returns the index of the character that lies beneath the specified point using the specified container’s coordinate system.
- [- characterRangeForGlyphRange:actualGlyphRange:](<nslayoutmanager/characterrange(forglyphrange_actualglyphrange_).md>) — Returns the range of characters that correspond to the glyphs in the specified glyph range.
- [- enumerateEnclosingRectsForGlyphRange:withinSelectedGlyphRange:inTextContainer:usingBlock:](<nslayoutmanager/enumerateenclosingrects(forglyphrange_withinselectedglyphrange_in_using_).md>) — Enumerates enclosing rectangles for the specified glyph range in a text container.
- [- enumerateLineFragmentsForGlyphRange:usingBlock:](<nslayoutmanager/enumeratelinefragments(forglyphrange_using_).md>) — Enumerates line fragments intersecting with the specified glyph range.
- [- fractionOfDistanceThroughGlyphForPoint:inTextContainer:](<nslayoutmanager/fractionofdistancethroughglyph(for_in_).md>) — Returns the fraction of the distance between the glyph at the specified point and the next glyph.
- [- getLineFragmentInsertionPointsForCharacterAtIndex:alternatePositions:inDisplayOrder:positions:characterIndexes:](<nslayoutmanager/getlinefragmentinsertionpoints(forcharacterat_alternatepositions_indisplayorder_positions_characterindexes_).md>) — Returns insertion points in bulk for a specified line fragment.
- [- glyphIndexForPoint:inTextContainer:](<nslayoutmanager/glyphindex(for_in_).md>) — Returns the index of the glyph at the specified location in a text container.
- [- glyphIndexForPoint:inTextContainer:fractionOfDistanceThroughGlyph:](<nslayoutmanager/glyphindex(for_in_fractionofdistancethroughglyph_).md>) — Returns the index of the glyph at the specified point using the container’s coordinate system.
- [- glyphRangeForBoundingRect:inTextContainer:](<nslayoutmanager/glyphrange(forboundingrect_in_).md>) — Returns the smallest contiguous range for glyphs lying wholly or partially within the specified rectangle of the text container.
- [- glyphRangeForBoundingRectWithoutAdditionalLayout:inTextContainer:](<nslayoutmanager/glyphrange(forboundingrectwithoutadditionallayout_in_).md>) — Returns the smallest contiguous range for glyphs lying wholly or partially within the specified rectangle of the text container.
- [- glyphRangeForTextContainer:](<nslayoutmanager/glyphrange(for_).md>) — Returns the range of glyphs lying within the specified text container.
- [- glyphRangeForCharacterRange:actualCharacterRange:](<nslayoutmanager/glyphrange(forcharacterrange_actualcharacterrange_).md>) — Returns the range of glyphs that the specified range of characters generates.
- [- rangeOfNominallySpacedGlyphsContainingIndex:](<nslayoutmanager/range(ofnominallyspacedglyphscontaining_).md>) — Returns the range of displayable glyphs that surround the glyph at the specified index.

### Drawing

- [- drawBackgroundForGlyphRange:atPoint:](<nslayoutmanager/drawbackground(forglyphrange_at_).md>) — Draws background marks for the specified glyphs, which must lie completely within a single text container.
- [- drawGlyphsForGlyphRange:atPoint:](<nslayoutmanager/drawglyphs(forglyphrange_at_).md>) — Draws the specified glyphs, which must lie completely within a single text container.
- [- drawStrikethroughForGlyphRange:strikethroughType:baselineOffset:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:](<nslayoutmanager/drawstrikethrough(forglyphrange_strikethroughtype_baselineoffset_linefragmentrect_linefragmentglyphrange_containerorigin_).md>) — Draws a strikethrough for the specified glyphs.
- [- drawUnderlineForGlyphRange:underlineType:baselineOffset:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:](<nslayoutmanager/drawunderline(forglyphrange_underlinetype_baselineoffset_linefragmentrect_linefragmentglyphrange_containerorigin_).md>) — Draws underlining for the glyphs in a specified range.
- [- fillBackgroundRectArray:count:forCharacterRange:color:](<nslayoutmanager/fillbackgroundrectarray(__count_forcharacterrange_color_).md>) — Fills background rectangles with a color.
- [- showCGGlyphs:positions:count:font:textMatrix:attributes:inContext:](<nslayoutmanager/showcgglyphs(__positions_count_font_textmatrix_attributes_in_).md>) — Renders the glyphs at the specified positions, using the specified attributes.
- [- strikethroughGlyphRange:strikethroughType:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:](<nslayoutmanager/strikethroughglyphrange(__strikethroughtype_linefragmentrect_linefragmentglyphrange_containerorigin_).md>) — Calculates and draws strikethrough for the specified glyphs.
- [- underlineGlyphRange:underlineType:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:](<nslayoutmanager/underlineglyphrange(__underlinetype_linefragmentrect_linefragmentglyphrange_containerorigin_).md>) — Calculates subranges to underline for the specified glyphs and draws the underlining as appropriate.

### Handling layout for text blocks

- [setLayoutRect(_:for:glyphRange:)](<../appkit/nslayoutmanager/setlayoutrect(__for_glyphrange_).md>) — Sets the layout rectangle that encloses the specified text block and glyph range.
- [layoutRect(for:glyphRange:)](<../appkit/nslayoutmanager/layoutrect(for_glyphrange_).md>) — Returns the rectangle for the layout of the specified text block and glyph range.
- [setBoundsRect(_:for:glyphRange:)](<../appkit/nslayoutmanager/setboundsrect(__for_glyphrange_).md>) — Sets the bounding rectangle that encloses the specified text block and glyph range.
- [boundsRect(for:glyphRange:)](<../appkit/nslayoutmanager/boundsrect(for_glyphrange_).md>) — Returns the bounding rectangle that encloses the specified text block and glyph range.
- [layoutRect(for:at:effectiveRange:)](<../appkit/nslayoutmanager/layoutrect(for_at_effectiverange_).md>) — Returns the rectangle for the layout of the specified text block and glyph.
- [boundsRect(for:at:effectiveRange:)](<../appkit/nslayoutmanager/boundsrect(for_at_effectiverange_).md>) — Returns the bounding rectangle for the specified text block and glyph.

### Managing attachments

- [defaultAttachmentScaling](../appkit/nslayoutmanager/defaultattachmentscaling.md) — The default amount of scaling to apply when an attachment image is too large to fit in a text container.
- [showAttachmentCell(_:in:characterIndex:)](<../appkit/nslayoutmanager/showattachmentcell(__in_characterindex_).md>) — Draws an attachment cell.

### Handling Rulers

- [rulerAccessoryView(for:paragraphStyle:ruler:enabled:)](<../appkit/nslayoutmanager/ruleraccessoryview(for_paragraphstyle_ruler_enabled_).md>) — Returns the accessory view that the text system uses for its ruler.
- [rulerMarkers(for:paragraphStyle:ruler:)](<../appkit/nslayoutmanager/rulermarkers(for_paragraphstyle_ruler_).md>) — Returns an array of text ruler objects for the current selection.

### Managing the responder chain

- [layoutManagerOwnsFirstResponder(in:)](<../appkit/nslayoutmanager/layoutmanagerownsfirstresponder(in_).md>) — Indicates whether the first responder in the specified window is a text view for the layout manager.
- [firstTextView](../appkit/nslayoutmanager/firsttextview.md) — The first text view in the layout manager’s series of text views.
- [textViewForBeginningOfSelection](../appkit/nslayoutmanager/textviewforbeginningofselection.md) — The text view that contains the first glyph in the selection.

### Managing the typesetter

- [typesetter](../appkit/nslayoutmanager/typesetter.md) — The current typesetter.
- [typesetterBehavior](../appkit/nslayoutmanager/typesetterbehavior-swift.property.md) — The default typesetter behavior.
- [NSLayoutManager.TypesetterBehavior](../appkit/nslayoutmanager/typesetterbehavior-swift.enum.md) — Constants that determine the layout manager’s behavior during layout.
- [defaultLineHeight(for:)](<../appkit/nslayoutmanager/defaultlineheight(for_).md>) — Returns the default line height for a line of text that uses a specified font.
- [defaultBaselineOffset(for:)](<../appkit/nslayoutmanager/defaultbaselineoffset(for_).md>) — Returns the default baseline offset that the layout manager’s typesetter uses for the specified font.

### Managing temporary attribute support

- [addTemporaryAttributes(_:forCharacterRange:)](<../appkit/nslayoutmanager/addtemporaryattributes(__forcharacterrange_).md>) — Appends one or more temporary attributes to the attributes dictionary of the specified character range.
- [addTemporaryAttribute(_:value:forCharacterRange:)](<../appkit/nslayoutmanager/addtemporaryattribute(__value_forcharacterrange_).md>) — Adds a temporary attribute to the characters in the specified range.
- [setTemporaryAttributes(_:forCharacterRange:)](<../appkit/nslayoutmanager/settemporaryattributes(__forcharacterrange_).md>) — Sets one or more temporary attributes for the specified character range.
- [removeTemporaryAttribute(_:forCharacterRange:)](<../appkit/nslayoutmanager/removetemporaryattribute(__forcharacterrange_).md>) — Removes a temporary attribute from the list of attributes for the specified character range.
- [temporaryAttribute(_:atCharacterIndex:effectiveRange:)](<../appkit/nslayoutmanager/temporaryattribute(__atcharacterindex_effectiverange_).md>) — Returns the value for the temporary attribute of a character, and the range it applies to.
- [temporaryAttribute(_:atCharacterIndex:longestEffectiveRange:in:)](<../appkit/nslayoutmanager/temporaryattribute(__atcharacterindex_longesteffectiverange_in_).md>) — Returns the value for the temporary attribute of a character, and the maximum range it applies to.
- [temporaryAttributes(atCharacterIndex:effectiveRange:)](<../appkit/nslayoutmanager/temporaryattributes(atcharacterindex_effectiverange_).md>) — Returns the dictionary of temporary attributes for the specified character range.
- [temporaryAttributes(atCharacterIndex:longestEffectiveRange:in:)](<../appkit/nslayoutmanager/temporaryattributes(atcharacterindex_longesteffectiverange_in_).md>) — Returns the temporary attributes for a character, and the maximum range they apply to.

### Supporting types

- [TextLayoutOrientation](nslayoutmanager/textlayoutorientation.md) — Constants that describe the text layout orientation.

### Deprecated

- [Deprecated symbols](nslayoutmanager-deprecated-symbols.md) — Review unsupported symbols and their replacements.

## See Also

### TextKit 1

- [NSTextStorage](nstextstorage.md) — The fundamental storage mechanism of TextKit that contains the text managed by the system.

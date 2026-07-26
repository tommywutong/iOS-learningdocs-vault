---
title: 'lineFragmentRect(forGlyphAt:effectiveRange:withoutAdditionalLayout:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/linefragmentrect(forglyphat:effectiverange:withoutadditionallayout:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/linefragmentrect(forglyphat:effectiverange:withoutadditionallayout:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/linefragmentrect%28forglyphat%3Aeffectiverange%3Awithoutadditionallayout%3A%29.json'
content_hash: 'sha256:b65b54e1c376ec67'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# lineFragmentRect(forGlyphAt:effectiveRange:withoutAdditionalLayout:)

<sub>Instance Method</sub>

Returns the line fragment rectangle that contains the glyph at the specified glyph index.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func lineFragmentRect(forGlyphAt glyphIndex: Int, effectiveRange effectiveGlyphRange: NSRangePointer?, withoutAdditionalLayout flag: Bool) -> CGRect
```

## Parameters

- `glyphIndex` — The glyph for which to return the line fragment rectangle.

- `effectiveGlyphRange` — If not `NULL`, on output, the range for all glyphs in the line fragment.

- `flag` — If [true](../../swift/true.md), glyph generation and layout are not performed, so this option should not be used unless layout is known to be complete for the range in question, or unless noncontiguous layout is enabled; if [false](../../swift/false.md), both are performed as needed.

## Return Value

The line fragment in which the given glyph is laid out.

## Discussion

This method is primarily for use from within `NSTypesetter`, after layout is complete for the range in question, but before the layout manager’s call to `NSTypesetter` has returned. In that case glyph and layout holes have not yet been recalculated, so the layout manager does not yet know that layout is complete for that range, and this variant must be used.

Overriding this method is not recommended. If the line fragment rectangle needs to be modified, that should be done at the typesetter level or by calling [- setLineFragmentRect:forGlyphRange:usedRect:](<setlinefragmentrect(__forglyphrange_usedrect_).md>).

## See Also

### Related Documentation

- [- setLineFragmentRect:forGlyphRange:usedRect:](<setlinefragmentrect(__forglyphrange_usedrect_).md>) — Associates the line fragment bounds for the specified range of glyphs.

### Getting layout information

- [- attachmentSizeForGlyphAtIndex:](<attachmentsize(forglyphat_).md>) — Returns the size of the attachment glyph at the specified index.
- [- drawsOutsideLineFragmentForGlyphAtIndex:](<drawsoutsidelinefragment(forglyphat_).md>) — Indicates whether the glyph draws outside its line fragment rectangle.
- [extraLineFragmentRect](extralinefragmentrect.md) — The rectangle for the extra line fragment at the end of a document.
- [extraLineFragmentTextContainer](extralinefragmenttextcontainer.md) — The text container for the extra line fragment rectangle.
- [extraLineFragmentUsedRect](extralinefragmentusedrect.md) — The rectangle that encloses the insertion point in the extra line fragment rectangle.
- [- firstUnlaidCharacterIndex](<firstunlaidcharacterindex().md>) — Returns the index for the first character in the layout manager that isn’t in the layout.
- [- firstUnlaidGlyphIndex](<firstunlaidglyphindex().md>) — Returns the index for the first glyph in the layout manager that isn’t in the layout.
- [- getFirstUnlaidCharacterIndex:glyphIndex:](<getfirstunlaidcharacterindex(__glyphindex_).md>) — Returns the indexes for the first character and glyph that have invalid layout information.
- [- lineFragmentRectForGlyphAtIndex:effectiveRange:](<linefragmentrect(forglyphat_effectiverange_).md>) — Returns the rectangle for the line fragment where the glyph lies and (optionally), by reference, the entire range of glyphs in that fragment.
- [- lineFragmentUsedRectForGlyphAtIndex:effectiveRange:](<linefragmentusedrect(forglyphat_effectiverange_).md>) — Returns the usage rectangle for the line fragment and (optionally) returns the entire range of glyphs in that fragment.
- [- lineFragmentUsedRectForGlyphAtIndex:effectiveRange:withoutAdditionalLayout:](<linefragmentusedrect(forglyphat_effectiverange_withoutadditionallayout_).md>) — Returns the usage rectangle for the line fragment and (optionally) returns the entire range of glyphs in that fragment.
- [- locationForGlyphAtIndex:](<location(forglyphat_).md>) — Returns the location for the specified glyph within its line fragment.
- [- notShownAttributeForGlyphAtIndex:](<notshownattribute(forglyphat_).md>) — Indicates whether the glyph at the specified index has a visible representation.
- [- truncatedGlyphRangeInLineFragmentForGlyphAtIndex:](<truncatedglyphrange(inlinefragmentforglyphat_).md>) — Returns the range of truncated glyphs for a line fragment that contains the specified index.

---
title: extraLineFragmentRect
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nslayoutmanager/extralinefragmentrect
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/extralinefragmentrect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/extralinefragmentrect.json'
content_hash: 'sha256:d0ff66d4deaec527'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# extraLineFragmentRect

<sub>Instance Property</sub>

The rectangle for the extra line fragment at the end of a document.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var extraLineFragmentRect: CGRect { get }
```

## Discussion

The layout manager uses the extra line fragment when the last character in a document causes a line or paragraph break. This extra line fragment has no corresponding glyph.

The rectangle is defined in the coordinate system of its `NSTextContainer`. `NSZeroRect` if there is no such rectangle.

## See Also

### Related Documentation

- [- setExtraLineFragmentRect:usedRect:textContainer:](<setextralinefragmentrect(__usedrect_textcontainer_).md>) — Sets the bounds and container for the extra line fragment.

### Getting layout information

- [- attachmentSizeForGlyphAtIndex:](<attachmentsize(forglyphat_).md>) — Returns the size of the attachment glyph at the specified index.
- [- drawsOutsideLineFragmentForGlyphAtIndex:](<drawsoutsidelinefragment(forglyphat_).md>) — Indicates whether the glyph draws outside its line fragment rectangle.
- [extraLineFragmentTextContainer](extralinefragmenttextcontainer.md) — The text container for the extra line fragment rectangle.
- [extraLineFragmentUsedRect](extralinefragmentusedrect.md) — The rectangle that encloses the insertion point in the extra line fragment rectangle.
- [- firstUnlaidCharacterIndex](<firstunlaidcharacterindex().md>) — Returns the index for the first character in the layout manager that isn’t in the layout.
- [- firstUnlaidGlyphIndex](<firstunlaidglyphindex().md>) — Returns the index for the first glyph in the layout manager that isn’t in the layout.
- [- getFirstUnlaidCharacterIndex:glyphIndex:](<getfirstunlaidcharacterindex(__glyphindex_).md>) — Returns the indexes for the first character and glyph that have invalid layout information.
- [- lineFragmentRectForGlyphAtIndex:effectiveRange:](<linefragmentrect(forglyphat_effectiverange_).md>) — Returns the rectangle for the line fragment where the glyph lies and (optionally), by reference, the entire range of glyphs in that fragment.
- [- lineFragmentRectForGlyphAtIndex:effectiveRange:withoutAdditionalLayout:](<linefragmentrect(forglyphat_effectiverange_withoutadditionallayout_).md>) — Returns the line fragment rectangle that contains the glyph at the specified glyph index.
- [- lineFragmentUsedRectForGlyphAtIndex:effectiveRange:](<linefragmentusedrect(forglyphat_effectiverange_).md>) — Returns the usage rectangle for the line fragment and (optionally) returns the entire range of glyphs in that fragment.
- [- lineFragmentUsedRectForGlyphAtIndex:effectiveRange:withoutAdditionalLayout:](<linefragmentusedrect(forglyphat_effectiverange_withoutadditionallayout_).md>) — Returns the usage rectangle for the line fragment and (optionally) returns the entire range of glyphs in that fragment.
- [- locationForGlyphAtIndex:](<location(forglyphat_).md>) — Returns the location for the specified glyph within its line fragment.
- [- notShownAttributeForGlyphAtIndex:](<notshownattribute(forglyphat_).md>) — Indicates whether the glyph at the specified index has a visible representation.
- [- truncatedGlyphRangeInLineFragmentForGlyphAtIndex:](<truncatedglyphrange(inlinefragmentforglyphat_).md>) — Returns the range of truncated glyphs for a line fragment that contains the specified index.

---
title: 'attachmentSize(forGlyphAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/attachmentsize(forglyphat:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/attachmentsize(forglyphat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/attachmentsize%28forglyphat%3A%29.json'
content_hash: 'sha256:92327767bf591169'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# attachmentSize(forGlyphAt:)

<sub>Instance Method</sub>

Returns the size of the attachment glyph at the specified index.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func attachmentSize(forGlyphAt glyphIndex: Int) -> CGSize
```

## Parameters

- `glyphIndex` — The index of the attachment glyph.

## Return Value

The layout manager calls this method for glyphs representing attachments, and returns the size that the attachment cell occupies. Returns `{-1.0, -1.0}` if there is no attachment laid for the specified glyph.

## See Also

### Related Documentation

- [- setAttachmentSize:forGlyphRange:](<setattachmentsize(__forglyphrange_).md>) — Sets the size to use when drawing a glyph that represents an attachment.
- [defaultAttachmentScaling](../../appkit/nslayoutmanager/defaultattachmentscaling.md) — The default amount of scaling to apply when an attachment image is too large to fit in a text container.

### Getting layout information

- [- drawsOutsideLineFragmentForGlyphAtIndex:](<drawsoutsidelinefragment(forglyphat_).md>) — Indicates whether the glyph draws outside its line fragment rectangle.
- [extraLineFragmentRect](extralinefragmentrect.md) — The rectangle for the extra line fragment at the end of a document.
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

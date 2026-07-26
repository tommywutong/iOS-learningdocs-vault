---
title: 'drawsOutsideLineFragment(forGlyphAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/drawsoutsidelinefragment(forglyphat:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/drawsoutsidelinefragment(forglyphat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/drawsoutsidelinefragment%28forglyphat%3A%29.json'
content_hash: 'sha256:a43982ff811f0805'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# drawsOutsideLineFragment(forGlyphAt:)

<sub>Instance Method</sub>

Indicates whether the glyph draws outside its line fragment rectangle.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func drawsOutsideLineFragment(forGlyphAt glyphIndex: Int) -> Bool
```

## Parameters

- `glyphIndex` — Index of the glyph.

## Return Value

[true](../../swift/true.md) if the glyph at `glyphIndex` exceeds the bounds of the line fragment where it’s laid out, [false](../../swift/false.md) otherwise.

## Discussion

Exceeding bounds can happen when text is set at a fixed line height. For example, if the user specifies a fixed line height of 12 points and sets the font size to 24 points, the glyphs will exceed their layout rectangles.

This method causes glyph generation and layout for the line fragment containing the specified glyph, or if noncontiguous layout is not enabled, up to and including that line fragment.

Glyphs that draw outside their line fragment rectangles aren’t considered when calculating enclosing rectangles with the [rectArray(forCharacterRange:withinSelectedCharacterRange:in:rectCount:)](<../../appkit/nslayoutmanager/rectarray(forcharacterrange_withinselectedcharacterrange_in_rectcount_).md>) and [rectArray(forGlyphRange:withinSelectedGlyphRange:in:rectCount:)](<../../appkit/nslayoutmanager/rectarray(forglyphrange_withinselectedglyphrange_in_rectcount_).md>) methods. They are, however, considered by [- boundingRectForGlyphRange:inTextContainer:](<boundingrect(forglyphrange_in_).md>).

## See Also

### Getting layout information

- [- attachmentSizeForGlyphAtIndex:](<attachmentsize(forglyphat_).md>) — Returns the size of the attachment glyph at the specified index.
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

---
title: 'setLineFragmentRect(_:forGlyphRange:usedRect:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/setlinefragmentrect(_:forglyphrange:usedrect:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/setlinefragmentrect(_:forglyphrange:usedrect:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/setlinefragmentrect%28_%3Aforglyphrange%3Ausedrect%3A%29.json'
content_hash: 'sha256:117f8aaa0bf2344f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# setLineFragmentRect(_:forGlyphRange:usedRect:)

<sub>Instance Method</sub>

Associates the line fragment bounds for the specified range of glyphs.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setLineFragmentRect(_ fragmentRect: CGRect, forGlyphRange glyphRange: NSRange, usedRect: CGRect)
```

## Parameters

- `fragmentRect` — The rectangle of the line fragment.

- `glyphRange` — The range of glyphs to be associated with `fragmentRect`.

- `usedRect` — The portion of `fragmentRect` that actually contains glyphs or other marks that are drawn (including the text container’s line fragment padding. Must be equal to or contained within `fragmentRect`.

## Discussion

The typesetter must specify the text container first with [- setTextContainer:forGlyphRange:](<settextcontainer(__forglyphrange_).md>), and it sets the exact positions of the glyphs afterwards with [- setLocation:forStartOfGlyphRange:](<setlocation(__forstartofglyphrange_).md>).

In the course of layout, all glyphs should end up being included in a range passed to this method, but only glyphs that start a new line fragment should be at the start of such ranges.

Line fragment rectangles and line fragment used rectangles are always in container coordinates.

This method is used by the layout mechanism and should be invoked only during typesetting, in almost all cases only by the typesetter. For example, a custom typesetter might invoke it.

## See Also

### Related Documentation

- [- lineFragmentUsedRectForGlyphAtIndex:effectiveRange:withoutAdditionalLayout:](<linefragmentusedrect(forglyphat_effectiverange_withoutadditionallayout_).md>) — Returns the usage rectangle for the line fragment and (optionally) returns the entire range of glyphs in that fragment.
- [- lineFragmentRectForGlyphAtIndex:effectiveRange:](<linefragmentrect(forglyphat_effectiverange_).md>) — Returns the rectangle for the line fragment where the glyph lies and (optionally), by reference, the entire range of glyphs in that fragment.
- [- lineFragmentRectForGlyphAtIndex:effectiveRange:withoutAdditionalLayout:](<linefragmentrect(forglyphat_effectiverange_withoutadditionallayout_).md>) — Returns the line fragment rectangle that contains the glyph at the specified glyph index.
- [- lineFragmentUsedRectForGlyphAtIndex:effectiveRange:](<linefragmentusedrect(forglyphat_effectiverange_).md>) — Returns the usage rectangle for the line fragment and (optionally) returns the entire range of glyphs in that fragment.

### Setting layout information

- [- setAttachmentSize:forGlyphRange:](<setattachmentsize(__forglyphrange_).md>) — Sets the size to use when drawing a glyph that represents an attachment.
- [- setDrawsOutsideLineFragment:forGlyphAtIndex:](<setdrawsoutsidelinefragment(__forglyphat_).md>) — Indicates whether the specified glyph exceeds the bounds of the line fragment for its layout.
- [- setExtraLineFragmentRect:usedRect:textContainer:](<setextralinefragmentrect(__usedrect_textcontainer_).md>) — Sets the bounds and container for the extra line fragment.
- [- setLocation:forStartOfGlyphRange:](<setlocation(__forstartofglyphrange_).md>) — Sets the location for the first glyph in the specified range.
- [- setNotShownAttribute:forGlyphAtIndex:](<setnotshownattribute(__forglyphat_).md>) — Sets the visibility of the glyph at the specified index.

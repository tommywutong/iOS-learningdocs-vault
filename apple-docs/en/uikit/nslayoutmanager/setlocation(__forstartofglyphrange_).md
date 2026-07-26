---
title: 'setLocation(_:forStartOfGlyphRange:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/setlocation(_:forstartofglyphrange:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/setlocation(_:forstartofglyphrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/setlocation%28_%3Aforstartofglyphrange%3A%29.json'
content_hash: 'sha256:462fac17f471b588'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# setLocation(_:forStartOfGlyphRange:)

<sub>Instance Method</sub>

Sets the location for the first glyph in the specified range.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setLocation(_ location: CGPoint, forStartOfGlyphRange glyphRange: NSRange)
```

## Parameters

- `location` — The location to which the first glyph is set, relative to the origin of the glyph’s line fragment origin.

- `glyphRange` — The glyphs whose location is set.

## Discussion

Setting the location for a glyph range implies that its first glyph is not nominally spaced with respect to the previous glyph. In the course of layout, all glyphs should end up being included in a range passed to this method, but only glyphs that start a new nominal range should be at the start of such ranges. The first glyph in a line fragment should always start a new nominal range. Glyph locations are given relative to their line fragment rectangle’s origin.

Before setting the location for a glyph range, you must specify the text container with [- setTextContainer:forGlyphRange:](<settextcontainer(__forglyphrange_).md>) and the line fragment rectangle with [- setLineFragmentRect:forGlyphRange:usedRect:](<setlinefragmentrect(__forglyphrange_usedrect_).md>).

This method is used by the layout mechanism and should be invoked only during typesetting, in almost all cases only by the typesetter. For example, a custom typesetter might invoke it.

## See Also

### Setting layout information

- [- setAttachmentSize:forGlyphRange:](<setattachmentsize(__forglyphrange_).md>) — Sets the size to use when drawing a glyph that represents an attachment.
- [- setDrawsOutsideLineFragment:forGlyphAtIndex:](<setdrawsoutsidelinefragment(__forglyphat_).md>) — Indicates whether the specified glyph exceeds the bounds of the line fragment for its layout.
- [- setExtraLineFragmentRect:usedRect:textContainer:](<setextralinefragmentrect(__usedrect_textcontainer_).md>) — Sets the bounds and container for the extra line fragment.
- [- setLineFragmentRect:forGlyphRange:usedRect:](<setlinefragmentrect(__forglyphrange_usedrect_).md>) — Associates the line fragment bounds for the specified range of glyphs.
- [- setNotShownAttribute:forGlyphAtIndex:](<setnotshownattribute(__forglyphat_).md>) — Sets the visibility of the glyph at the specified index.

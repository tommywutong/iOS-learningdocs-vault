---
title: 'setDrawsOutsideLineFragment(_:forGlyphAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/setdrawsoutsidelinefragment(_:forglyphat:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/setdrawsoutsidelinefragment(_:forglyphat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/setdrawsoutsidelinefragment%28_%3Aforglyphat%3A%29.json'
content_hash: 'sha256:deaa2a77d745a252'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# setDrawsOutsideLineFragment(_:forGlyphAt:)

<sub>Instance Method</sub>

Indicates whether the specified glyph exceeds the bounds of the line fragment for its layout.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setDrawsOutsideLineFragment(_ flag: Bool, forGlyphAt glyphIndex: Int)
```

## Parameters

- `flag` — If [true](../../swift/true.md), sets the given glyph to draw outside its line fragment; if [false](../../swift/false.md), the glyph does not draw outside.

- `glyphIndex` — Index of the glyph to set.

## Discussion

This can happen when text is set at a fixed line height. For example, if the user specifies a fixed line height of 12 points and sets the font size to 24 points, the glyphs will exceed their layout rectangles. This information is important for determining whether additional lines need to be redrawn as a result of changes to any given line fragment.

This method is used by the layout mechanism and should be invoked only during typesetting, in almost all cases only by the typesetter. For example, a custom typesetter might invoke it.

## See Also

### Related Documentation

- [- drawsOutsideLineFragmentForGlyphAtIndex:](<drawsoutsidelinefragment(forglyphat_).md>) — Indicates whether the glyph draws outside its line fragment rectangle.

### Setting layout information

- [- setAttachmentSize:forGlyphRange:](<setattachmentsize(__forglyphrange_).md>) — Sets the size to use when drawing a glyph that represents an attachment.
- [- setExtraLineFragmentRect:usedRect:textContainer:](<setextralinefragmentrect(__usedrect_textcontainer_).md>) — Sets the bounds and container for the extra line fragment.
- [- setLineFragmentRect:forGlyphRange:usedRect:](<setlinefragmentrect(__forglyphrange_usedrect_).md>) — Associates the line fragment bounds for the specified range of glyphs.
- [- setLocation:forStartOfGlyphRange:](<setlocation(__forstartofglyphrange_).md>) — Sets the location for the first glyph in the specified range.
- [- setNotShownAttribute:forGlyphAtIndex:](<setnotshownattribute(__forglyphat_).md>) — Sets the visibility of the glyph at the specified index.

---
title: 'setExtraLineFragmentRect(_:usedRect:textContainer:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/setextralinefragmentrect(_:usedrect:textcontainer:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/setextralinefragmentrect(_:usedrect:textcontainer:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/setextralinefragmentrect%28_%3Ausedrect%3Atextcontainer%3A%29.json'
content_hash: 'sha256:65c6fd04eb5e604e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# setExtraLineFragmentRect(_:usedRect:textContainer:)

<sub>Instance Method</sub>

Sets the bounds and container for the extra line fragment.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setExtraLineFragmentRect(_ fragmentRect: CGRect, usedRect: CGRect, textContainer container: NSTextContainer)
```

## Parameters

- `fragmentRect` — The rectangle to set.

- `usedRect` — Indicates where the insertion point is drawn.

- `container` — The text container where the rectangle is to be laid out.

## Discussion

The extra line fragment is used when the text backing ends with a hard line break or when the text backing is totally empty, to define the extra line which needs to be displayed at the end of the text. If the text backing is not empty and does not end with a hard line break, this should be set to [NSZeroRect](../../foundation/nszerorect.md) and `nil`.

Line fragment rectangles and line fragment used rectangles are always in container coordinates.

This method is used by the layout mechanism and should be invoked only during typesetting, in almost all cases only by the typesetter. For example, a custom typesetter might invoke it.

## See Also

### Setting layout information

- [- setAttachmentSize:forGlyphRange:](<setattachmentsize(__forglyphrange_).md>) — Sets the size to use when drawing a glyph that represents an attachment.
- [- setDrawsOutsideLineFragment:forGlyphAtIndex:](<setdrawsoutsidelinefragment(__forglyphat_).md>) — Indicates whether the specified glyph exceeds the bounds of the line fragment for its layout.
- [- setLineFragmentRect:forGlyphRange:usedRect:](<setlinefragmentrect(__forglyphrange_usedrect_).md>) — Associates the line fragment bounds for the specified range of glyphs.
- [- setLocation:forStartOfGlyphRange:](<setlocation(__forstartofglyphrange_).md>) — Sets the location for the first glyph in the specified range.
- [- setNotShownAttribute:forGlyphAtIndex:](<setnotshownattribute(__forglyphat_).md>) — Sets the visibility of the glyph at the specified index.

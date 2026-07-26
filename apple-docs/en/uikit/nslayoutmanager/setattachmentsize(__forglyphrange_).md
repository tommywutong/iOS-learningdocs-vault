---
title: 'setAttachmentSize(_:forGlyphRange:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/setattachmentsize(_:forglyphrange:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/setattachmentsize(_:forglyphrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/setattachmentsize%28_%3Aforglyphrange%3A%29.json'
content_hash: 'sha256:e0f4098ec0c1ad4d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# setAttachmentSize(_:forGlyphRange:)

<sub>Instance Method</sub>

Sets the size to use when drawing a glyph that represents an attachment.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setAttachmentSize(_ attachmentSize: CGSize, forGlyphRange glyphRange: NSRange)
```

## Parameters

- `attachmentSize` — The glyph size to set.

- `glyphRange` — The attachment glyph’s position in the glyph stream.

## Discussion

For a glyph corresponding to an attachment, this method should be called to set the size for the attachment cell to occupy. The glyph’s value should be [NSControlGlyph](../../appkit/nscontrolglyph.md).

This method is used by the layout mechanism and should be invoked only during typesetting, in almost all cases only by the typesetter. For example, a custom typesetter might invoke it.

## See Also

### Related Documentation

- [- attachmentSizeForGlyphAtIndex:](<attachmentsize(forglyphat_).md>) — Returns the size of the attachment glyph at the specified index.
- [defaultAttachmentScaling](../../appkit/nslayoutmanager/defaultattachmentscaling.md) — The default amount of scaling to apply when an attachment image is too large to fit in a text container.

### Setting layout information

- [- setDrawsOutsideLineFragment:forGlyphAtIndex:](<setdrawsoutsidelinefragment(__forglyphat_).md>) — Indicates whether the specified glyph exceeds the bounds of the line fragment for its layout.
- [- setExtraLineFragmentRect:usedRect:textContainer:](<setextralinefragmentrect(__usedrect_textcontainer_).md>) — Sets the bounds and container for the extra line fragment.
- [- setLineFragmentRect:forGlyphRange:usedRect:](<setlinefragmentrect(__forglyphrange_usedrect_).md>) — Associates the line fragment bounds for the specified range of glyphs.
- [- setLocation:forStartOfGlyphRange:](<setlocation(__forstartofglyphrange_).md>) — Sets the location for the first glyph in the specified range.
- [- setNotShownAttribute:forGlyphAtIndex:](<setnotshownattribute(__forglyphat_).md>) — Sets the visibility of the glyph at the specified index.

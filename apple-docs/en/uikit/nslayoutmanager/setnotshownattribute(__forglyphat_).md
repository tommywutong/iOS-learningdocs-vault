---
title: 'setNotShownAttribute(_:forGlyphAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/setnotshownattribute(_:forglyphat:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/setnotshownattribute(_:forglyphat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/setnotshownattribute%28_%3Aforglyphat%3A%29.json'
content_hash: 'sha256:b06f1ab5e017105a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# setNotShownAttribute(_:forGlyphAt:)

<sub>Instance Method</sub>

Sets the visibility of the glyph at the specified index.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setNotShownAttribute(_ flag: Bool, forGlyphAt glyphIndex: Int)
```

## Parameters

- `flag` — If [true](../../swift/true.md), the glyph is not shown; if [false](../../swift/false.md), it is shown.

- `glyphIndex` — Index of the glyph whose attribute is set.

## Discussion

The typesetter decides which glyphs are not shown and sets this attribute in the layout manager to ensure that those glyphs are not displayed. For example, a tab or newline character doesn’t leave any marks; it just indicates where following glyphs are laid out.

Raises an `NSRangeException` if `glyphIndex` is out of bounds.

This method is used by the layout mechanism and should be invoked only during typesetting, in almost all cases only by the typesetter. For example, a custom typesetter might invoke it.

## See Also

### Related Documentation

- [- notShownAttributeForGlyphAtIndex:](<notshownattribute(forglyphat_).md>) — Indicates whether the glyph at the specified index has a visible representation.

### Setting layout information

- [- setAttachmentSize:forGlyphRange:](<setattachmentsize(__forglyphrange_).md>) — Sets the size to use when drawing a glyph that represents an attachment.
- [- setDrawsOutsideLineFragment:forGlyphAtIndex:](<setdrawsoutsidelinefragment(__forglyphat_).md>) — Indicates whether the specified glyph exceeds the bounds of the line fragment for its layout.
- [- setExtraLineFragmentRect:usedRect:textContainer:](<setextralinefragmentrect(__usedrect_textcontainer_).md>) — Sets the bounds and container for the extra line fragment.
- [- setLineFragmentRect:forGlyphRange:usedRect:](<setlinefragmentrect(__forglyphrange_usedrect_).md>) — Associates the line fragment bounds for the specified range of glyphs.
- [- setLocation:forStartOfGlyphRange:](<setlocation(__forstartofglyphrange_).md>) — Sets the location for the first glyph in the specified range.

---
title: 'textContainer(forGlyphAt:effectiveRange:withoutAdditionalLayout:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/textcontainer(forglyphat:effectiverange:withoutadditionallayout:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/textcontainer(forglyphat:effectiverange:withoutadditionallayout:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/textcontainer%28forglyphat%3Aeffectiverange%3Awithoutadditionallayout%3A%29.json'
content_hash: 'sha256:d4e3a7c91271e9e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# textContainer(forGlyphAt:effectiveRange:withoutAdditionalLayout:)

<sub>Instance Method</sub>

Returns the text container that manages the layout for the specified glyph.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func textContainer(forGlyphAt glyphIndex: Int, effectiveRange effectiveGlyphRange: NSRangePointer?, withoutAdditionalLayout flag: Bool) -> NSTextContainer?
```

## Parameters

- `glyphIndex` — Index of a glyph in the returned container.

- `effectiveGlyphRange` — If not `NULL`, on output, points to the whole range of glyphs that are in the returned container.

- `flag` — If [true](../../swift/true.md), glyph generation and layout are not performed, so this option should not be used unless layout is known to be complete for the range in question, or unless noncontiguous layout is enabled; if [false](../../swift/false.md), both are performed as needed.

## Return Value

The text container in which the glyph at `glyphIndex` is laid out.

## Discussion

This method is primarily for use from within `NSTypesetter`, after layout is complete for the range in question, but before the layout manager’s call to `NSTypesetter` has returned. In that case glyph and layout holes have not yet been recalculated, so the layout manager does not yet know that layout is complete for that range, and this variant must be used.

Overriding this method is not recommended. Any changes to the returned glyph range should be done at the typesetter level.

## See Also

### Managing the text containers

- [textContainers](textcontainers.md) — The current text containers of the layout manager.
- [- addTextContainer:](<addtextcontainer(__).md>) — Appends the specified text container to the series of text containers where the layout manager arranges text.
- [- insertTextContainer:atIndex:](<inserttextcontainer(__at_).md>) — Inserts a text container at the specified index in the list of text containers.
- [- removeTextContainerAtIndex:](<removetextcontainer(at_).md>) — Removes the text container at the specified index and invalidates the layout as necessary.
- [- setTextContainer:forGlyphRange:](<settextcontainer(__forglyphrange_).md>) — Associates a text container with the specified range of glyphs.
- [- textContainerChangedGeometry:](<textcontainerchangedgeometry(__).md>) — Invalidates the layout information, and possibly glyphs, for the specified text container and all subsequent text container objects.
- [textContainerChangedTextView(_:)](<../../appkit/nslayoutmanager/textcontainerchangedtextview(__).md>) — Updates the information necessary to manage text view objects for the specified text container.
- [- textContainerForGlyphAtIndex:effectiveRange:](<textcontainer(forglyphat_effectiverange_).md>) — Returns the text container that manages the layout for the specified glyph, causing layout to happen as necessary.
- [- usedRectForTextContainer:](<usedrect(for_).md>) — Returns the bounding rectangle for the glyphs in the specified text container.

---
title: 'textContainer(forGlyphAt:effectiveRange:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/textcontainer(forglyphat:effectiverange:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/textcontainer(forglyphat:effectiverange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/textcontainer%28forglyphat%3Aeffectiverange%3A%29.json'
content_hash: 'sha256:91a1bf78efef73f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# textContainer(forGlyphAt:effectiveRange:)

<sub>Instance Method</sub>

Returns the text container that manages the layout for the specified glyph, causing layout to happen as necessary.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func textContainer(forGlyphAt glyphIndex: Int, effectiveRange effectiveGlyphRange: NSRangePointer?) -> NSTextContainer?
```

## Parameters

- `glyphIndex` — Index of a glyph in the returned container.

- `effectiveGlyphRange` — If not `NULL`, on output, points to the whole range of glyphs that are in the returned container.

## Return Value

The text container in which the glyph at `glyphIndex` is laid out.

## Discussion

This method causes glyph generation and layout for the line fragment containing the specified glyph, or if noncontiguous layout is not enabled, up to and including that line fragment. If noncontiguous layout is not enabled and `effectiveGlyphRange` is not `NULL`, this method additionally causes glyph generation and layout for the entire text container containing the specified glyph.

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
- [- textContainerForGlyphAtIndex:effectiveRange:withoutAdditionalLayout:](<textcontainer(forglyphat_effectiverange_withoutadditionallayout_).md>) — Returns the text container that manages the layout for the specified glyph.
- [- usedRectForTextContainer:](<usedrect(for_).md>) — Returns the bounding rectangle for the glyphs in the specified text container.

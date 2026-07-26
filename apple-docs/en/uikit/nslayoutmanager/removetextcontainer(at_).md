---
title: 'removeTextContainer(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/removetextcontainer(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/removetextcontainer(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/removetextcontainer%28at%3A%29.json'
content_hash: 'sha256:1999377c811839aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# removeTextContainer(at:)

<sub>Instance Method</sub>

Removes the text container at the specified index and invalidates the layout as necessary.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func removeTextContainer(at index: Int)
```

## Parameters

- `index` — The index of the text container to remove.

## Discussion

This method invalidates glyph information as needed.

## See Also

### Related Documentation

- [- invalidateGlyphsForCharacterRange:changeInLength:actualCharacterRange:](<invalidateglyphs(forcharacterrange_changeinlength_actualcharacterrange_).md>) — Invalidates and adjusts the glyphs in the specified character range.
- [- invalidateLayoutForCharacterRange:actualCharacterRange:](<invalidatelayout(forcharacterrange_actualcharacterrange_).md>) — Invalidates the layout information for the glyphs that map to the specified character range.

### Managing the text containers

- [textContainers](textcontainers.md) — The current text containers of the layout manager.
- [- addTextContainer:](<addtextcontainer(__).md>) — Appends the specified text container to the series of text containers where the layout manager arranges text.
- [- insertTextContainer:atIndex:](<inserttextcontainer(__at_).md>) — Inserts a text container at the specified index in the list of text containers.
- [- setTextContainer:forGlyphRange:](<settextcontainer(__forglyphrange_).md>) — Associates a text container with the specified range of glyphs.
- [- textContainerChangedGeometry:](<textcontainerchangedgeometry(__).md>) — Invalidates the layout information, and possibly glyphs, for the specified text container and all subsequent text container objects.
- [textContainerChangedTextView(_:)](<../../appkit/nslayoutmanager/textcontainerchangedtextview(__).md>) — Updates the information necessary to manage text view objects for the specified text container.
- [- textContainerForGlyphAtIndex:effectiveRange:](<textcontainer(forglyphat_effectiverange_).md>) — Returns the text container that manages the layout for the specified glyph, causing layout to happen as necessary.
- [- textContainerForGlyphAtIndex:effectiveRange:withoutAdditionalLayout:](<textcontainer(forglyphat_effectiverange_withoutadditionallayout_).md>) — Returns the text container that manages the layout for the specified glyph.
- [- usedRectForTextContainer:](<usedrect(for_).md>) — Returns the bounding rectangle for the glyphs in the specified text container.

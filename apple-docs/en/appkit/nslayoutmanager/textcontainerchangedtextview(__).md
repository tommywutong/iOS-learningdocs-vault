---
title: 'textContainerChangedTextView(_:)'
framework: AppKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/appkit/nslayoutmanager/textcontainerchangedtextview(_:)'
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutmanager/textcontainerchangedtextview(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutmanager/textcontainerchangedtextview%28_%3A%29.json'
content_hash: 'sha256:b24bdd8c4a4c3d08'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutManager](../nslayoutmanager.md)

# textContainerChangedTextView(_:)

<sub>Instance Method</sub>

Updates the information necessary to manage text view objects for the specified text container.

<sub>macOS</sub>

```swift
func textContainerChangedTextView(_ container: NSTextContainer)
```

## Parameters

- `container` — The text container whose text view has changed.

## Discussion

This method is called by a text container, whenever its text view changes, to keep notifications synchronized. You should rarely need to invoke it directly.

## See Also

### Managing the text containers

- [textContainers](textcontainers.md) — The current text containers of the layout manager.
- [- addTextContainer:](<addtextcontainer(__).md>) — Appends the specified text container to the series of text containers where the layout manager arranges text.
- [- insertTextContainer:atIndex:](<inserttextcontainer(__at_).md>) — Inserts a text container at the specified index in the list of text containers.
- [- removeTextContainerAtIndex:](<removetextcontainer(at_).md>) — Removes the text container at the specified index and invalidates the layout as necessary.
- [- setTextContainer:forGlyphRange:](<settextcontainer(__forglyphrange_).md>) — Associates a text container with the specified range of glyphs.
- [- textContainerChangedGeometry:](<textcontainerchangedgeometry(__).md>) — Invalidates the layout information, and possibly glyphs, for the specified text container and all subsequent text container objects.
- [- textContainerForGlyphAtIndex:effectiveRange:](<textcontainer(forglyphat_effectiverange_).md>) — Returns the text container that manages the layout for the specified glyph, causing layout to happen as necessary.
- [- textContainerForGlyphAtIndex:effectiveRange:withoutAdditionalLayout:](<textcontainer(forglyphat_effectiverange_withoutadditionallayout_).md>) — Returns the text container that manages the layout for the specified glyph.
- [- usedRectForTextContainer:](<usedrect(for_).md>) — Returns the bounding rectangle for the glyphs in the specified text container.

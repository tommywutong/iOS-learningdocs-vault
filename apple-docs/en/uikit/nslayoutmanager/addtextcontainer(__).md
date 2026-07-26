---
title: 'addTextContainer(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/addtextcontainer(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/addtextcontainer(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/addtextcontainer%28_%3A%29.json'
content_hash: 'sha256:b7c36ac0d8fee40d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# addTextContainer(_:)

<sub>Instance Method</sub>

Appends the specified text container to the series of text containers where the layout manager arranges text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func addTextContainer(_ container: NSTextContainer)
```

## Parameters

- `container` — The text container to append.

## Discussion

Invalidates glyphs and layout as needed, but doesn’t perform glyph generation or layout.

## See Also

### Managing the text containers

- [textContainers](textcontainers.md) — The current text containers of the layout manager.
- [- insertTextContainer:atIndex:](<inserttextcontainer(__at_).md>) — Inserts a text container at the specified index in the list of text containers.
- [- removeTextContainerAtIndex:](<removetextcontainer(at_).md>) — Removes the text container at the specified index and invalidates the layout as necessary.
- [- setTextContainer:forGlyphRange:](<settextcontainer(__forglyphrange_).md>) — Associates a text container with the specified range of glyphs.
- [- textContainerChangedGeometry:](<textcontainerchangedgeometry(__).md>) — Invalidates the layout information, and possibly glyphs, for the specified text container and all subsequent text container objects.
- [textContainerChangedTextView(_:)](<../../appkit/nslayoutmanager/textcontainerchangedtextview(__).md>) — Updates the information necessary to manage text view objects for the specified text container.
- [- textContainerForGlyphAtIndex:effectiveRange:](<textcontainer(forglyphat_effectiverange_).md>) — Returns the text container that manages the layout for the specified glyph, causing layout to happen as necessary.
- [- textContainerForGlyphAtIndex:effectiveRange:withoutAdditionalLayout:](<textcontainer(forglyphat_effectiverange_withoutadditionallayout_).md>) — Returns the text container that manages the layout for the specified glyph.
- [- usedRectForTextContainer:](<usedrect(for_).md>) — Returns the bounding rectangle for the glyphs in the specified text container.

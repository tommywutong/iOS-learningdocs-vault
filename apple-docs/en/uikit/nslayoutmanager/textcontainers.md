---
title: textContainers
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nslayoutmanager/textcontainers
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/textcontainers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/textcontainers.json'
content_hash: 'sha256:b2230835e32eeaae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# textContainers

<sub>Instance Property</sub>

The current text containers of the layout manager.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var textContainers: [NSTextContainer] { get }
```

## See Also

### Managing the text containers

- [- addTextContainer:](<addtextcontainer(__).md>) — Appends the specified text container to the series of text containers where the layout manager arranges text.
- [- insertTextContainer:atIndex:](<inserttextcontainer(__at_).md>) — Inserts a text container at the specified index in the list of text containers.
- [- removeTextContainerAtIndex:](<removetextcontainer(at_).md>) — Removes the text container at the specified index and invalidates the layout as necessary.
- [- setTextContainer:forGlyphRange:](<settextcontainer(__forglyphrange_).md>) — Associates a text container with the specified range of glyphs.
- [- textContainerChangedGeometry:](<textcontainerchangedgeometry(__).md>) — Invalidates the layout information, and possibly glyphs, for the specified text container and all subsequent text container objects.
- [textContainerChangedTextView(_:)](<../../appkit/nslayoutmanager/textcontainerchangedtextview(__).md>) — Updates the information necessary to manage text view objects for the specified text container.
- [- textContainerForGlyphAtIndex:effectiveRange:](<textcontainer(forglyphat_effectiverange_).md>) — Returns the text container that manages the layout for the specified glyph, causing layout to happen as necessary.
- [- textContainerForGlyphAtIndex:effectiveRange:withoutAdditionalLayout:](<textcontainer(forglyphat_effectiverange_withoutadditionallayout_).md>) — Returns the text container that manages the layout for the specified glyph.
- [- usedRectForTextContainer:](<usedrect(for_).md>) — Returns the bounding rectangle for the glyphs in the specified text container.

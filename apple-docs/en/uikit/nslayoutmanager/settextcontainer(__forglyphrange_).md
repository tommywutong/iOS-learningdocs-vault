---
title: 'setTextContainer(_:forGlyphRange:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/settextcontainer(_:forglyphrange:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/settextcontainer(_:forglyphrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/settextcontainer%28_%3Aforglyphrange%3A%29.json'
content_hash: 'sha256:562863c2840e658f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# setTextContainer(_:forGlyphRange:)

<sub>Instance Method</sub>

Associates a text container with the specified range of glyphs.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setTextContainer(_ container: NSTextContainer, forGlyphRange glyphRange: NSRange)
```

## Parameters

- `container` — The text container to set.

- `glyphRange` — The range of glyphs to lay out.

## Discussion

The layout within the container is specified with the [- setLineFragmentRect:forGlyphRange:usedRect:](<setlinefragmentrect(__forglyphrange_usedrect_).md>) and [- setLocation:forStartOfGlyphRange:](<setlocation(__forstartofglyphrange_).md>) methods.

This method is used by the layout mechanism and should be invoked only during typesetting, in almost all cases only by the typesetter. For example, a custom typesetter might invoke it.

## See Also

### Managing the text containers

- [textContainers](textcontainers.md) — The current text containers of the layout manager.
- [- addTextContainer:](<addtextcontainer(__).md>) — Appends the specified text container to the series of text containers where the layout manager arranges text.
- [- insertTextContainer:atIndex:](<inserttextcontainer(__at_).md>) — Inserts a text container at the specified index in the list of text containers.
- [- removeTextContainerAtIndex:](<removetextcontainer(at_).md>) — Removes the text container at the specified index and invalidates the layout as necessary.
- [- textContainerChangedGeometry:](<textcontainerchangedgeometry(__).md>) — Invalidates the layout information, and possibly glyphs, for the specified text container and all subsequent text container objects.
- [textContainerChangedTextView(_:)](<../../appkit/nslayoutmanager/textcontainerchangedtextview(__).md>) — Updates the information necessary to manage text view objects for the specified text container.
- [- textContainerForGlyphAtIndex:effectiveRange:](<textcontainer(forglyphat_effectiverange_).md>) — Returns the text container that manages the layout for the specified glyph, causing layout to happen as necessary.
- [- textContainerForGlyphAtIndex:effectiveRange:withoutAdditionalLayout:](<textcontainer(forglyphat_effectiverange_withoutadditionallayout_).md>) — Returns the text container that manages the layout for the specified glyph.
- [- usedRectForTextContainer:](<usedrect(for_).md>) — Returns the bounding rectangle for the glyphs in the specified text container.

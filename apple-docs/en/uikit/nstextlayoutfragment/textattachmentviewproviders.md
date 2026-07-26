---
title: textAttachmentViewProviders
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextlayoutfragment/textattachmentviewproviders
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutfragment/textattachmentviewproviders'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutfragment/textattachmentviewproviders.json'
content_hash: 'sha256:8c21e193fcc6aa4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutFragment](../nstextlayoutfragment.md)

# textAttachmentViewProviders

<sub>Instance Property</sub>

The attachment view provider associated with the text layout fragment.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var textAttachmentViewProviders: [NSTextAttachmentViewProvider] { get }
```

## Discussion

The property contents are only valid with [NSTextLayoutFragmentStateLayoutAvailable](state-swift.enum/layoutavailable.md).

## See Also

### Drawing the fragment and attachments

- [layoutFragmentFrame](layoutfragmentframe.md) — The rectangle the framework uses for tiling the layout fragment inside the target layout coordinate system.
- [renderingSurfaceBounds](renderingsurfacebounds.md) — The bounds defining the area required for rendering the contents.
- [- drawAtPoint:inContext:](<draw(at_in_).md>) — Renders the visual representation of this element in the specified graphics context.
- [- invalidateLayout](<invalidatelayout().md>) — Invalidates any layout information associated with the text layout fragment.
- [- frameForTextAttachmentAtLocation:](<framefortextattachment(at_).md>) — Returns the frame in the text layout fragment coordinate system for the attachment at the location you specify.

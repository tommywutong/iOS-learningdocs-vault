---
title: invalidateLayout()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextlayoutfragment/invalidatelayout()
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutfragment/invalidatelayout()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutfragment/invalidatelayout%28%29.json'
content_hash: 'sha256:7641fa446eee7fe9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutFragment](../nstextlayoutfragment.md)

# invalidateLayout()

<sub>Instance Method</sub>

Invalidates any layout information associated with the text layout fragment.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func invalidateLayout()
```

## See Also

### Drawing the fragment and attachments

- [layoutFragmentFrame](layoutfragmentframe.md) — The rectangle the framework uses for tiling the layout fragment inside the target layout coordinate system.
- [renderingSurfaceBounds](renderingsurfacebounds.md) — The bounds defining the area required for rendering the contents.
- [- drawAtPoint:inContext:](<draw(at_in_).md>) — Renders the visual representation of this element in the specified graphics context.
- [textAttachmentViewProviders](textattachmentviewproviders.md) — The attachment view provider associated with the text layout fragment.
- [- frameForTextAttachmentAtLocation:](<framefortextattachment(at_).md>) — Returns the frame in the text layout fragment coordinate system for the attachment at the location you specify.

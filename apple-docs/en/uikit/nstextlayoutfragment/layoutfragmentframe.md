---
title: layoutFragmentFrame
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextlayoutfragment/layoutfragmentframe
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutfragment/layoutfragmentframe'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutfragment/layoutfragmentframe.json'
content_hash: 'sha256:c3c2431958af2f1c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutFragment](../nstextlayoutfragment.md)

# layoutFragmentFrame

<sub>Instance Property</sub>

The rectangle the framework uses for tiling the layout fragment inside the target layout coordinate system.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var layoutFragmentFrame: CGRect { get }
```

## See Also

### Drawing the fragment and attachments

- [renderingSurfaceBounds](renderingsurfacebounds.md) — The bounds defining the area required for rendering the contents.
- [- drawAtPoint:inContext:](<draw(at_in_).md>) — Renders the visual representation of this element in the specified graphics context.
- [- invalidateLayout](<invalidatelayout().md>) — Invalidates any layout information associated with the text layout fragment.
- [textAttachmentViewProviders](textattachmentviewproviders.md) — The attachment view provider associated with the text layout fragment.
- [- frameForTextAttachmentAtLocation:](<framefortextattachment(at_).md>) — Returns the frame in the text layout fragment coordinate system for the attachment at the location you specify.

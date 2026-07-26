---
title: renderingSurfaceBounds
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextlayoutfragment/renderingsurfacebounds
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutfragment/renderingsurfacebounds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutfragment/renderingsurfacebounds.json'
content_hash: 'sha256:8adc899f52e67c4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutFragment](../nstextlayoutfragment.md)

# renderingSurfaceBounds

<sub>Instance Property</sub>

The bounds defining the area required for rendering the contents.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var renderingSurfaceBounds: CGRect { get }
```

## Discussion

The coordinate system is vertically flipped from the `layoutFragmentFrame` origin ({`0`,`0`} is at the upper-left corner). The size should be larger than `layoutFragmentFrame.size`. The origin could be in the negative coordinate since the rendering could stretch out of `layoutFragmentFrame`. Only valid when `state` greater than [NSTextLayoutFragmentStateEstimatedUsageBounds](state-swift.enum/estimatedusagebounds.md).

## See Also

### Drawing the fragment and attachments

- [layoutFragmentFrame](layoutfragmentframe.md) — The rectangle the framework uses for tiling the layout fragment inside the target layout coordinate system.
- [- drawAtPoint:inContext:](<draw(at_in_).md>) — Renders the visual representation of this element in the specified graphics context.
- [- invalidateLayout](<invalidatelayout().md>) — Invalidates any layout information associated with the text layout fragment.
- [textAttachmentViewProviders](textattachmentviewproviders.md) — The attachment view provider associated with the text layout fragment.
- [- frameForTextAttachmentAtLocation:](<framefortextattachment(at_).md>) — Returns the frame in the text layout fragment coordinate system for the attachment at the location you specify.

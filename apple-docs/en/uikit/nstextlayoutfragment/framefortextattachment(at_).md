---
title: 'frameForTextAttachment(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextlayoutfragment/framefortextattachment(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutfragment/framefortextattachment(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutfragment/framefortextattachment%28at%3A%29.json'
content_hash: 'sha256:702d8703c6027748'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutFragment](../nstextlayoutfragment.md)

# frameForTextAttachment(at:)

<sub>Instance Method</sub>

Returns the frame in the text layout fragment coordinate system for the attachment at the location you specify.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func frameForTextAttachment(at location: any NSTextLocation) -> CGRect
```

## Parameters

- `location` — The [NSTextLocation](../nstextlocation.md) that describes the location in the text layout fragment.

## Return Value

The frame rectangle that describes the text layout fragment.

## Discussion

Returns [CGRectZero](../../coregraphics/cgrectzero.md) if `location` isn’t with any attachment or the state isn’t [NSTextLayoutFragmentStateLayoutAvailable](state-swift.enum/layoutavailable.md).

## See Also

### Drawing the fragment and attachments

- [layoutFragmentFrame](layoutfragmentframe.md) — The rectangle the framework uses for tiling the layout fragment inside the target layout coordinate system.
- [renderingSurfaceBounds](renderingsurfacebounds.md) — The bounds defining the area required for rendering the contents.
- [- drawAtPoint:inContext:](<draw(at_in_).md>) — Renders the visual representation of this element in the specified graphics context.
- [- invalidateLayout](<invalidatelayout().md>) — Invalidates any layout information associated with the text layout fragment.
- [textAttachmentViewProviders](textattachmentviewproviders.md) — The attachment view provider associated with the text layout fragment.

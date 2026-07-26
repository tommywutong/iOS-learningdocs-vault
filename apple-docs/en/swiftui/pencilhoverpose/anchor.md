---
title: anchor
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.5+, iPadOS 17.5+, Mac Catalyst 17.5+, macOS 14.5+, visionOS 26.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/pencilhoverpose/anchor
source_url: 'https://developer.apple.com/documentation/swiftui/pencilhoverpose/anchor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/pencilhoverpose/anchor.json'
content_hash: 'sha256:1c2c34f042977b76'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PencilHoverPose](../pencilhoverpose.md)

# anchor

<sub>Instance Property</sub>

The location of an Apple Pencil hovering in the area above the view’s bounds, expressed as a normalized anchor point relative to that view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
let anchor: UnitPoint
```

## Discussion

You can pass this anchor point directly to a presentation modifier like [popover(isPresented:attachmentAnchor:arrowEdge:content:)](<../view/popover(ispresented_attachmentanchor_arrowedge_content_).md>) or use the [location](location.md) property if you require an absolute point instead.

## See Also

### Getting the hover characteristics

- [altitude](altitude.md) — A value that represents the altitude angle of the hovering Apple Pencil.
- [azimuth](azimuth.md) — A value that represents the azimuth angle of a hovering Apple Pencil.
- [location](location.md) — The location of an Apple Pencil hovering in the area above the view’s bounds, expressed as a point in that view’s coordinate space.
- [roll](roll.md) — A value that represents the barrel roll angle of the hovering Apple Pencil.
- [zDistance](zdistance.md) — The normalized distance between the screen and a hovering Apple Pencil.

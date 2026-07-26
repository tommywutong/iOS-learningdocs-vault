---
title: zDistance
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.5+, iPadOS 17.5+, Mac Catalyst 17.5+, macOS 14.5+, visionOS 26.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/pencilhoverpose/zdistance
source_url: 'https://developer.apple.com/documentation/swiftui/pencilhoverpose/zdistance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/pencilhoverpose/zdistance.json'
content_hash: 'sha256:40deb4f9a6f3ed9c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PencilHoverPose](../pencilhoverpose.md)

# zDistance

<sub>Instance Property</sub>

The normalized distance between the screen and a hovering Apple Pencil.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
let zDistance: CGFloat
```

## Discussion

This value is `1` at the maximum distance from the screen and approaches `0` as the Apple Pencil gets closer to the screen.

## See Also

### Getting the hover characteristics

- [altitude](altitude.md) — A value that represents the altitude angle of the hovering Apple Pencil.
- [anchor](anchor.md) — The location of an Apple Pencil hovering in the area above the view’s bounds, expressed as a normalized anchor point relative to that view.
- [azimuth](azimuth.md) — A value that represents the azimuth angle of a hovering Apple Pencil.
- [location](location.md) — The location of an Apple Pencil hovering in the area above the view’s bounds, expressed as a point in that view’s coordinate space.
- [roll](roll.md) — A value that represents the barrel roll angle of the hovering Apple Pencil.

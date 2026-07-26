---
title: location
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.5+, iPadOS 17.5+, Mac Catalyst 17.5+, macOS 14.5+, visionOS 26.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/pencilhoverpose/location
source_url: 'https://developer.apple.com/documentation/swiftui/pencilhoverpose/location'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/pencilhoverpose/location.json'
content_hash: 'sha256:67374e9c717cfc0e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PencilHoverPose](../pencilhoverpose.md)

# location

<sub>Instance Property</sub>

The location of an Apple Pencil hovering in the area above the view’s bounds, expressed as a point in that view’s coordinate space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
let location: CGPoint
```

## Discussion

Use the [anchor](anchor.md) property if you require a normalized anchor point for use with a presentation modifier instead.

## See Also

### Getting the hover characteristics

- [altitude](altitude.md) — A value that represents the altitude angle of the hovering Apple Pencil.
- [anchor](anchor.md) — The location of an Apple Pencil hovering in the area above the view’s bounds, expressed as a normalized anchor point relative to that view.
- [azimuth](azimuth.md) — A value that represents the azimuth angle of a hovering Apple Pencil.
- [roll](roll.md) — A value that represents the barrel roll angle of the hovering Apple Pencil.
- [zDistance](zdistance.md) — The normalized distance between the screen and a hovering Apple Pencil.

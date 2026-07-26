---
title: roll
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.5+, iPadOS 17.5+, Mac Catalyst 17.5+, macOS 14.5+, visionOS 26.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/pencilhoverpose/roll
source_url: 'https://developer.apple.com/documentation/swiftui/pencilhoverpose/roll'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/pencilhoverpose/roll.json'
content_hash: 'sha256:f98f4e86ab4b1aa7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PencilHoverPose](../pencilhoverpose.md)

# roll

<sub>Instance Property</sub>

A value that represents the barrel roll angle of the hovering Apple Pencil.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
let roll: Angle
```

## Discussion

This value is `.zero` when the user starts using their Apple Pencil, and changes relative to that initial angle as the user rolls the Apple Pencil alongside its barrel. If the Apple Pencil doesn’t support detecting its barrel roll angle, this property is always `.zero`.

## See Also

### Getting the hover characteristics

- [altitude](altitude.md) — A value that represents the altitude angle of the hovering Apple Pencil.
- [anchor](anchor.md) — The location of an Apple Pencil hovering in the area above the view’s bounds, expressed as a normalized anchor point relative to that view.
- [azimuth](azimuth.md) — A value that represents the azimuth angle of a hovering Apple Pencil.
- [location](location.md) — The location of an Apple Pencil hovering in the area above the view’s bounds, expressed as a point in that view’s coordinate space.
- [zDistance](zdistance.md) — The normalized distance between the screen and a hovering Apple Pencil.

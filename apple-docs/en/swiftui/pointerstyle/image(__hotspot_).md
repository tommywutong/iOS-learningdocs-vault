---
title: 'image(_:hotSpot:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/pointerstyle/image(_:hotspot:)'
source_url: 'https://developer.apple.com/documentation/swiftui/pointerstyle/image(_:hotspot:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/pointerstyle/image%28_%3Ahotspot%3A%29.json'
content_hash: 'sha256:98c30d3d3763e70b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PointerStyle](../pointerstyle.md)

# image(_:hotSpot:)

<sub>Type Method</sub>

Initializes a pointer style with a given image and hot spot.

<sub>macOS</sub>

```swift
static func image(_ image: Image, hotSpot: UnitPoint) -> PointerStyle
```

## Parameters

- `image` — The pointer image.

- `hotSpot` — The point on the image that represents the location from which the pointer interaction occurs. For example, the hot spot of an arrow-shaped pointer is the tip of the arrow.

## Discussion

The hot spot is the part of the pointer that must be positioned over an onscreen element for clicking to have an effect.

For guidance on using a custom pointer, refer to [Pointing devices](../../design/human-interface-guidelines/pointing-devices.md) in the Human Interface Guidelines.

You may apply this pointer style to a single view or a view hierarchy using the [pointerStyle(_:)](<../view/pointerstyle(__).md>) modifier.

## See Also

### Creating custom pointer styles

- [shape(_:eoFill:size:)](<shape(__eofill_size_).md>) — Initializes a pointer style with a given shape.

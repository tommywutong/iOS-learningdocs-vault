---
title: 'shape(_:eoFill:size:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/pointerstyle/shape(_:eofill:size:)'
source_url: 'https://developer.apple.com/documentation/swiftui/pointerstyle/shape(_:eofill:size:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/pointerstyle/shape%28_%3Aeofill%3Asize%3A%29.json'
content_hash: 'sha256:50bb6401b3d691fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PointerStyle](../pointerstyle.md)

# shape(_:eoFill:size:)

<sub>Type Method</sub>

Initializes a pointer style with a given shape.

<sub>visionOS</sub>

```swift
static func shape(_ shape: some Shape, eoFill: Bool = false, size: CGSize) -> PointerStyle
```

## Parameters

- `shape` — The pointer shape.

- `eoFill` — A Boolean that indicates whether the shape is interpreted with the even-odd winding number rule.

- `size` — The size of the pointer shape.

## Discussion

For guidance on using a custom pointer, refer to [Pointing devices](../../design/human-interface-guidelines/pointing-devices.md) in the Human Interface Guidelines.

You may apply this pointer style to a single view or a view hierarchy using the [pointerStyle(_:)](<../view/pointerstyle(__).md>) modifier.

## See Also

### Creating custom pointer styles

- [image(_:hotSpot:)](<image(__hotspot_).md>) — Initializes a pointer style with a given image and hot spot.

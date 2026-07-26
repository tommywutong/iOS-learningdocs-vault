---
title: hoverPose
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.5+, iPadOS 17.5+, Mac Catalyst 17.5+, macOS 14.5+, visionOS 26.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/pencilsqueezegesturevalue/hoverpose
source_url: 'https://developer.apple.com/documentation/swiftui/pencilsqueezegesturevalue/hoverpose'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/pencilsqueezegesturevalue/hoverpose.json'
content_hash: 'sha256:0b482218e3447d5a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PencilSqueezeGestureValue](../pencilsqueezegesturevalue.md)

# hoverPose

<sub>Instance Property</sub>

The location and distance of an Apple Pencil hovering in the area above the view’s bounds when the squeeze gesture occurred.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
let hoverPose: PencilHoverPose?
```

## Discussion

If the Apple Pencil was hovering in the area above the view’s bounds when the user squeezed their Apple Pencil, this property describes its pose relative to that view.

Conversely, if the Apple Pencil wasn’t hovering in the area above the view’s bounds or if the device can’t detect a hovering Apple Pencil, this property is `nil`.

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
doc_path: /documentation/swiftui/pencildoubletapgesturevalue/hoverpose
source_url: 'https://developer.apple.com/documentation/swiftui/pencildoubletapgesturevalue/hoverpose'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/pencildoubletapgesturevalue/hoverpose.json'
content_hash: 'sha256:1d0150c3fa4097a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PencilDoubleTapGestureValue](../pencildoubletapgesturevalue.md)

# hoverPose

<sub>Instance Property</sub>

The location and distance of an Apple Pencil hovering in the area above the view’s bounds when the double-tap gesture occurred.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
let hoverPose: PencilHoverPose?
```

## Discussion

If the Apple Pencil was hovering in the area above the view’s bounds when the user double-tapped their Apple Pencil, this property describes its pose relative to that view.

Conversely, if the Apple Pencil wasn’t hovering in the area above the view’s bounds or if the device can’t detect a hovering Apple Pencil, this property is `nil`.

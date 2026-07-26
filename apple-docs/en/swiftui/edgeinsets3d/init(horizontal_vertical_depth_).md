---
title: 'init(horizontal:vertical:depth:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/edgeinsets3d/init(horizontal:vertical:depth:)'
source_url: 'https://developer.apple.com/documentation/swiftui/edgeinsets3d/init(horizontal:vertical:depth:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/edgeinsets3d/init%28horizontal%3Avertical%3Adepth%3A%29.json'
content_hash: 'sha256:988fd4362bdfe7ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EdgeInsets3D](../edgeinsets3d.md)

# init(horizontal:vertical:depth:)

<sub>Initializer</sub>

Creates an `EdgeInsets3D` value with values provided for each axis.

<sub>visionOS</sub>

```swift
@export(implementation) init(horizontal: CGFloat = 0, vertical: CGFloat = 0, depth: CGFloat = 0)
```

## Parameters

- `horizontal` — The insets to apply along the horizontal axis.

- `vertical` — The insets to apply along the vertical axis.

- `depth` — The insets to apply along the depth axis.

## See Also

### Creating an edge inset

- [init(top:leading:bottom:trailing:front:back:)](<init(top_leading_bottom_trailing_front_back_).md>) — Creates an `EdgeInsets3D` value with values provided for each face.

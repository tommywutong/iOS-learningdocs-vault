---
title: init()
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/unitpoint3d/init()
source_url: 'https://developer.apple.com/documentation/swiftui/unitpoint3d/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/unitpoint3d/init%28%29.json'
content_hash: 'sha256:a155c8c2fb31b54e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UnitPoint3D](../unitpoint3d.md)

# init()

<sub>Initializer</sub>

Creates a 3D unit point at the origin.

<sub>visionOS</sub>

```swift
init()
```

## Discussion

A view’s origin appears in the top-left-back corner in a left-to-right language environment, with positive x toward the right. It appears in the top-right-back corner in a right-to-left language, with positive x toward the left. Positive y is always toward the bottom of the view, and positive z points toward the front.

## See Also

### Creating a point

- [init(x:y:z:)](<init(x_y_z_).md>) — Creates a 3D unit point with the specified offsets.

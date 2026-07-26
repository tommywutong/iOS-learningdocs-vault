---
title: 'init(x:y:z:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/unitpoint3d/init(x:y:z:)'
source_url: 'https://developer.apple.com/documentation/swiftui/unitpoint3d/init(x:y:z:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/unitpoint3d/init%28x%3Ay%3Az%3A%29.json'
content_hash: 'sha256:2b8aff217a2df494'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UnitPoint3D](../unitpoint3d.md)

# init(x:y:z:)

<sub>Initializer</sub>

Creates a 3D unit point with the specified offsets.

<sub>visionOS</sub>

```swift
init(x: CGFloat, y: CGFloat, z: CGFloat)
```

## Parameters

- `x` — The normalized distance from the origin to the point in the horizontal dimension.

- `y` — The normalized distance from the origin to the point in the vertical dimension.

- `z` — The normalized distance from the origin to the point in the depth dimension.

## Discussion

Values outside the range `[0, 1]` project to points outside of a view.

## See Also

### Creating a point

- [init()](<init().md>) — Creates a 3D unit point at the origin.

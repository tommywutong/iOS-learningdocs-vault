---
title: 'offset(z:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/visualeffect/offset(z:)'
source_url: 'https://developer.apple.com/documentation/swiftui/visualeffect/offset(z:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/visualeffect/offset%28z%3A%29.json'
content_hash: 'sha256:9d2ef0e65e42699e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [VisualEffect](../visualeffect.md)

# offset(z:)

<sub>Instance Method</sub>

Brings a view forward in Z by the provided distance in points.

<sub>visionOS</sub>

```swift
@export(implementation) func offset(z: CGFloat) -> some VisualEffect

```

## Return Value

An effect that is extruded forward in Z by `distance`.

## See Also

### Translating

- [offset(_:)](<offset(__).md>) — Offsets the view by the horizontal and vertical amount specified in the offset parameter.
- [offset(x:y:)](<offset(x_y_).md>) — Offsets the view by the specified horizontal and vertical distances.

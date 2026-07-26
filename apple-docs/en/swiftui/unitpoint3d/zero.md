---
title: zero
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/unitpoint3d/zero
source_url: 'https://developer.apple.com/documentation/swiftui/unitpoint3d/zero'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/unitpoint3d/zero.json'
content_hash: 'sha256:d11e267cd3c4d882'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UnitPoint3D](../unitpoint3d.md)

# zero

<sub>Type Property</sub>

A 3D unit point with all components equal to zero.

<sub>visionOS</sub>

```swift
static let zero: UnitPoint3D
```

## Discussion

This point is equivalent to the [origin](origin.md). A view’s origin appears in the top-left-back corner in a left-to-right language environment, with positive x toward the right. It appears in the top-right-back corner in a right-to-left language, with positive x toward the left. Positive y is always toward the bottom of the view, and positive z points toward the front.

## See Also

### Getting the origin

- [origin](origin.md) — The origin of a view.

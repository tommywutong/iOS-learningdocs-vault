---
title: origin
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/unitpoint3d/origin
source_url: 'https://developer.apple.com/documentation/swiftui/unitpoint3d/origin'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/unitpoint3d/origin.json'
content_hash: 'sha256:a3476046e8c3715b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UnitPoint3D](../unitpoint3d.md)

# origin

<sub>Type Property</sub>

The origin of a view.

<sub>visionOS</sub>

```swift
static let origin: UnitPoint3D
```

## Discussion

A view’s origin appears in the top-left-back corner in a left-to-right language environment, with positive x toward the right. It appears in the top-right-back corner in a right-to-left language, with positive x toward the left. Positive y is always toward the bottom of the view, and positive z points toward the front.

## See Also

### Getting the origin

- [zero](zero.md) — A 3D unit point with all components equal to zero.

---
title: dynamic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/worldscalingbehavior/dynamic
source_url: 'https://developer.apple.com/documentation/swiftui/worldscalingbehavior/dynamic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/worldscalingbehavior/dynamic.json'
content_hash: 'sha256:6d112ffe3d6def77'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WorldScalingBehavior](../worldscalingbehavior.md)

# dynamic

<sub>Type Property</sub>

The window will scale up as it moves further away, maintaining the same angular size.

<sub>visionOS</sub>

```swift
static var dynamic: WorldScalingBehavior { get }
```

## Discussion

Prefer dynamic window scaling for windows that display dense UI or a lot of text. Using dynamic scaling ensures that controls and text remain at a comfortable size regardless of the window’s position.

For further information, see [Spatial layout](../../design/human-interface-guidelines/spatial-layout.md#Scale) in the Human Interface Guidelines.

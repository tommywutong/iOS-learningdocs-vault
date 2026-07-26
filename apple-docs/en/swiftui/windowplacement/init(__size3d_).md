---
title: 'init(_:size3D:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/windowplacement/init(_:size3d:)'
source_url: 'https://developer.apple.com/documentation/swiftui/windowplacement/init(_:size3d:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowplacement/init%28_%3Asize3d%3A%29.json'
content_hash: 'sha256:78a4c131dc62c27d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WindowPlacement](../windowplacement.md)

# init(_:size3D:)

<sub>Initializer</sub>

Creates a new window placement with an optional position and 3D size. Depth is ignored on scenes that don’t support it.

<sub>visionOS</sub>

```swift
init(_ position: WindowPlacement.Position? = nil, size3D: Size3D? = nil)
```

## Discussion

Any values not provided will use use the default values for the `Scene` that this placement is being applied to.

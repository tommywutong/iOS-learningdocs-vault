---
title: 'init(_:width:height:depth:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/windowplacement/init(_:width:height:depth:)'
source_url: 'https://developer.apple.com/documentation/swiftui/windowplacement/init(_:width:height:depth:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowplacement/init%28_%3Awidth%3Aheight%3Adepth%3A%29.json'
content_hash: 'sha256:0b821689ad25f943'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WindowPlacement](../windowplacement.md)

# init(_:width:height:depth:)

<sub>Initializer</sub>

Creates a new window placement with an optional position and 3D size. Depth is ignored on scenes or platforms that don’t support it.

<sub>visionOS</sub>

```swift
init(_ position: WindowPlacement.Position? = nil, width: CGFloat? = nil, height: CGFloat? = nil, depth: CGFloat? = nil)
```

## Discussion

Any values not provided will use use the default values for the `Scene` that this placement is being applied to.

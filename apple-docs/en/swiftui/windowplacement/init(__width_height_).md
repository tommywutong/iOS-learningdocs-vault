---
title: 'init(_:width:height:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/windowplacement/init(_:width:height:)'
source_url: 'https://developer.apple.com/documentation/swiftui/windowplacement/init(_:width:height:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowplacement/init%28_%3Awidth%3Aheight%3A%29.json'
content_hash: 'sha256:af308e70108700e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WindowPlacement](../windowplacement.md)

# init(_:width:height:)

<sub>Initializer</sub>

Creates a new window placement with a display-relative position, with an optional width and height.

<sub>macOS</sub>

```swift
init(_ position: UnitPoint, width: CGFloat? = nil, height: CGFloat? = nil)
```

## Discussion

Any values not provided will use use the default values for the `Scene` that this placement is being applied to.

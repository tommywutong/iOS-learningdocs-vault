---
title: 'init(x:y:width:height:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/windowplacement/init(x:y:width:height:)'
source_url: 'https://developer.apple.com/documentation/swiftui/windowplacement/init(x:y:width:height:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowplacement/init%28x%3Ay%3Awidth%3Aheight%3A%29.json'
content_hash: 'sha256:9ff8c7c6f84e93c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WindowPlacement](../windowplacement.md)

# init(x:y:width:height:)

<sub>Initializer</sub>

Creates a new window placement with an optional position and size.

<sub>macOS</sub>

```swift
init(x: CGFloat? = nil, y: CGFloat? = nil, width: CGFloat? = nil, height: CGFloat? = nil)
```

## Discussion

Any values not provided will use use the default values for the `Scene` that this placement is being applied to.

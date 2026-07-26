---
title: 'init(_:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/windowplacement/init(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/windowplacement/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowplacement/init%28_%3A%29.json'
content_hash: 'sha256:f274cecd71353f70'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WindowPlacement](../windowplacement.md)

# init(_:)

<sub>Initializer</sub>

Creates a new window placement with an optional position.

<sub>visionOS</sub>

```swift
init(_ position: WindowPlacement.Position? = nil)
```

## Discussion

Any values not provided will use use the default values for the `Scene` that this placement is being applied to.

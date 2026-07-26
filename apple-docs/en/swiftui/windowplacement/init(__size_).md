---
title: 'init(_:size:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/windowplacement/init(_:size:)'
source_url: 'https://developer.apple.com/documentation/swiftui/windowplacement/init(_:size:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowplacement/init%28_%3Asize%3A%29.json'
content_hash: 'sha256:73aa7611bb3a9c13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WindowPlacement](../windowplacement.md)

# init(_:size:)

<sub>Initializer</sub>

Creates a new window placement with an absolute position and optional size.

<sub>macOS</sub>

```swift
init(_ position: CGPoint? = nil, size: CGSize? = nil)
```

## Discussion

Any values not provided will use use the default values for the `Scene` that this placement is being applied to.

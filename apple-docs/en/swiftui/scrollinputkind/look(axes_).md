---
title: 'look(axes:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scrollinputkind/look(axes:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scrollinputkind/look(axes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollinputkind/look%28axes%3A%29.json'
content_hash: 'sha256:352898f58259dc66'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollInputKind](../scrollinputkind.md)

# look(axes:)

<sub>Type Method</sub>

On visionOS, by looking at the edge of a scroll view the content can automatically scroll. This contructor method takes a set of the scrollable axes.

<sub>visionOS</sub>

```swift
static func look(axes: Axis.Set) -> ScrollInputKind
```

## Discussion

This is an opt-in behavior.

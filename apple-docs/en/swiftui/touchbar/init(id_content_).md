---
title: 'init(id:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/touchbar/init(id:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/touchbar/init(id:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/touchbar/init%28id%3Acontent%3A%29.json'
content_hash: 'sha256:2407e8111fa97c3d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TouchBar](../touchbar.md)

# init(id:content:)

<sub>Initializer</sub>

Creates a customizable Touch Bar view container with a globally unique identifier.

<sub>macOS</sub>

```swift
init(id: String, @ContentBuilder content: () -> Content)
```

## Parameters

- `id` — A globally unique identifier for this Touch Bar.

- `content` — A collection of views to be displayed by the Touch Bar.

## Discussion

Be sure that each view in `content` has an explicit `touchBarItemPresence` value with customization identifier.

## See Also

### Creating a Touch Bar view

- [init(content:)](<init(content_).md>) — Creates a non-customizable Touch Bar view container.

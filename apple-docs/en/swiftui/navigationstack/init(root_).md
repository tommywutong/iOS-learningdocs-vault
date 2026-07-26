---
title: 'init(root:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/navigationstack/init(root:)'
source_url: 'https://developer.apple.com/documentation/swiftui/navigationstack/init(root:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/navigationstack/init%28root%3A%29.json'
content_hash: 'sha256:b4e5e08e10c052ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NavigationStack](../navigationstack.md)

# init(root:)

<sub>Initializer</sub>

Creates a navigation stack that manages its own navigation state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(@ContentBuilder root: () -> Root) where Data == NavigationPath
```

## Parameters

- `root` — The view to display when the stack is empty.

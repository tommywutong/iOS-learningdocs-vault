---
title: 'init(path:root:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/navigationstack/init(path:root:)'
source_url: 'https://developer.apple.com/documentation/swiftui/navigationstack/init(path:root:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/navigationstack/init%28path%3Aroot%3A%29.json'
content_hash: 'sha256:f5c6d77ec995ef81'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NavigationStack](../navigationstack.md)

# init(path:root:)

<sub>Initializer</sub>

Creates a navigation stack with homogeneous navigation state that you can control.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(path: Binding<Data>, @ContentBuilder root: () -> Root) where Data : MutableCollection, Data : RandomAccessCollection, Data : RangeReplaceableCollection, Data.Element : Hashable
```

## Parameters

- `path` — A [Binding](../binding.md) to the navigation state for this stack.

- `root` — The view to display when the stack is empty.

## Discussion

If you don’t need access to the navigation state, use [init(root:)](<init(root_).md>).

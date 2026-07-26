---
title: 'init(_:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/anycompositorcontent/init(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/anycompositorcontent/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/anycompositorcontent/init%28_%3A%29.json'
content_hash: 'sha256:1364c29310984e2b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AnyCompositorContent](../anycompositorcontent.md)

# init(_:)

<sub>Initializer</sub>

Create an instance that type-erases `CompositorContent`.

<sub>macOS, visionOS</sub>

```swift
nonisolated init<T>(_ content: T) where T : CompositorContent
```

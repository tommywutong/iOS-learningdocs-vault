---
title: 'init(for:makeContent:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/immersivespace/init(for:makecontent:)'
source_url: 'https://developer.apple.com/documentation/swiftui/immersivespace/init(for:makecontent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/immersivespace/init%28for%3Amakecontent%3A%29.json'
content_hash: 'sha256:fde623b92f134ba4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ImmersiveSpace](../immersivespace.md)

# init(for:makeContent:)

<sub>Initializer</sub>

<sub>visionOS</sub>

```swift
nonisolated init<C>(for type: Data.Type, @CompositorContentBuilder makeContent: @escaping (Binding<Data?>) -> C) where Content == CompositorContentBuilder.Content<C>, C : CompositorContent
```

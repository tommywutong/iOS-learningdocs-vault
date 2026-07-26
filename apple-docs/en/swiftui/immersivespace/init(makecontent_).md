---
title: 'init(makeContent:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/immersivespace/init(makecontent:)'
source_url: 'https://developer.apple.com/documentation/swiftui/immersivespace/init(makecontent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/immersivespace/init%28makecontent%3A%29.json'
content_hash: 'sha256:e51009b7ff9b4e83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ImmersiveSpace](../immersivespace.md)

# init(makeContent:)

<sub>Initializer</sub>

<sub>visionOS</sub>

```swift
nonisolated init<C>(@CompositorContentBuilder makeContent: @escaping () -> C) where Content == CompositorContentBuilder.Content<C>, Data == Never, C : CompositorContent
```

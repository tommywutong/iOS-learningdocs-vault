---
title: 'init(id:for:makeContent:defaultValue:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/immersivespace/init(id:for:makecontent:defaultvalue:)'
source_url: 'https://developer.apple.com/documentation/swiftui/immersivespace/init(id:for:makecontent:defaultvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/immersivespace/init%28id%3Afor%3Amakecontent%3Adefaultvalue%3A%29.json'
content_hash: 'sha256:be948c374b9e6ed1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ImmersiveSpace](../immersivespace.md)

# init(id:for:makeContent:defaultValue:)

<sub>Initializer</sub>

<sub>visionOS</sub>

```swift
nonisolated init<C>(id: String, for type: Data.Type = Data.self, @CompositorContentBuilder makeContent: @escaping (Binding<Data>) -> C, defaultValue: @escaping () -> Data) where Content == CompositorContentBuilder.Content<C>, C : CompositorContent
```

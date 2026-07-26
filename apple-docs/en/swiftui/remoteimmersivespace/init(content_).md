---
title: 'init(content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/remoteimmersivespace/init(content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/remoteimmersivespace/init(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/remoteimmersivespace/init%28content%3A%29.json'
content_hash: 'sha256:31df30638a001363'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [RemoteImmersiveSpace](../remoteimmersivespace.md)

# init(content:)

<sub>Initializer</sub>

Creates a remote immersive space.

<sub>macOS</sub>

```swift
nonisolated init<C>(@CompositorContentBuilder content: @escaping () -> C) where Content == CompositorContentBuilder.Content<C>, Data == Never, C : CompositorContent
```

## Parameters

- `content` — A compositor content builder that defines the content of the space.

## Discussion

The space uses the specified content builder to form the content.

---
title: 'init(id:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/remoteimmersivespace/init(id:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/remoteimmersivespace/init(id:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/remoteimmersivespace/init%28id%3Acontent%3A%29.json'
content_hash: 'sha256:e7f8a03739e0febc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [RemoteImmersiveSpace](../remoteimmersivespace.md)

# init(id:content:)

<sub>Initializer</sub>

Creates the remote immersive space associated with the specified identifier.

<sub>macOS</sub>

```swift
nonisolated init<C>(id: String, @CompositorContentBuilder content: @escaping () -> C) where Content == CompositorContentBuilder.Content<C>, Data == Never, C : CompositorContent
```

## Parameters

- `id` — A string that uniquely identifies the immersive space. Ensure that identifiers are unique among the immersive spaces in your app.

- `content` — An compositor content builder that defines the content of the space.

## Discussion

The space uses the specified content builder to form the content.

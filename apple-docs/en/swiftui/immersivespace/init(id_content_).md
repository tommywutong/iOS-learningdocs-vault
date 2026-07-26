---
title: 'init(id:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [visionOS 1.0+（26.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/immersivespace/init(id:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/immersivespace/init(id:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/immersivespace/init%28id%3Acontent%3A%29.json'
content_hash: 'sha256:a0f170b7af6e33ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ImmersiveSpace](../immersivespace.md)

# init(id:content:)

<sub>Initializer</sub>

Creates the immersive space associated with the specified identifier.

<sub>visionOS</sub>

```swift
nonisolated init(id: String, @ImmersiveSpaceContentBuilder content: () -> Content) where Data == Never
```

## Parameters

- `id` — A string that uniquely identifies the immersive space. Ensure that identifiers are unique among the immersive spaces in your app.

- `content` — An immersive space content builder that defines the content of the space.

## Discussion

The space uses the specified content builder to form the content.

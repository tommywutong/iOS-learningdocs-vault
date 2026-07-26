---
title: 'init(content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/immersivespace/init(content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/immersivespace/init(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/immersivespace/init%28content%3A%29.json'
content_hash: 'sha256:43e1aef9448ceb1f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ImmersiveSpace](../immersivespace.md)

# init(content:)

<sub>Initializer</sub>

Creates an immersive space.

<sub>visionOS</sub>

```swift
nonisolated init(@ImmersiveSpaceContentBuilder content: @escaping () -> Content) where Data == Never
```

## Parameters

- `content` — An immersive space content builder that defines the content of the space.

## Discussion

The space uses the specified content builder to form the content.

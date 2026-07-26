---
title: 'init(id:makeContent:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/immersivespace/init(id:makecontent:)'
source_url: 'https://developer.apple.com/documentation/swiftui/immersivespace/init(id:makecontent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/immersivespace/init%28id%3Amakecontent%3A%29.json'
content_hash: 'sha256:8852f0020dac25df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ImmersiveSpace](../immersivespace.md)

# init(id:makeContent:)

<sub>Initializer</sub>

Creates the immersive space associated with the specified identifier.

<sub>visionOS</sub>

```swift
@export(implementation) nonisolated init(id: String, @ImmersiveSpaceContentBuilder makeContent: @escaping () -> Content) where Data == Never
```

## Parameters

- `id` — A string that uniquely identifies the immersive space. Ensure that identifiers are unique among the immersive spaces in your app.

## Discussion

The space uses the specified content builder to form the content.

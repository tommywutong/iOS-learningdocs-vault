---
title: 'init(foveatedStreaming:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [visionOS 26.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/immersivespace/init(foveatedstreaming:)'
source_url: 'https://developer.apple.com/documentation/swiftui/immersivespace/init(foveatedstreaming:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/immersivespace/init%28foveatedstreaming%3A%29.json'
content_hash: 'sha256:e6a7949dc3f7cf6d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ImmersiveSpace](../immersivespace.md)

# init(foveatedStreaming:)

<sub>Initializer</sub>

Creates an immersive space to display foveated streaming content.

<sub>visionOS</sub>

```swift
nonisolated init(foveatedStreaming session: FoveatedStreamingSession) where Content == ImmersiveSpaceViewContent<FoveatedStreamingSpaceContent>, Data == Never
```

## Parameters

- `session` — The foveated streaming session whose streamed content the space displays.

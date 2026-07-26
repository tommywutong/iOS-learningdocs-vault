---
title: 'init(foveatedStreaming:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [visionOS 26.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/immersivespace/init(foveatedstreaming:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/immersivespace/init(foveatedstreaming:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/immersivespace/init%28foveatedstreaming%3Acontent%3A%29.json'
content_hash: 'sha256:d7587c51139c311b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ImmersiveSpace](../immersivespace.md)

# init(foveatedStreaming:content:)

<sub>Initializer</sub>

Creates an immersive space to display foveated streaming content alongside `RealityKit` content.

<sub>visionOS</sub>

```swift
nonisolated init<V>(foveatedStreaming session: FoveatedStreamingSession, @ViewBuilder content: @escaping () -> V) where Content == ImmersiveSpaceViewContent<FoveatedStreamingSpaceContent>, Data == Never, V : View
```

## Parameters

- `session` — The foveated streaming session whose streamed content the space displays.

- `content` — An immersive space content builder that defines the content of the space.

## Discussion

You can add [RealityKit](../../realitykit.md) content to your space that coexists alongside the streamed content, for example:

```swift
ImmersiveSpace(foveatedStreaming: session) {
    RealityView { content in
        // Add a sphere to the immersive space.
        let entity = ModelEntity(mesh: .generateSphere(radius: 0.1),
                         materials: [SimpleMaterial()])
        content.add(entity)
    }
}
```

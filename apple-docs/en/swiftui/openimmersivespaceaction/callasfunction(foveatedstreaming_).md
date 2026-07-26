---
title: 'callAsFunction(foveatedStreaming:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 26.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/openimmersivespaceaction/callasfunction(foveatedstreaming:)'
source_url: 'https://developer.apple.com/documentation/swiftui/openimmersivespaceaction/callasfunction(foveatedstreaming:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/openimmersivespaceaction/callasfunction%28foveatedstreaming%3A%29.json'
content_hash: 'sha256:849aa0d1688150a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [OpenImmersiveSpaceAction](../openimmersivespaceaction.md)

# callAsFunction(foveatedStreaming:)

<sub>Instance Method</sub>

Presents the immersive space that your app defines for the specified foveated streaming session.

<sub>visionOS</sub>

```swift
@discardableResult @MainActor func callAsFunction(foveatedStreaming session: FoveatedStreamingSession) async -> OpenImmersiveSpaceAction.Result
```

## Parameters

- `session` — The foveated streaming session associated with the immersive space to present.

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the `<doc://com.apple.documentation/documentation/swiftui/environmentvalues/openimmersivespace>` action with a foveated streaming session:

```swift
await openImmersiveSpace(foveatedStreaming: session)
```

For information about how Swift uses the `callAsFunction()` method to simplify call site syntax, see [Methods with Special Names](https://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID622) in _The Swift Programming Language_.

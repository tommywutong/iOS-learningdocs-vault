---
title: 'persistentSystemOverlays(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/compositorcontent/persistentsystemoverlays(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/compositorcontent/persistentsystemoverlays(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/compositorcontent/persistentsystemoverlays%28_%3A%29.json'
content_hash: 'sha256:f50c56bcc575b095'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CompositorContent](../compositorcontent.md)

# persistentSystemOverlays(_:)

<sub>Instance Method</sub>

Sets the preferred visibility of the non-transient system views overlaying the app.

<sub>macOS, visionOS</sub>

```swift
nonisolated func persistentSystemOverlays(_ visibility: Visibility) -> some CompositorContent

```

## Parameters

- `visibility` — A value that indicates the visibility of the non-transient system views overlaying the app.

## Discussion

Use this modifier to influence the appearance of system overlays in your app. The behavior varies by platform. For an [ImmersiveSpace](../immersivespace.md), it affects the Home indicator.

> [!note] Note
> You can indicate a preference with this modifier, but the system might or might not be able to honor that preference.

Affected non-transient system views can include, but are not limited to:

- The Home indicator.
- The SharePlay indicator.
- The Multitasking Controls button and Picture in Picture on iPad.

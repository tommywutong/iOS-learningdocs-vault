---
title: 'onWorldRecenter(action:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/compositorcontent/onworldrecenter(action:)'
source_url: 'https://developer.apple.com/documentation/swiftui/compositorcontent/onworldrecenter(action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/compositorcontent/onworldrecenter%28action%3A%29.json'
content_hash: 'sha256:73bfe37ad37646f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CompositorContent](../compositorcontent.md)

# onWorldRecenter(action:)

<sub>Instance Method</sub>

Adds an action to perform when recentering the view with the digital crown.

<sub>macOS, visionOS</sub>

```swift
nonisolated func onWorldRecenter(action: @escaping @MainActor () -> Void) -> some CompositorContent

```

## Parameters

- `action` — A closure to run when the content is recentered. This will run when the app has been recentered and is about to fade back in, equivalent to `WorldRecenterPhase.ended`.

## Discussion

When the user recenters their content, the app will fade out and then be repositioned. Once it has been repositioned, the action will be called and the app will fade back in. The action will be called if the app is not backgrounded or suspended.

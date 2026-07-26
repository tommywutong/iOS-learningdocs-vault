---
title: 'onDisappear(perform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/compositorcontent/ondisappear(perform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/compositorcontent/ondisappear(perform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/compositorcontent/ondisappear%28perform%3A%29.json'
content_hash: 'sha256:3bcd384e5c0179c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CompositorContent](../compositorcontent.md)

# onDisappear(perform:)

<sub>Instance Method</sub>

Adds an action to perform after this content disappears.

<sub>macOS, visionOS</sub>

```swift
nonisolated func onDisappear(perform action: (() -> Void)? = nil) -> some CompositorContent

```

## Parameters

- `action` — The action to perform. If `action` is `nil`, the call has no effect.

## Return Value

A CompositorContent that triggers `action` after it disappears.

## Discussion

The exact moment that SwiftUI calls this method depends on the specific content type that you apply it to, but the `action` closure doesn’t execute until the content disappears from the interface.

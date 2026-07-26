---
title: 'onAppear(perform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/compositorcontent/onappear(perform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/compositorcontent/onappear(perform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/compositorcontent/onappear%28perform%3A%29.json'
content_hash: 'sha256:661e624c2789cf65'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CompositorContent](../compositorcontent.md)

# onAppear(perform:)

<sub>Instance Method</sub>

Adds an action to perform before this content appears.

<sub>macOS, visionOS</sub>

```swift
nonisolated func onAppear(perform action: (() -> Void)? = nil) -> some CompositorContent

```

## Parameters

- `action` — The action to perform. If `action` is `nil`, the call has no effect.

## Return Value

A CompositorContent that triggers `action` before it appears.

## Discussion

The exact moment that SwiftUI calls this method depends on the specific content type that you apply it to, but the `action` closure completes before the first rendered frame appears.

---
title: 'body(content:context:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/previewmodifier/body(content:context:)'
source_url: 'https://developer.apple.com/documentation/swiftui/previewmodifier/body(content:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/previewmodifier/body%28content%3Acontext%3A%29.json'
content_hash: 'sha256:3e68d303e0bd549d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PreviewModifier](../previewmodifier.md)

# body(content:context:)

<sub>Instance Method</sub>

Modify a preview by applying the shared context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@ContentBuilder @MainActor func body(content: Self.Content, context: Self.Context) -> Self.Body
```

## Parameters

- `content` — A proxy for the preview being modified.

- `context` — The shared context to apply.

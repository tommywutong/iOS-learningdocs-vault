---
title: 'init(isEnabled:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/externalnoninteractiveaccessory/init(isenabled:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/externalnoninteractiveaccessory/init(isenabled:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/externalnoninteractiveaccessory/init%28isenabled%3Acontent%3A%29.json'
content_hash: 'sha256:d68186f7ae2eb4a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ExternalNonInteractiveAccessory](../externalnoninteractiveaccessory.md)

# init(isEnabled:content:)

<sub>Initializer</sub>

Creates a scene accessory that presents non-interactive content on an external display with a binding for programmatic enablement.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
nonisolated init(isEnabled: Binding<Bool>, @ContentBuilder content: @escaping () -> Content)
```

## Parameters

- `isEnabled` — A binding for whether or not the accessory should present if available.

- `content` — The scene’s content.

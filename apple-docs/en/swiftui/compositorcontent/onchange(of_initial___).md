---
title: 'onChange(of:initial:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/compositorcontent/onchange(of:initial:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/compositorcontent/onchange(of:initial:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/compositorcontent/onchange%28of%3Ainitial%3A_%3A%29.json'
content_hash: 'sha256:465e34197aa702e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CompositorContent](../compositorcontent.md)

# onChange(of:initial:_:)

<sub>Instance Method</sub>

<sub>macOS, visionOS</sub>

```swift
nonisolated func onChange<V>(of value: V, initial: Bool = false, _ action: @escaping () -> Void) -> some CompositorContent where V : Equatable

```

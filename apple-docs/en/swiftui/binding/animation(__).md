---
title: 'animation(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/binding/animation(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/binding/animation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/binding/animation%28_%3A%29.json'
content_hash: 'sha256:4da5b04d6860e829'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Binding](../binding.md)

# animation(_:)

<sub>Instance Method</sub>

Specifies an animation to perform when the binding value changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func animation(_ animation: Animation? = .default) -> Binding<Value>
```

## Parameters

- `animation` — An animation sequence performed when the binding value changes.

## Return Value

A new binding.

## See Also

### Managing changes

- [id](id.md) — The stable identity of the entity associated with this instance, corresponding to the `id` of the binding’s wrapped value.
- [transaction(_:)](<transaction(__).md>) — Specifies a transaction for the binding.
- [transaction](transaction.md) — The binding’s transaction.

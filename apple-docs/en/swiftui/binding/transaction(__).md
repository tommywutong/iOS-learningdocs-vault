---
title: 'transaction(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/binding/transaction(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/binding/transaction(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/binding/transaction%28_%3A%29.json'
content_hash: 'sha256:1c36ef547bad8195'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Binding](../binding.md)

# transaction(_:)

<sub>Instance Method</sub>

Specifies a transaction for the binding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func transaction(_ transaction: Transaction) -> Binding<Value>
```

## Parameters

- `transaction` — An instance of a [Transaction](../transaction.md).

## Return Value

A new binding.

## See Also

### Managing changes

- [id](id.md) — The stable identity of the entity associated with this instance, corresponding to the `id` of the binding’s wrapped value.
- [animation(_:)](<animation(__).md>) — Specifies an animation to perform when the binding value changes.
- [transaction](transaction.md) — The binding’s transaction.

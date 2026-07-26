---
title: transaction
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/binding/transaction
source_url: 'https://developer.apple.com/documentation/swiftui/binding/transaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/binding/transaction.json'
content_hash: 'sha256:0ca0490af3ac358e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Binding](../binding.md)

# transaction

<sub>Instance Property</sub>

The binding’s transaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var transaction: Transaction
```

## Discussion

The transaction captures the information needed to update the view when the binding value changes.

## See Also

### Managing changes

- [id](id.md) — The stable identity of the entity associated with this instance, corresponding to the `id` of the binding’s wrapped value.
- [animation(_:)](<animation(__).md>) — Specifies an animation to perform when the binding value changes.
- [transaction(_:)](<transaction(__).md>) — Specifies a transaction for the binding.

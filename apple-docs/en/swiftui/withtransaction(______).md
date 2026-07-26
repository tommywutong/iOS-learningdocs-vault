---
title: 'withTransaction(_:_:_:)'
framework: SwiftUI
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/withtransaction(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/withtransaction(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/withtransaction%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:7a965d2df11c3acd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# withTransaction(_:_:_:)

<sub>Function</sub>

Executes a closure with the specified transaction key path and value and returns the result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) func withTransaction<R, V>(_ keyPath: WritableKeyPath<Transaction, V>, _ value: V, _ body: () throws -> R) rethrows -> R
```

## Parameters

- `keyPath` — A key path that indicates the property of the [Transaction](transaction.md) structure to update.

- `value` — The new value to set for the item specified by `keyPath`.

- `body` — A closure to execute.

## Return Value

The result of executing the closure with the specified transaction value.

## See Also

### Moving an animation to another view

- [withTransaction(_:_:)](<withtransaction(____).md>) — Executes a closure with the specified transaction and returns the result.
- [transaction(_:)](<view/transaction(__).md>) — Applies the given transaction mutation function to all animations used within the view.
- [transaction(value:_:)](<view/transaction(value___).md>) — Applies the given transaction mutation function to all animations used within the view.
- [transaction(_:body:)](<view/transaction(__body_).md>) — Applies the given transaction mutation function to all animations used within the `body` closure.
- [Transaction](transaction.md) — The context of the current state-processing update.
- [Entry()](<entry().md>) — Creates an environment values, transaction, container values, or focused values entry.
- [TransactionKey](transactionkey.md) — A key for accessing values in a transaction.

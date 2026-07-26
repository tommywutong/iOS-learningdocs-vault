---
title: 'withTransaction(_:_:)'
framework: SwiftUI
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/withtransaction(_:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/withtransaction(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/withtransaction%28_%3A_%3A%29.json'
content_hash: 'sha256:4f26b0b552625897'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# withTransaction(_:_:)

<sub>Function</sub>

Executes a closure with the specified transaction and returns the result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withTransaction<Result>(_ transaction: Transaction, _ body: () throws -> Result) rethrows -> Result
```

## Parameters

- `body` — A closure to execute.

## Return Value

The result of executing the closure with the specified transaction.

## See Also

### Moving an animation to another view

- [withTransaction(_:_:_:)](<withtransaction(______).md>) — Executes a closure with the specified transaction key path and value and returns the result.
- [transaction(_:)](<view/transaction(__).md>) — Applies the given transaction mutation function to all animations used within the view.
- [transaction(value:_:)](<view/transaction(value___).md>) — Applies the given transaction mutation function to all animations used within the view.
- [transaction(_:body:)](<view/transaction(__body_).md>) — Applies the given transaction mutation function to all animations used within the `body` closure.
- [Transaction](transaction.md) — The context of the current state-processing update.
- [Entry()](<entry().md>) — Creates an environment values, transaction, container values, or focused values entry.
- [TransactionKey](transactionkey.md) — A key for accessing values in a transaction.

---
title: 'transaction(_:body:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/transaction(_:body:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/transaction(_:body:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/transaction%28_%3Abody%3A%29.json'
content_hash: 'sha256:5cd728c8014960a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# transaction(_:body:)

<sub>Instance Method</sub>

Applies the given transaction mutation function to all animations used within the `body` closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func transaction<V>(_ transform: @escaping (inout Transaction) -> Void, @ContentBuilder body: (PlaceholderContentView<Self>) -> V) -> some View where V : View

```

## Discussion

Any modifiers applied to the content of `body` will be applied to this view, and the changes to the transaction performed in the `transform` will only affect the modifiers defined in the `body`.

The following code animates the opacity changing with a faster animation, while the contents of MyView are animated with the implicit transaction:

```swift
MyView(isActive: isActive)
    .transaction { transaction in
        transaction.animation = transaction.animation?.speed(2)
    } body: { content in
        content.opacity(isActive ? 1.0 : 0.0)
    }
```

- See Also: `Transaction.disablesAnimations`

## See Also

### Moving an animation to another view

- [withTransaction(_:_:)](<../withtransaction(____).md>) — Executes a closure with the specified transaction and returns the result.
- [withTransaction(_:_:_:)](<../withtransaction(______).md>) — Executes a closure with the specified transaction key path and value and returns the result.
- [transaction(_:)](<transaction(__).md>) — Applies the given transaction mutation function to all animations used within the view.
- [transaction(value:_:)](<transaction(value___).md>) — Applies the given transaction mutation function to all animations used within the view.
- [Transaction](../transaction.md) — The context of the current state-processing update.
- [Entry()](<../entry().md>) — Creates an environment values, transaction, container values, or focused values entry.
- [TransactionKey](../transactionkey.md) — A key for accessing values in a transaction.

---
title: 'subscript(_:)'
framework: SwiftUI
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/transaction/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/transaction/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/transaction/subscript%28_%3A%29.json'
content_hash: 'sha256:7e16dd29cc9c29d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Transaction](../transaction.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the transaction value associated with a custom key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript<K>(key: K.Type) -> K.Value where K : TransactionKey { get set }
```

## Overview

Create custom transaction values by defining a key that conforms to the [TransactionKey](../transactionkey.md) protocol, and then using that key with the subscript operator of the [Transaction](../transaction.md) structure to get and set a value for that key:

```swift
private struct MyTransactionKey: TransactionKey {
    static let defaultValue = false
}

extension Transaction {
    var myCustomValue: Bool {
        get { self[MyTransactionKey.self] }
        set { self[MyTransactionKey.self] = newValue }
    }
}
```

## See Also

### Getting information about a transaction

- [isContinuous](iscontinuous.md) — A Boolean value that indicates whether the transaction originated from an action that produces a sequence of values.
- [scrollTargetAnchor](scrolltargetanchor.md) — The preferred alignment of the view within a scroll view’s visible region when scrolling to a view.
- [tracksVelocity](tracksvelocity.md) — Whether this transaction will track the velocity of any animatable properties that change.

---
title: 'paymentQueue(_:removedTransactions:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS 9.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skpaymenttransactionobserver/paymentqueue(_:removedtransactions:)'
source_url: 'https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/paymentqueue(_:removedtransactions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymenttransactionobserver/paymentqueue%28_%3Aremovedtransactions%3A%29.json'
content_hash: 'sha256:b36b8805a404138c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentTransactionObserver](../skpaymenttransactionobserver.md)

# paymentQueue(_:removedTransactions:)

<sub>Instance Method</sub>

Tells an observer that one or more transactions have been removed from the queue.

> [!warning] Deprecated
> Use StoreKit 2 Transaction APIs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func paymentQueue(_ queue: SKPaymentQueue, removedTransactions transactions: [SKPaymentTransaction])
```

## Parameters

- `queue` — The payment queue that updated the transactions.

- `transactions` — An array of the transactions that were removed.

## Discussion

Your application does not typically need to implement this method but might implement it to update its own user interface to reflect that a transaction has been completed.

## See Also

### Handling transactions

- [- paymentQueue:updatedTransactions:](<paymentqueue(__updatedtransactions_).md>) — Tells an observer that one or more transactions have been updated. _(deprecated)_

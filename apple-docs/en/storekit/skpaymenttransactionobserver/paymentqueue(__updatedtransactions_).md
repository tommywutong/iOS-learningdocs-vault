---
title: 'paymentQueue(_:updatedTransactions:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS 9.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skpaymenttransactionobserver/paymentqueue(_:updatedtransactions:)'
source_url: 'https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/paymentqueue(_:updatedtransactions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymenttransactionobserver/paymentqueue%28_%3Aupdatedtransactions%3A%29.json'
content_hash: 'sha256:4028e9073c12d982'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentTransactionObserver](../skpaymenttransactionobserver.md)

# paymentQueue(_:updatedTransactions:)

<sub>Instance Method</sub>

Tells an observer that one or more transactions have been updated.

> [!warning] Deprecated
> Use StoreKit 2 Transaction APIs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func paymentQueue(_ queue: SKPaymentQueue, updatedTransactions transactions: [SKPaymentTransaction])
```

## Parameters

- `queue` — The payment queue that updated the transactions.

- `transactions` — An array of the transactions that were updated.

## Discussion

The application should process each transaction by examining the transaction’s [transactionState](../skpaymenttransaction/transactionstate.md) property. If [transactionState](../skpaymenttransaction/transactionstate.md) is [SKPaymentTransactionStatePurchased](../skpaymenttransactionstate/purchased.md), payment was successfully received for the desired functionality. The application should make the functionality available to the user. If [transactionState](../skpaymenttransaction/transactionstate.md) is [SKPaymentTransactionStateFailed](../skpaymenttransactionstate/failed.md), the application can read the transaction’s error property to return a meaningful error to the user.

Once a transaction is processed, it should be removed from the payment queue by calling the payment queue’s [- finishTransaction:](<../skpaymentqueue/finishtransaction(__).md>) method, passing the transaction as a parameter.

> [!important] Important
> Once the transaction is finished, StoreKit can’t tell you that this item is already purchased. It is important that applications process the transaction completely before calling [- finishTransaction:](<../skpaymentqueue/finishtransaction(__).md>).

## See Also

### Related Documentation

- [In-App Purchase Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267)

### Handling transactions

- [- paymentQueue:removedTransactions:](<paymentqueue(__removedtransactions_).md>) — Tells an observer that one or more transactions have been removed from the queue. _(deprecated)_

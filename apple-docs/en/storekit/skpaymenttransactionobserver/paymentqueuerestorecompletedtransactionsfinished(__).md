---
title: 'paymentQueueRestoreCompletedTransactionsFinished(_:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS 9.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skpaymenttransactionobserver/paymentqueuerestorecompletedtransactionsfinished(_:)'
source_url: 'https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/paymentqueuerestorecompletedtransactionsfinished(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymenttransactionobserver/paymentqueuerestorecompletedtransactionsfinished%28_%3A%29.json'
content_hash: 'sha256:f5c8f08d9f0e89b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentTransactionObserver](../skpaymenttransactionobserver.md)

# paymentQueueRestoreCompletedTransactionsFinished(_:)

<sub>Instance Method</sub>

Tells the observer that the payment queue has finished sending restored transactions.

> [!warning] Deprecated
> Use AppStore.sync().

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func paymentQueueRestoreCompletedTransactionsFinished(_ queue: SKPaymentQueue)
```

## Parameters

- `queue` — The payment queue that restored the transactions.

## Discussion

This method is called after all restorable transactions have been processed by the payment queue. Your application is not required to do anything in this method.

## See Also

### Restoring transactions

- [- paymentQueue:restoreCompletedTransactionsFailedWithError:](<paymentqueue(__restorecompletedtransactionsfailedwitherror_).md>) — Tells the observer that an error occurred while restoring transactions. _(deprecated)_

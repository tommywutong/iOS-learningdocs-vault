---
title: 'paymentQueue(_:restoreCompletedTransactionsFailedWithError:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS 9.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skpaymenttransactionobserver/paymentqueue(_:restorecompletedtransactionsfailedwitherror:)'
source_url: 'https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/paymentqueue(_:restorecompletedtransactionsfailedwitherror:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymenttransactionobserver/paymentqueue%28_%3Arestorecompletedtransactionsfailedwitherror%3A%29.json'
content_hash: 'sha256:a4789b2fc8e7487b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentTransactionObserver](../skpaymenttransactionobserver.md)

# paymentQueue(_:restoreCompletedTransactionsFailedWithError:)

<sub>Instance Method</sub>

Tells the observer that an error occurred while restoring transactions.

> [!warning] Deprecated
> Use AppStore.sync().

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func paymentQueue(_ queue: SKPaymentQueue, restoreCompletedTransactionsFailedWithError error: any Error)
```

## Parameters

- `queue` — The payment queue that was restoring transactions.

- `error` — The error that occurred.

## See Also

### Restoring transactions

- [- paymentQueueRestoreCompletedTransactionsFinished:](<paymentqueuerestorecompletedtransactionsfinished(__).md>) — Tells the observer that the payment queue has finished sending restored transactions. _(deprecated)_

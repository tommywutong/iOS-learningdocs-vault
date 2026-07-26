---
title: 'finishTransaction(_:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS 9.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skpaymentqueue/finishtransaction(_:)'
source_url: 'https://developer.apple.com/documentation/storekit/skpaymentqueue/finishtransaction(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymentqueue/finishtransaction%28_%3A%29.json'
content_hash: 'sha256:df3e91e9b2ea453f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentQueue](../skpaymentqueue.md)

# finishTransaction(_:)

<sub>Instance Method</sub>

Notifies the App Store that the app finished processing the transaction.

> [!warning] Deprecated
> Use Transaction.finish().

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func finishTransaction(_ transaction: SKPaymentTransaction)
```

## Parameters

- `transaction` — The transaction to finish.

## Discussion

Transactions on the payment queue are persistent until they are completed. StoreKit calls your observer’s [- paymentQueue:updatedTransactions:](<../skpaymenttransactionobserver/paymentqueue(__updatedtransactions_).md>) method every time your app launches or resumes from background to tell you about transactions in the queue. After you’ve finished processing a transaction in your app, always call the [- finishTransaction:](<finishtransaction(__).md>) method to finish the transaction and remove it from the queue.

Call [- finishTransaction:](<finishtransaction(__).md>) only after the app has finished all work it performs to complete the transaction. The transaction’s state determines which steps you might take:

- For a failed transaction ([SKPaymentTransactionStateFailed](../skpaymenttransactionstate/failed.md)), update your user interface, track information in analytics, and perform other similar tasks.
- For a successful transaction ([SKPaymentTransactionStatePurchased](../skpaymenttransactionstate/purchased.md) or [SKPaymentTransactionStateRestored](../skpaymenttransactionstate/restored.md)), perform all necessary actions to unlock the functionality the user has purchased before finishing the transaction. For example, if you are downloading content, finish the transaction only after the downloads are complete.

If you validate receipts, validate them before completing the transaction, and take one of the paths described above.

In rare circumstances, this call might fail, and you’ll receive updates for that transaction again. For this reason, you should record information in your app about the transactions it has processed and which steps the app has already completed. That way, you don’t repeat steps that shouldn’t be performed multiple times. For example, if you are processing a consumable transaction, you only want to add the consumable benefit once.

If you call [- finishTransaction:](<finishtransaction(__).md>) on a transaction that is in the [SKPaymentTransactionStatePurchasing](../skpaymenttransactionstate/purchasing.md) state, StoreKit raises an exception.

## See Also

### Related Documentation

- [- paymentQueue:updatedTransactions:](<../skpaymenttransactionobserver/paymentqueue(__updatedtransactions_).md>) — Tells an observer that one or more transactions have been updated. _(deprecated)_

### Managing Transactions

- [delegate](delegate.md) — A delegate that provides information needed to complete transactions. _(deprecated)_
- [transactions](transactions.md) — Returns an array of pending transactions. _(deprecated)_
- [- addPayment:](<add(__)-4vct1.md>) — Adds a payment request to the queue. _(deprecated)_

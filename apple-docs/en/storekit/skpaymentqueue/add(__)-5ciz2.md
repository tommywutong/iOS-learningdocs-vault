---
title: 'add(_:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS 9.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skpaymentqueue/add(_:)-5ciz2'
source_url: 'https://developer.apple.com/documentation/storekit/skpaymentqueue/add(_:)-5ciz2'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymentqueue/add%28_%3A%29-5ciz2.json'
content_hash: 'sha256:9cb5a3a3fa286efc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentQueue](../skpaymentqueue.md)

# add(_:)

<sub>Instance Method</sub>

Adds an observer to the payment queue.

> [!warning] Deprecated
> Use Transaction.updates or PurchaseResult from Product.purchase(confirmIn:options:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func add(_ observer: any SKPaymentTransactionObserver)
```

## Parameters

- `observer` — The observer to add to the queue.

## Discussion

Your application should add an observer to the payment queue during application initialization. If there are no observers attached to the queue, the payment queue does not synchronize its list of pending transactions with the Apple App Store, because there is no observer to respond to updated transactions.

If an application quits when transactions are still being processed, those transactions are not lost. The next time the application launches, the payment queue resumes processing the transactions. Your application should always expect to be notified of completed transactions.

If more than one transaction observer is attached to the payment queue, no guarantees are made as to the order which they will be called. It is safe for multiple observers to call [- finishTransaction:](<finishtransaction(__).md>), but not recommended. It is recommended that you use a single observer to process and finish the transaction.

## See Also

### Related Documentation

- [transactions](transactions.md) — Returns an array of pending transactions. _(deprecated)_

### Adding, Getting, and Removing Observers

- [transactionObservers](transactionobservers.md) — An array of all active payment queue observers. _(deprecated)_
- [- removeTransactionObserver:](<remove(__).md>) — Removes an observer from the payment queue. _(deprecated)_

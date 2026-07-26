---
title: transactions
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS 9.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skpaymentqueue/transactions
source_url: 'https://developer.apple.com/documentation/storekit/skpaymentqueue/transactions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymentqueue/transactions.json'
content_hash: 'sha256:edb37cccf4d97725'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentQueue](../skpaymentqueue.md)

# transactions

<sub>Instance Property</sub>

Returns an array of pending transactions.

> [!warning] Deprecated
> Use Transaction.unfinished.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var transactions: [SKPaymentTransaction] { get }
```

## Discussion

The value of this property is undefined when there are no observers attached to the payment queue.

## See Also

### Related Documentation

- [- addTransactionObserver:](<add(__)-5ciz2.md>) — Adds an observer to the payment queue. _(deprecated)_

### Managing Transactions

- [delegate](delegate.md) — A delegate that provides information needed to complete transactions. _(deprecated)_
- [- addPayment:](<add(__)-4vct1.md>) — Adds a payment request to the queue. _(deprecated)_
- [- finishTransaction:](<finishtransaction(__).md>) — Notifies the App Store that the app finished processing the transaction. _(deprecated)_

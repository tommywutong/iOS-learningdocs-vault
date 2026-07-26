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
doc_path: '/documentation/storekit/skpaymentqueue/add(_:)-4vct1'
source_url: 'https://developer.apple.com/documentation/storekit/skpaymentqueue/add(_:)-4vct1'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymentqueue/add%28_%3A%29-4vct1.json'
content_hash: 'sha256:db1ae43016010d8d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentQueue](../skpaymentqueue.md)

# add(_:)

<sub>Instance Method</sub>

Adds a payment request to the queue.

> [!warning] Deprecated
> Use Product.purchase(confirmIn:options:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func add(_ payment: SKPayment)
```

## Parameters

- `payment` — A payment request.

## Discussion

An application should always have at least one observer of the payment queue before adding payment requests.

The payment request must have a product identifier registered with the Apple App Store and a quantity greater than `0`. If either property is invalid, [- addPayment:](<add(__)-4vct1.md>) throws an exception.

When a payment request is added to the queue, the payment queue processes that request with the Apple App Store and arranges for payment from the user. When that transaction is complete or if a failure occurs, the payment queue sends the [SKPaymentTransaction](../skpaymenttransaction.md) object that encapsulates the request to all transaction observers.

## See Also

### Managing Transactions

- [delegate](delegate.md) — A delegate that provides information needed to complete transactions. _(deprecated)_
- [transactions](transactions.md) — Returns an array of pending transactions. _(deprecated)_
- [- finishTransaction:](<finishtransaction(__).md>) — Notifies the App Store that the app finished processing the transaction. _(deprecated)_

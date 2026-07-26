---
title: transactionObservers
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+（18.0 起废弃）, iPadOS 14.0+（18.0 起废弃）, Mac Catalyst 14.0+（18.0 起废弃）, macOS 11.0+（15.0 起废弃）, tvOS 14.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 7.0+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skpaymentqueue/transactionobservers
source_url: 'https://developer.apple.com/documentation/storekit/skpaymentqueue/transactionobservers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymentqueue/transactionobservers.json'
content_hash: 'sha256:f90423ecd52e3f9b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentQueue](../skpaymentqueue.md)

# transactionObservers

<sub>Instance Property</sub>

An array of all active payment queue observers.

> [!warning] Deprecated
> Use Transaction.updates or PurchaseResult from Product.purchase(confirmIn:options:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var transactionObservers: [any SKPaymentTransactionObserver] { get }
```

## See Also

### Adding, Getting, and Removing Observers

- [- addTransactionObserver:](<add(__)-5ciz2.md>) — Adds an observer to the payment queue. _(deprecated)_
- [- removeTransactionObserver:](<remove(__).md>) — Removes an observer from the payment queue. _(deprecated)_

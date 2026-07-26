---
title: delegate
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+（18.0 起废弃）, iPadOS 13.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.15+（15.0 起废弃）, tvOS 13.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skpaymentqueue/delegate
source_url: 'https://developer.apple.com/documentation/storekit/skpaymentqueue/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymentqueue/delegate.json'
content_hash: 'sha256:eefdbd30bcab6ac0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentQueue](../skpaymentqueue.md)

# delegate

<sub>Instance Property</sub>

A delegate that provides information needed to complete transactions.

> [!warning] Deprecated
> No longer supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
weak var delegate: (any SKPaymentQueueDelegate)? { get set }
```

## Discussion

This delegate implements the [SKPaymentQueueDelegate](../skpaymentqueuedelegate.md) protocol.

## See Also

### Managing Transactions

- [transactions](transactions.md) — Returns an array of pending transactions. _(deprecated)_
- [- addPayment:](<add(__)-4vct1.md>) — Adds a payment request to the queue. _(deprecated)_
- [- finishTransaction:](<finishtransaction(__).md>) — Notifies the App Store that the app finished processing the transaction. _(deprecated)_

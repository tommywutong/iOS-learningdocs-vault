---
title: 'remove(_:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS 9.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skpaymentqueue/remove(_:)'
source_url: 'https://developer.apple.com/documentation/storekit/skpaymentqueue/remove(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymentqueue/remove%28_%3A%29.json'
content_hash: 'sha256:9d955c11a1163cde'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentQueue](../skpaymentqueue.md)

# remove(_:)

<sub>Instance Method</sub>

Removes an observer from the payment queue.

> [!warning] Deprecated
> No longer supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func remove(_ observer: any SKPaymentTransactionObserver)
```

## Parameters

- `observer` — The observer to remove.

## Discussion

If there are no observers attached to the queue, the payment queue does not synchronize its list of pending transactions with the Apple App Store, because there is no observer to respond to updated transactions.

## See Also

### Related Documentation

- [transactions](transactions.md) — Returns an array of pending transactions. _(deprecated)_

### Adding, Getting, and Removing Observers

- [- addTransactionObserver:](<add(__)-5ciz2.md>) — Adds an observer to the payment queue. _(deprecated)_
- [transactionObservers](transactionobservers.md) — An array of all active payment queue observers. _(deprecated)_

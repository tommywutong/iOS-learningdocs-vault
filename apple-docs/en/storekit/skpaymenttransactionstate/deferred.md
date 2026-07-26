---
title: SKPaymentTransactionState.deferred
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+（18.0 起废弃）, iPadOS 8.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.10+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skpaymenttransactionstate/deferred
source_url: 'https://developer.apple.com/documentation/storekit/skpaymenttransactionstate/deferred'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymenttransactionstate/deferred.json'
content_hash: 'sha256:cd2afea7ebf28c9f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentTransactionState](../skpaymenttransactionstate.md)

# SKPaymentTransactionState.deferred

<sub>Case</sub>

A transaction that is in the queue, but its final status is pending external action such as Ask to Buy.

> [!warning] Deprecated
> Use PurchaseResult.pending from Product.purchase(confirmIn:options:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case deferred
```

## Discussion

Update your UI to show the deferred state, and wait for another callback that indicates the final status.

## See Also

### Constants

- [SKPaymentTransactionStatePurchasing](purchasing.md) — A transaction that is being processed by the App Store. _(deprecated)_
- [SKPaymentTransactionStatePurchased](purchased.md) — A successfully processed transaction. _(deprecated)_
- [SKPaymentTransactionStateFailed](failed.md) — A failed transaction. _(deprecated)_
- [SKPaymentTransactionStateRestored](restored.md) — A transaction that restores content previously purchased by the user. _(deprecated)_

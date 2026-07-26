---
title: SKPaymentTransactionState.purchasing
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skpaymenttransactionstate/purchasing
source_url: 'https://developer.apple.com/documentation/storekit/skpaymenttransactionstate/purchasing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymenttransactionstate/purchasing.json'
content_hash: 'sha256:d7f57a5d4db597cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentTransactionState](../skpaymenttransactionstate.md)

# SKPaymentTransactionState.purchasing

<sub>Case</sub>

A transaction that is being processed by the App Store.

> [!warning] Deprecated
> Use PurchaseResult from Product.purchase(confirmIn:options:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case purchasing
```

## See Also

### Constants

- [SKPaymentTransactionStatePurchased](purchased.md) — A successfully processed transaction. _(deprecated)_
- [SKPaymentTransactionStateFailed](failed.md) — A failed transaction. _(deprecated)_
- [SKPaymentTransactionStateRestored](restored.md) — A transaction that restores content previously purchased by the user. _(deprecated)_
- [SKPaymentTransactionStateDeferred](deferred.md) — A transaction that is in the queue, but its final status is pending external action such as Ask to Buy. _(deprecated)_

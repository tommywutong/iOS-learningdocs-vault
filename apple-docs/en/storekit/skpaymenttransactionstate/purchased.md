---
title: SKPaymentTransactionState.purchased
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skpaymenttransactionstate/purchased
source_url: 'https://developer.apple.com/documentation/storekit/skpaymenttransactionstate/purchased'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymenttransactionstate/purchased.json'
content_hash: 'sha256:d2d10404229f7976'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentTransactionState](../skpaymenttransactionstate.md)

# SKPaymentTransactionState.purchased

<sub>Case</sub>

A successfully processed transaction.

> [!warning] Deprecated
> Use PurchaseResult from Product.purchase(confirmIn:options:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case purchased
```

## Discussion

Your application should provide the content the user purchased.

## See Also

### Constants

- [SKPaymentTransactionStatePurchasing](purchasing.md) — A transaction that is being processed by the App Store. _(deprecated)_
- [SKPaymentTransactionStateFailed](failed.md) — A failed transaction. _(deprecated)_
- [SKPaymentTransactionStateRestored](restored.md) — A transaction that restores content previously purchased by the user. _(deprecated)_
- [SKPaymentTransactionStateDeferred](deferred.md) — A transaction that is in the queue, but its final status is pending external action such as Ask to Buy. _(deprecated)_

---
title: transactionState
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skpaymenttransaction/transactionstate
source_url: 'https://developer.apple.com/documentation/storekit/skpaymenttransaction/transactionstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymenttransaction/transactionstate.json'
content_hash: 'sha256:2c40fad09e597947'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentTransaction](../skpaymenttransaction.md)

# transactionState

<sub>Instance Property</sub>

The current state of the transaction.

> [!warning] Deprecated
> Use PurchaseResult from Product.purchase(confirmIn:options:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var transactionState: SKPaymentTransactionState { get }
```

## See Also

### Getting Transaction State

- [SKPaymentTransactionState](../skpaymenttransactionstate.md) — Values representing the state of a transaction. _(deprecated)_

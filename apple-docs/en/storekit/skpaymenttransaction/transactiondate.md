---
title: transactionDate
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skpaymenttransaction/transactiondate
source_url: 'https://developer.apple.com/documentation/storekit/skpaymenttransaction/transactiondate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymenttransaction/transactiondate.json'
content_hash: 'sha256:0ba054e2c80c5736'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentTransaction](../skpaymenttransaction.md)

# transactionDate

<sub>Instance Property</sub>

The date the transaction was added to the App Store’s payment queue.

> [!warning] Deprecated
> Use PurchaseResult from Product.purchase(confirmIn:options:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var transactionDate: Date? { get }
```

## Discussion

The contents of this property are undefined except when [transactionState](transactionstate.md) is set to [SKPaymentTransactionStatePurchased](../skpaymenttransactionstate/purchased.md) or [SKPaymentTransactionStateRestored](../skpaymenttransactionstate/restored.md).

## See Also

### Getting Transaction Information

- [payment](payment.md) — The payment for the transaction. _(deprecated)_
- [transactionIdentifier](transactionidentifier.md) — A string that uniquely identifies a successful payment transaction. _(deprecated)_
- [originalTransaction](original.md) — The transaction that was restored by the App Store. _(deprecated)_
- [error](error.md) — An object describing the error that occurred while processing the transaction. _(deprecated)_
- [transactionReceipt](transactionreceipt.md) — A signed receipt that records all information about a successful payment transaction. _(deprecated)_

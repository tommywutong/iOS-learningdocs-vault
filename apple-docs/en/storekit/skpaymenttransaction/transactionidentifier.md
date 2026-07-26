---
title: transactionIdentifier
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skpaymenttransaction/transactionidentifier
source_url: 'https://developer.apple.com/documentation/storekit/skpaymenttransaction/transactionidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymenttransaction/transactionidentifier.json'
content_hash: 'sha256:7a1272eae359e3ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentTransaction](../skpaymenttransaction.md)

# transactionIdentifier

<sub>Instance Property</sub>

A string that uniquely identifies a successful payment transaction.

> [!warning] Deprecated
> Use PurchaseResult from Product.purchase(confirmIn:options:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var transactionIdentifier: String? { get }
```

## Discussion

The contents of this property are undefined except when [transactionState](transactionstate.md) is set to [SKPaymentTransactionStatePurchased](../skpaymenttransactionstate/purchased.md) or [SKPaymentTransactionStateRestored](../skpaymenttransactionstate/restored.md). The [transactionIdentifier](transactionidentifier.md) is a string that uniquely identifies an interaction between the user’s device and the App Store, such as a purchase or restore.

This value has the same format as the transaction’s [transaction_id](../../appstorereceipts/transaction_id.md) in the receipt; however, the values may not be the same.

## See Also

### Getting Transaction Information

- [payment](payment.md) — The payment for the transaction. _(deprecated)_
- [transactionDate](transactiondate.md) — The date the transaction was added to the App Store’s payment queue. _(deprecated)_
- [originalTransaction](original.md) — The transaction that was restored by the App Store. _(deprecated)_
- [error](error.md) — An object describing the error that occurred while processing the transaction. _(deprecated)_
- [transactionReceipt](transactionreceipt.md) — A signed receipt that records all information about a successful payment transaction. _(deprecated)_

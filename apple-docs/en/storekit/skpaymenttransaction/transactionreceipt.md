---
title: transactionReceipt
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS（18.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skpaymenttransaction/transactionreceipt
source_url: 'https://developer.apple.com/documentation/storekit/skpaymenttransaction/transactionreceipt'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymenttransaction/transactionreceipt.json'
content_hash: 'sha256:fb2de768ff39d8d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentTransaction](../skpaymenttransaction.md)

# transactionReceipt

<sub>Instance Property</sub>

A signed receipt that records all information about a successful payment transaction.

> [!warning] Deprecated
> Use the app receipt instead, as described in [Receipt Validation Programming Guide](https://developer.apple.com/library/archive/releasenotes/General/ValidateAppStoreReceipt/Introduction.html#//apple_ref/doc/uid/TP40010573).

<sub>tvOS</sub>

```swift
var transactionReceipt: Data? { get }
```

## Discussion

The contents of this property are undefined except when [transactionState](transactionstate.md) is set to [SKPaymentTransactionStatePurchased](../skpaymenttransactionstate/purchased.md).

The receipt is a signed chunk of data that can be sent to the App Store to verify that the payment was successfully processed. This is most useful when designing a store that uses a server separate from the iPhone to verify that payment was processed. For more information on verifying receipts, see [Receipt Validation Programming Guide](https://developer.apple.com/library/archive/releasenotes/General/ValidateAppStoreReceipt/Introduction.html#//apple_ref/doc/uid/TP40010573).

## See Also

### Getting Transaction Information

- [payment](payment.md) — The payment for the transaction. _(deprecated)_
- [transactionIdentifier](transactionidentifier.md) — A string that uniquely identifies a successful payment transaction. _(deprecated)_
- [transactionDate](transactiondate.md) — The date the transaction was added to the App Store’s payment queue. _(deprecated)_
- [originalTransaction](original.md) — The transaction that was restored by the App Store. _(deprecated)_
- [error](error.md) — An object describing the error that occurred while processing the transaction. _(deprecated)_

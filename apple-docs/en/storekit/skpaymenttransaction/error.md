---
title: error
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skpaymenttransaction/error
source_url: 'https://developer.apple.com/documentation/storekit/skpaymenttransaction/error'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymenttransaction/error.json'
content_hash: 'sha256:22480c77f1f7083f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentTransaction](../skpaymenttransaction.md)

# error

<sub>Instance Property</sub>

An object describing the error that occurred while processing the transaction.

> [!warning] Deprecated
> Use PurchaseResult from Product.purchase(confirmIn:options:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var error: (any Error)? { get }
```

## Discussion

The [error](error.md) property is undefined except when [transactionState](transactionstate.md) is set to [SKPaymentTransactionStateFailed](../skpaymenttransactionstate/failed.md). Your application can read the [error](error.md) property to determine why the transaction failed. For a list of error constants, see SKErrorDomain in `StoreKit Constants`.

## See Also

### Related Documentation

- [In-App Purchase Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267)

### Getting Transaction Information

- [payment](payment.md) — The payment for the transaction. _(deprecated)_
- [transactionIdentifier](transactionidentifier.md) — A string that uniquely identifies a successful payment transaction. _(deprecated)_
- [transactionDate](transactiondate.md) — The date the transaction was added to the App Store’s payment queue. _(deprecated)_
- [originalTransaction](original.md) — The transaction that was restored by the App Store. _(deprecated)_
- [transactionReceipt](transactionreceipt.md) — A signed receipt that records all information about a successful payment transaction. _(deprecated)_

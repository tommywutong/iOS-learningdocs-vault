---
title: SKPaymentTransaction
framework: StoreKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skpaymenttransaction
source_url: 'https://developer.apple.com/documentation/storekit/skpaymenttransaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymenttransaction.json'
content_hash: 'sha256:a6c46782e3dddb31'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKPaymentTransaction

<sub>Class</sub>

An object in the payment queue.

> [!warning] Deprecated
> Use PurchaseResult from Product.purchase(confirmIn:options:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class SKPaymentTransaction
```

## Overview

A payment transaction is created whenever a payment is added to the payment queue. The system delivers transactions to your app when the App Store finishes processing the payment. Completed transactions provide a receipt and transaction identifier that your app can use to save a permanent record of the processed payment.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting Transaction Information

- [payment](skpaymenttransaction/payment.md) — The payment for the transaction. _(deprecated)_
- [transactionIdentifier](skpaymenttransaction/transactionidentifier.md) — A string that uniquely identifies a successful payment transaction. _(deprecated)_
- [transactionDate](skpaymenttransaction/transactiondate.md) — The date the transaction was added to the App Store’s payment queue. _(deprecated)_
- [originalTransaction](skpaymenttransaction/original.md) — The transaction that was restored by the App Store. _(deprecated)_
- [error](skpaymenttransaction/error.md) — An object describing the error that occurred while processing the transaction. _(deprecated)_
- [transactionReceipt](skpaymenttransaction/transactionreceipt.md) — A signed receipt that records all information about a successful payment transaction. _(deprecated)_

### Getting Downloads

- [downloads](skpaymenttransaction/downloads.md) — An array of download objects representing the downloadable content associated with the transaction. _(deprecated)_

### Getting Transaction State

- [transactionState](skpaymenttransaction/transactionstate.md) — The current state of the transaction. _(deprecated)_
- [SKPaymentTransactionState](skpaymenttransactionstate.md) — Values representing the state of a transaction. _(deprecated)_

## See Also

### Purchases

- [Requesting a payment from the App Store](requesting-a-payment-from-the-app-store.md) — Submit a payment request to the App Store when a customer selects a product to buy.
- [Processing a transaction](processing-a-transaction.md) — Register a transaction queue observer to get and handle transaction updates from the App Store.
- [SKPayment](skpayment.md) — A request to the App Store to process payment for additional functionality that your app offers. _(deprecated)_
- [SKMutablePayment](skmutablepayment.md) — A mutable request to the App Store to process payment for additional functionality that your app offers. _(deprecated)_

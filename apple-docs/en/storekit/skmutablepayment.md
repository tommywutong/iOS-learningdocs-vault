---
title: SKMutablePayment
framework: StoreKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skmutablepayment
source_url: 'https://developer.apple.com/documentation/storekit/skmutablepayment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skmutablepayment.json'
content_hash: 'sha256:e518e3d783736db4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKMutablePayment

<sub>Class</sub>

A mutable request to the App Store to process payment for additional functionality that your app offers.

> [!warning] Deprecated
> Use Product.purchase(confirmIn:options:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class SKMutablePayment
```

## Overview

A mutable payment object identifies a product and the quantity of that item the user would like to purchase.

When a mutable payment is added to the payment queue, the payment queue copies the contents into an immutable request before queueing the request. Your app can safely change the contents of the mutable payment object.

## Relationships

- **Inherits From**: [SKPayment](skpayment.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSMutableCopying](../foundation/nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting and Setting Attributes

- [productIdentifier](skmutablepayment/productidentifier.md) — A string that identifies a product that can be purchased from within your app. _(deprecated)_
- [quantity](skmutablepayment/quantity.md) — The number of items the user wants to purchase. _(deprecated)_
- [requestData](skmutablepayment/requestdata.md) — Reserved for future use. _(deprecated)_
- [applicationUsername](skmutablepayment/applicationusername.md) — A string that associates the transaction with a user account on your service. _(deprecated)_

### Simulating Buy for Testing

- [simulatesAskToBuyInSandbox](skmutablepayment/simulatesasktobuyinsandbox.md) — A Boolean value that produces an “ask to buy” flow for this payment in the sandbox. _(deprecated)_

### Getting and Setting Discount Details

- [paymentDiscount](skmutablepayment/paymentdiscount.md) — The details of the discount offer to apply to the payment. _(deprecated)_

## See Also

### Purchases

- [Requesting a payment from the App Store](requesting-a-payment-from-the-app-store.md) — Submit a payment request to the App Store when a customer selects a product to buy.
- [Processing a transaction](processing-a-transaction.md) — Register a transaction queue observer to get and handle transaction updates from the App Store.
- [SKPayment](skpayment.md) — A request to the App Store to process payment for additional functionality that your app offers. _(deprecated)_
- [SKPaymentTransaction](skpaymenttransaction.md) — An object in the payment queue. _(deprecated)_

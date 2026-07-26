---
title: SKPayment
framework: StoreKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skpayment
source_url: 'https://developer.apple.com/documentation/storekit/skpayment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpayment.json'
content_hash: 'sha256:01e1b0ff9723f90a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKPayment

<sub>Class</sub>

A request to the App Store to process payment for additional functionality that your app offers.

> [!warning] Deprecated
> Use Product.purchase(confirmIn:options:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class SKPayment
```

## Overview

A payment object identifies a product and the quantity of those items the user would like to purchase.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [SKMutablePayment](skmutablepayment.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSMutableCopying](../foundation/nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating Payments

- [+ paymentWithProduct:](<skpayment/init(product_).md>) — Returns a new payment for the specified product. _(deprecated)_

### Getting Payment Details

- [productIdentifier](skpayment/productidentifier.md) — A string used to identify a product that can be purchased from within your app. _(deprecated)_
- [quantity](skpayment/quantity.md) — The number of items the user wants to purchase. _(deprecated)_
- [requestData](skpayment/requestdata.md) — Reserved for future use. _(deprecated)_
- [applicationUsername](skpayment/applicationusername.md) — A string that associates the transaction with a user account on your service. _(deprecated)_

### Simulating Purchases for Testing

- [simulatesAskToBuyInSandbox](skpayment/simulatesasktobuyinsandbox.md) — A Boolean value that produces an “ask to buy” flow for this payment in the sandbox. _(deprecated)_

### Getting Discount Details

- [paymentDiscount](skpayment/paymentdiscount.md) — The details of the discount offer to apply to the payment. _(deprecated)_
- [SKPaymentDiscount](skpaymentdiscount.md) — The signed discount to apply to a payment. _(deprecated)_

## See Also

### Purchases

- [Requesting a payment from the App Store](requesting-a-payment-from-the-app-store.md) — Submit a payment request to the App Store when a customer selects a product to buy.
- [Processing a transaction](processing-a-transaction.md) — Register a transaction queue observer to get and handle transaction updates from the App Store.
- [SKMutablePayment](skmutablepayment.md) — A mutable request to the App Store to process payment for additional functionality that your app offers. _(deprecated)_
- [SKPaymentTransaction](skpaymenttransaction.md) — An object in the payment queue. _(deprecated)_

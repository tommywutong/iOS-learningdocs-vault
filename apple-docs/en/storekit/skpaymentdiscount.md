---
title: SKPaymentDiscount
framework: StoreKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 12.2+（18.0 起废弃）, iPadOS 12.2+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.14.4+（15.0 起废弃）, tvOS 12.2+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skpaymentdiscount
source_url: 'https://developer.apple.com/documentation/storekit/skpaymentdiscount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymentdiscount.json'
content_hash: 'sha256:6288fcd5f4e3627b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKPaymentDiscount

<sub>Class</sub>

The signed discount to apply to a payment.

> [!warning] Deprecated
> Create a Product.PurchaseOption.promotionalOffer to use in Product.purchase(confirmIn:options:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class SKPaymentDiscount
```

## Overview

The [SKPaymentDiscount](skpaymentdiscount.md) contains the details of a promotional offer discount that you want to apply to a [SKMutablePayment](skmutablepayment.md).

Include the signature that you generated in this object. For guidance, see [Generating a signature for promotional offers](generating-a-signature-for-promotional-offers.md). The App Store uses this signature and the parameters to validate the promotional offer. Keep in mind that the signature must correspond to the parameters in the payment for a transaction to be successful.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializing a Payment Discount

- [- initWithIdentifier:keyIdentifier:nonce:signature:timestamp:](<skpaymentdiscount/init(identifier_keyidentifier_nonce_signature_timestamp_).md>) — Initializes the payment discount with a signature and the parameters used by the signature. _(deprecated)_

### Identifying the Discount

- [identifier](skpaymentdiscount/identifier.md) — A string used to uniquely identify a discount offer for a product. _(deprecated)_
- [keyIdentifier](skpaymentdiscount/keyidentifier.md) — A string that identifies the key used to generate the signature. _(deprecated)_

### Validating the Discount

- [nonce](skpaymentdiscount/nonce.md) — A universally unique ID (UUID) value that you define. _(deprecated)_
- [signature](skpaymentdiscount/signature.md) — A string representing the properties of a specific promotional offer, cryptographically signed. _(deprecated)_
- [timestamp](skpaymentdiscount/timestamp.md) — The date and time of the signature’s creation in milliseconds, formatted in Unix epoch time. _(deprecated)_

## See Also

### Getting Discount Details

- [paymentDiscount](skpayment/paymentdiscount.md) — The details of the discount offer to apply to the payment. _(deprecated)_

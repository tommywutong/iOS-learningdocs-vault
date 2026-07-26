---
title: signature
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.2+（18.0 起废弃）, iPadOS 12.2+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.14.4+（15.0 起废弃）, tvOS 12.2+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skpaymentdiscount/signature
source_url: 'https://developer.apple.com/documentation/storekit/skpaymentdiscount/signature'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymentdiscount/signature.json'
content_hash: 'sha256:5903e486c578b2a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentDiscount](../skpaymentdiscount.md)

# signature

<sub>Instance Property</sub>

A string representing the properties of a specific promotional offer, cryptographically signed.

> [!warning] Deprecated
> Create a Product.PurchaseOption.promotionalOffer to use in Product.purchase(confirmIn:options:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var signature: String { get }
```

## Discussion

The [signature](signature.md) is a string signed with your private key that represents the properties of a specific promotional offer. To keep your private key secure, generate the [signature](signature.md) on a server.

Generate the [signature](signature.md) using the Elliptic Curve Digital Signature Algorithm (ECDSA) with SHA 256. For more information, see [Generating a signature for promotional offers](../generating-a-signature-for-promotional-offers.md).

## See Also

### Validating the Discount

- [nonce](nonce.md) — A universally unique ID (UUID) value that you define. _(deprecated)_
- [timestamp](timestamp.md) — The date and time of the signature’s creation in milliseconds, formatted in Unix epoch time. _(deprecated)_

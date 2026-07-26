---
title: nonce
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.2+（18.0 起废弃）, iPadOS 12.2+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.14.4+（15.0 起废弃）, tvOS 12.2+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skpaymentdiscount/nonce
source_url: 'https://developer.apple.com/documentation/storekit/skpaymentdiscount/nonce'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymentdiscount/nonce.json'
content_hash: 'sha256:7cdd6ae7f6d667fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentDiscount](../skpaymentdiscount.md)

# nonce

<sub>Instance Property</sub>

A universally unique ID (UUID) value that you define.

> [!warning] Deprecated
> Create a Product.PurchaseOption.promotionalOffer to use in Product.purchase(confirmIn:options:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var nonce: UUID { get }
```

## Discussion

Your server generates a unique [nonce](nonce.md) when it creates the [signature](signature.md) string for the payment discount. The string representation of the [nonce](nonce.md) must be lowercase.

You can use a [nonce](nonce.md) one time; generate a new one for every buy request.

## See Also

### Validating the Discount

- [signature](signature.md) — A string representing the properties of a specific promotional offer, cryptographically signed. _(deprecated)_
- [timestamp](timestamp.md) — The date and time of the signature’s creation in milliseconds, formatted in Unix epoch time. _(deprecated)_

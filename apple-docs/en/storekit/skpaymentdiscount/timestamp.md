---
title: timestamp
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.2+（18.0 起废弃）, iPadOS 12.2+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.14.4+（15.0 起废弃）, tvOS 12.2+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skpaymentdiscount/timestamp
source_url: 'https://developer.apple.com/documentation/storekit/skpaymentdiscount/timestamp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymentdiscount/timestamp.json'
content_hash: 'sha256:844fef3e60643359'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentDiscount](../skpaymentdiscount.md)

# timestamp

<sub>Instance Property</sub>

The date and time of the signature’s creation in milliseconds, formatted in Unix epoch time.

> [!warning] Deprecated
> Create a Product.PurchaseOption.promotionalOffer to use in Product.purchase(confirmIn:options:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var timestamp: NSNumber { get }
```

## Discussion

The [timestamp](timestamp.md) keeps the payment discount active for 24 hours.

## See Also

### Validating the Discount

- [nonce](nonce.md) — A universally unique ID (UUID) value that you define. _(deprecated)_
- [signature](signature.md) — A string representing the properties of a specific promotional offer, cryptographically signed. _(deprecated)_

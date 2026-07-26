---
title: identifier
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.2+（18.0 起废弃）, iPadOS 12.2+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.14.4+（15.0 起废弃）, tvOS 12.2+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skpaymentdiscount/identifier
source_url: 'https://developer.apple.com/documentation/storekit/skpaymentdiscount/identifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymentdiscount/identifier.json'
content_hash: 'sha256:01a2343546b91eed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentDiscount](../skpaymentdiscount.md)

# identifier

<sub>Instance Property</sub>

A string used to uniquely identify a discount offer for a product.

> [!warning] Deprecated
> Create a Product.PurchaseOption.promotionalOffer to use in Product.purchase(confirmIn:options:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var identifier: String { get }
```

## Discussion

You set up offers and their identifiers in App Store Connect. If the [identifier](identifier.md) is not valid, an [SKErrorInvalidOfferIdentifier](../skerror/code/invalidofferidentifier.md) error can result.

## See Also

### Identifying the Discount

- [keyIdentifier](keyidentifier.md) — A string that identifies the key used to generate the signature. _(deprecated)_

---
title: keyIdentifier
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.2+（18.0 起废弃）, iPadOS 12.2+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.14.4+（15.0 起废弃）, tvOS 12.2+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skpaymentdiscount/keyidentifier
source_url: 'https://developer.apple.com/documentation/storekit/skpaymentdiscount/keyidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymentdiscount/keyidentifier.json'
content_hash: 'sha256:10ac703e8af6c1a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentDiscount](../skpaymentdiscount.md)

# keyIdentifier

<sub>Instance Property</sub>

A string that identifies the key used to generate the signature.

> [!warning] Deprecated
> Create a Product.PurchaseOption.promotionalOffer to use in Product.purchase(confirmIn:options:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var keyIdentifier: String { get }
```

## Discussion

You generate and download keys from App Store Connect. See the “KEY ID” column in App Store Connect to use as the [keyIdentifier](keyidentifier.md).

## See Also

### Identifying the Discount

- [identifier](identifier.md) — A string used to uniquely identify a discount offer for a product. _(deprecated)_

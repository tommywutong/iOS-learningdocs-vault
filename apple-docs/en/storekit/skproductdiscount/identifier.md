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
doc_path: /documentation/storekit/skproductdiscount/identifier
source_url: 'https://developer.apple.com/documentation/storekit/skproductdiscount/identifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproductdiscount/identifier.json'
content_hash: 'sha256:5d71ad72a600442f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKProductDiscount](../skproductdiscount.md)

# identifier

<sub>Instance Property</sub>

A string used to uniquely identify a discount offer for a product.

> [!warning] Deprecated
> Use Product.SubscriptionOffer.id.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var identifier: String? { get }
```

## Discussion

You set up offers and their identifiers in App Store Connect.

## See Also

### Identifying the Discount

- [type](type-swift.property.md) — The type of discount offer. _(deprecated)_
- [Type](type-swift.enum.md) — Values representing the types of discount offers an app can present. _(deprecated)_

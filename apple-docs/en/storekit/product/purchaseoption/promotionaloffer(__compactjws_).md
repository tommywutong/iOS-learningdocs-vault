---
title: 'promotionalOffer(_:compactJWS:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/product/purchaseoption/promotionaloffer(_:compactjws:)'
source_url: 'https://developer.apple.com/documentation/storekit/product/purchaseoption/promotionaloffer(_:compactjws:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/purchaseoption/promotionaloffer%28_%3Acompactjws%3A%29.json'
content_hash: 'sha256:01df77c0ad8684e1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [PurchaseOption](../purchaseoption.md)

# promotionalOffer(_:compactJWS:)

<sub>Type Method</sub>

Apply a promotional offer to a purchase.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: iOS 26.0, macOS 26.0, tvOS 26.0, watchOS 26.0, visionOS 26.0)
static func promotionalOffer(_ offerID: String, compactJWS: String) -> [Product.PurchaseOption]
```

## Parameters

- `offerID` — The `id` property of the `SubscriptionOffer` to apply.

- `compactJWS` — The JWS signature used to validate a promotional offer.

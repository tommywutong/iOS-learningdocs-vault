---
title: 'quantity(_:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/product/purchaseoption/quantity(_:)'
source_url: 'https://developer.apple.com/documentation/storekit/product/purchaseoption/quantity(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/purchaseoption/quantity%28_%3A%29.json'
content_hash: 'sha256:9f6476e3448c31e8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [PurchaseOption](../purchaseoption.md)

# quantity(_:)

<sub>Type Method</sub>

Indicates the quantity of items the customer is purchasing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func quantity(_ quantity: Int) -> Product.PurchaseOption
```

## Parameters

- `quantity` — The number of items the customer is purchasing. The default value is 1. The maximum value is 10.

## Return Value

An instance of [PurchaseOption](../purchaseoption.md) to use in [purchase(options:)](<../purchase(options_).md>).

## Discussion

The quantity applies to consumable in-app purchases and non-renewing subscriptions.

## See Also

### Setting the purchase options

- [appAccountToken(_:)](<appaccounttoken(__).md>) — Sets a UUID to associate the purchase with an account in your system.
- [winBackOffer(_:)](<winbackoffer(__).md>) — Sets a win-back offer to apply to the purchase.
- [promotionalOffer(offerID:keyID:nonce:signature:timestamp:)](<promotionaloffer(offerid_keyid_nonce_signature_timestamp_).md>) — Applies a promotional offer for an auto-renewable subscription. _(deprecated)_
- [promotionalOffer(offerID:signature:)](<promotionaloffer(offerid_signature_).md>) _(deprecated)_

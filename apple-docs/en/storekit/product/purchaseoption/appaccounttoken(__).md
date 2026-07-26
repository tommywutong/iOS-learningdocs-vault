---
title: 'appAccountToken(_:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/product/purchaseoption/appaccounttoken(_:)'
source_url: 'https://developer.apple.com/documentation/storekit/product/purchaseoption/appaccounttoken(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/purchaseoption/appaccounttoken%28_%3A%29.json'
content_hash: 'sha256:f97c1254a9ae8182'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [PurchaseOption](../purchaseoption.md)

# appAccountToken(_:)

<sub>Type Method</sub>

Sets a UUID to associate the purchase with an account in your system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func appAccountToken(_ token: UUID) -> Product.PurchaseOption
```

## Parameters

- `token` — A UUID you provide to associate with the purchase.

## Return Value

An instance of [PurchaseOption](../purchaseoption.md) to use in [purchase(options:)](<../purchase(options_).md>).

## Discussion

When you set the app account token in the purchase options, the App Store returns the same app account token value in the resulting transaction, in [appAccountToken](../../transaction/appaccounttoken.md).

## See Also

### Setting the purchase options

- [winBackOffer(_:)](<winbackoffer(__).md>) — Sets a win-back offer to apply to the purchase.
- [promotionalOffer(offerID:keyID:nonce:signature:timestamp:)](<promotionaloffer(offerid_keyid_nonce_signature_timestamp_).md>) — Applies a promotional offer for an auto-renewable subscription. _(deprecated)_
- [promotionalOffer(offerID:signature:)](<promotionaloffer(offerid_signature_).md>) _(deprecated)_
- [quantity(_:)](<quantity(__).md>) — Indicates the quantity of items the customer is purchasing.

---
title: 'promotionalOffer(offerID:signature:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.4+（26.0 起废弃）, iPadOS 17.4+（26.0 起废弃）, macOS 14.4+（26.0 起废弃）, tvOS 17.4+（26.0 起废弃）, visionOS 1.1+（26.0 起废弃）, watchOS 10.4+（26.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/storekit/product/purchaseoption/promotionaloffer(offerid:signature:)'
source_url: 'https://developer.apple.com/documentation/storekit/product/purchaseoption/promotionaloffer(offerid:signature:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/purchaseoption/promotionaloffer%28offerid%3Asignature%3A%29.json'
content_hash: 'sha256:eff977e3e2e2a56c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [PurchaseOption](../purchaseoption.md)

# promotionalOffer(offerID:signature:)

<sub>Type Method</sub>

> [!warning] Deprecated
> Sign promotional offers with JWS and use promotionalOffer(_:compactJWS:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func promotionalOffer(offerID: String, signature: Product.SubscriptionOffer.Signature) -> Product.PurchaseOption
```

## See Also

### Setting the purchase options

- [appAccountToken(_:)](<appaccounttoken(__).md>) — Sets a UUID to associate the purchase with an account in your system.
- [winBackOffer(_:)](<winbackoffer(__).md>) — Sets a win-back offer to apply to the purchase.
- [promotionalOffer(offerID:keyID:nonce:signature:timestamp:)](<promotionaloffer(offerid_keyid_nonce_signature_timestamp_).md>) — Applies a promotional offer for an auto-renewable subscription. _(deprecated)_
- [quantity(_:)](<quantity(__).md>) — Indicates the quantity of items the customer is purchasing.

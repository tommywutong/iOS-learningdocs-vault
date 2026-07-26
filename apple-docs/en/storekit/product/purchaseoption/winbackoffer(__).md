---
title: 'winBackOffer(_:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/product/purchaseoption/winbackoffer(_:)'
source_url: 'https://developer.apple.com/documentation/storekit/product/purchaseoption/winbackoffer(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/purchaseoption/winbackoffer%28_%3A%29.json'
content_hash: 'sha256:b83b22d064777e37'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [PurchaseOption](../purchaseoption.md)

# winBackOffer(_:)

<sub>Type Method</sub>

Sets a win-back offer to apply to the purchase.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func winBackOffer(_ offer: Product.SubscriptionOffer) -> Product.PurchaseOption
```

## Parameters

- `offer` — The [SubscriptionOffer](../subscriptionoffer.md) instance that represents the win-back offer to apply to the purchase.

## Discussion

To test win-back offers in Xcode, set up the offers in your StoreKit configuration file. For more information, see [Setting up StoreKit Testing in Xcode](../../../xcode/setting-up-storekit-testing-in-xcode.md).

## See Also

### Setting the purchase options

- [appAccountToken(_:)](<appaccounttoken(__).md>) — Sets a UUID to associate the purchase with an account in your system.
- [promotionalOffer(offerID:keyID:nonce:signature:timestamp:)](<promotionaloffer(offerid_keyid_nonce_signature_timestamp_).md>) — Applies a promotional offer for an auto-renewable subscription. _(deprecated)_
- [promotionalOffer(offerID:signature:)](<promotionaloffer(offerid_signature_).md>) _(deprecated)_
- [quantity(_:)](<quantity(__).md>) — Indicates the quantity of items the customer is purchasing.

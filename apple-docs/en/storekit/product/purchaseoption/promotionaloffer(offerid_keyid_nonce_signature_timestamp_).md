---
title: 'promotionalOffer(offerID:keyID:nonce:signature:timestamp:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+（26.0 起废弃）, iPadOS 15.0+（26.0 起废弃）, macOS 12.0+（26.0 起废弃）, tvOS 15.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）, watchOS 8.0+（26.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/storekit/product/purchaseoption/promotionaloffer(offerid:keyid:nonce:signature:timestamp:)'
source_url: 'https://developer.apple.com/documentation/storekit/product/purchaseoption/promotionaloffer(offerid:keyid:nonce:signature:timestamp:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/purchaseoption/promotionaloffer%28offerid%3Akeyid%3Anonce%3Asignature%3Atimestamp%3A%29.json'
content_hash: 'sha256:4d2e086f8fd55500'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [PurchaseOption](../purchaseoption.md)

# promotionalOffer(offerID:keyID:nonce:signature:timestamp:)

<sub>Type Method</sub>

Applies a promotional offer for an auto-renewable subscription.

> [!warning] Deprecated
> Sign promotional offers with JWS and use promotionalOffer(_:compactJWS:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func promotionalOffer(offerID: String, keyID: String, nonce: UUID, signature: Data, timestamp: Int) -> Product.PurchaseOption
```

## Parameters

- `offerID` — The subscription-offer identifier, [id](../subscriptionoffer/id.md).

- `keyID` — The key ID of the subscription key.

- `nonce` — The antireplay value used in the signature. Use lowercase.

- `signature` — The cryptographic signature of the offer parameters, which you generate on your server.

- `timestamp` — The UNIX time, in milliseconds, when you generate the signature.

## Return Value

An instance of [PurchaseOption](../purchaseoption.md) to use in [purchase(options:)](<../purchase(options_).md>).

## Discussion

For information about `keyID`, `nonce`, `signature`, and `timestamp`, see [Generating a signature for promotional offers](../../generating-a-signature-for-promotional-offers.md). If you’re providing an [appAccountToken(_:)](<appaccounttoken(__).md>) in the purchase options, you must include that value when you generate the `signature`. Use lowercase for the UUID string representations of the app account token and the `nonce` in the signature.

You can offer a discounted or free period of service for auto-renewable subscriptions on iOS, iPadOS, macOS, and tvOS using promotional offers. Before you can provide promotional offers in your app, you must set up the offers in your App Store Connect account. To configure your offer, see [Set up promotional offers for auto-renewable subscriptions](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-promotional-offers-for-auto-renewable-subscriptions).

## See Also

### Setting the purchase options

- [appAccountToken(_:)](<appaccounttoken(__).md>) — Sets a UUID to associate the purchase with an account in your system.
- [winBackOffer(_:)](<winbackoffer(__).md>) — Sets a win-back offer to apply to the purchase.
- [promotionalOffer(offerID:signature:)](<promotionaloffer(offerid_signature_).md>) _(deprecated)_
- [quantity(_:)](<quantity(__).md>) — Indicates the quantity of items the customer is purchasing.

---
title: 'subscriptionPromotionalOffer(offer:signature:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.4+（26.0 起废弃）, iPadOS 17.4+（26.0 起废弃）, macOS 14.4+（26.0 起废弃）, tvOS 17.4+（26.0 起废弃）, visionOS 1.1+（26.0 起废弃）, watchOS 10.4+（26.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/subscriptionpromotionaloffer(offer:signature:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/subscriptionpromotionaloffer(offer:signature:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/subscriptionpromotionaloffer%28offer%3Asignature%3A%29.json'
content_hash: 'sha256:275c2f21d20f65d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# subscriptionPromotionalOffer(offer:signature:)

<sub>Instance Method</sub>

Selects a promotional offer to apply to a purchase a customer makes from a subscription store view.

> [!warning] Deprecated
> Sign promotional offers with JWS and use the [subscriptionPromotionalOffer(offer:compactJWS:)](<subscriptionpromotionaloffer(offer_compactjws_).md>) view modifier instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func subscriptionPromotionalOffer(offer: @escaping (Product, Product.SubscriptionInfo) -> Product.SubscriptionOffer?, signature: @escaping (Product, Product.SubscriptionInfo, Product.SubscriptionOffer) async throws -> Product.SubscriptionOffer.Signature) -> some View

```

## Parameters

- `offer` — The system calls this function before drawing the given subscription product on the subscription store view. Return the promotional offer to apply to the product, if any, to have system-provided UI reflect the discounted terms under the selected offer.

- `signature` — The system calls this function before processing a purchase, with the product to be purchased provided as a parameter, along with the selected subscription offer to be applied to the purchase. Return a signature you generate on your server that validates the selected offer. Errors thrown from this closure will be surfaced via the [onInAppPurchaseCompletion(perform:)](<oninapppurchasecompletion(perform_).md>) modifier. For information about generating the signature, see [Generating a signature for promotional offers](../../storekit/generating-a-signature-for-promotional-offers.md).

## Discussion

Subscription stores within this view uses the specified subscription offer to configure the appearance of the subscription plans displayed, when you use a system-provided [SubscriptionStoreControlStyle](../../storekit/subscriptionstorecontrolstyle.md) to style the in-app subscription store. Standard [ProductViewStyle](../../storekit/productviewstyle.md) instances don’t show introductory or promotional offers in UI. Use the [SubscriptionStoreView](../../storekit/subscriptionstoreview.md) instead to show these offers in the UI.

If the signature passes validation for the offer you select, the system applies the offer to the purchase. If the signature fails validation for the offer you select, the purchase fails with [Product.PurchaseError.invalidOfferSignature](../../storekit/product/purchaseerror/invalidoffersignature.md).

Promotional offers you select in this modifier overwrite any offers you specified in ancestor views.

## See Also

### Technology-specific modifiers

- [postToPhotosSharedAlbumSheet(isPresented:items:photoLibrary:defaultAlbumIdentifier:completion:)](<posttophotossharedalbumsheet(ispresented_items_photolibrary_defaultalbumidentifier_completion_).md>) — Presents an “Add to Shared Album” sheet that allows the user to post the given items to a shared album. _(deprecated)_
- [offerCodeRedemption(isPresented:onCompletion:)](<offercoderedemption(ispresented_oncompletion_).md>) _(deprecated)_

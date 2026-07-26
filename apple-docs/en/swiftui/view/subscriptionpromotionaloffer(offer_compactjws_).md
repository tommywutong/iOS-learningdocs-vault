---
title: 'subscriptionPromotionalOffer(offer:compactJWS:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/subscriptionpromotionaloffer(offer:compactjws:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/subscriptionpromotionaloffer(offer:compactjws:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/subscriptionpromotionaloffer%28offer%3Acompactjws%3A%29.json'
content_hash: 'sha256:82f830246ee198f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# subscriptionPromotionalOffer(offer:compactJWS:)

<sub>Instance Method</sub>

Selects a promotional offer to apply to a purchase a customer makes from a subscription store view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func subscriptionPromotionalOffer(offer: @escaping (Product, Product.SubscriptionInfo) -> Product.SubscriptionOffer?, compactJWS: @escaping (Product, Product.SubscriptionInfo, Product.SubscriptionOffer) async throws -> String) -> some View

```

## Parameters

- `offer` — The system calls this function before drawing the given subscription product on the subscription store view. Return the promotional offer to apply to the product, if any, to have system-provided UI reflect the discounted terms under the selected offer.

- `compactJWS` — The system calls this function before processing a purchase, with the product to be purchased provided as a parameter, along with the selected subscription offer to be applied to the purchase. Return a compact JWS signature you generate on your server that validates the selected offer. Errors thrown from this closure will be surfaced via the [onInAppPurchaseCompletion(perform:)](<oninapppurchasecompletion(perform_).md>) modifier. For information about generating the JWS signature, see [Generating JWS to sign App Store requests](../../storekit/generating-jws-to-sign-app-store-requests.md)..

## Discussion

Subscription stores within this view uses the specified subscription offer to configure the appearance of the subscription plans displayed, when you use a system-provided [SubscriptionStoreControlStyle](../../storekit/subscriptionstorecontrolstyle.md) to style the in-app subscription store. Standard [ProductViewStyle](../../storekit/productviewstyle.md) instances don’t show introductory or promotional offers in UI. Use the [SubscriptionStoreView](../../storekit/subscriptionstoreview.md) instead to show these offers in the UI.

If the signature passes validation for the offer you select, the system applies the offer to the purchase. If the signature fails validation for the offer you select, the purchase fails with [Product.PurchaseError.invalidOfferSignature](../../storekit/product/purchaseerror/invalidoffersignature.md).

Promotional offers you select in this modifier overwrite any offers you specified in ancestor views.

## See Also

### Interacting with the App Store and Apple Music

- [appStoreOverlay(isPresented:configuration:)](<appstoreoverlay(ispresented_configuration_).md>) — Presents a StoreKit overlay when a given condition is true.
- [manageSubscriptionsSheet(isPresented:)](<managesubscriptionssheet(ispresented_).md>)
- [refundRequestSheet(for:isPresented:onDismiss:)](<refundrequestsheet(for_ispresented_ondismiss_).md>) — Display the refund request sheet for the given transaction.
- [offerCodeRedemption(options:isPresented:onCompletion:)](<offercoderedemption(options_ispresented_oncompletion_).md>) — Presents a sheet that enables customers to redeem offer codes that you configure in App Store Connect. _(beta)_
- [musicPicker(isPresented:title:selection:)](<musicpicker(ispresented_title_selection_).md>) — Presents a music picker to select items from the Apple Music catalog and the user’s music library. _(beta)_
- [musicSubscriptionOffer(isPresented:options:onLoadCompletion:)](<musicsubscriptionoffer(ispresented_options_onloadcompletion_).md>) — Initiates the process of presenting a sheet with subscription offers for Apple Music when the `isPresented` binding is `true`.
- [currentEntitlementTask(for:priority:action:)](<currententitlementtask(for_priority_action_).md>) — Declares the view as dependent on the entitlement of an In-App Purchase product, and returns a modified view.
- [inAppPurchaseOptions(_:)](<inapppurchaseoptions(__).md>) — Add a function to call before initiating a purchase from StoreKit view within this view, providing a set of options for the purchase.
- [manageSubscriptionsSheet(isPresented:subscriptionGroupID:)](<managesubscriptionssheet(ispresented_subscriptiongroupid_).md>)
- [onInAppPurchaseCompletion(perform:)](<oninapppurchasecompletion(perform_).md>) — Add an action to perform when a purchase initiated from a StoreKit view within this view completes.
- [onInAppPurchaseStart(perform:)](<oninapppurchasestart(perform_).md>) — Add an action to perform when a user triggers the purchase button on a StoreKit view within this view.
- [productIconBorder()](<producticonborder().md>) — Adds a standard border to an in-app purchase product’s icon .
- [productViewStyle(_:)](<productviewstyle(__).md>) — Sets the style for In-App Purchase product views within a view.
- [productDescription(_:)](<productdescription(__).md>) — Configure the visibility of labels displaying an in-app purchase product description within the view.
- [storeButton(_:for:)](<storebutton(__for_).md>) — Specifies the visibility of auxiliary buttons that store view and subscription store view instances may use.

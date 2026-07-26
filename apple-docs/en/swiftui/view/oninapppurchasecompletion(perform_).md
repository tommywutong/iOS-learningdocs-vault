---
title: 'onInAppPurchaseCompletion(perform:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/oninapppurchasecompletion(perform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/oninapppurchasecompletion(perform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/oninapppurchasecompletion%28perform%3A%29.json'
content_hash: 'sha256:1548f7e5ea1db431'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onInAppPurchaseCompletion(perform:)

<sub>Instance Method</sub>

Add an action to perform when a purchase initiated from a StoreKit view within this view completes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func onInAppPurchaseCompletion(perform action: ((Product, Result<Product.PurchaseResult, any Error>) async -> ())?) -> some View

```

## Parameters

- `action` — The action to perform, with the product value and the purchase result provided as parameters.

## Discussion

By default, transactions from successful in-app store view purchases will be emitted from `Transaction.updates`. If the purchase fails with an error, an alert will be displayed. You can revert a view back to this behavior by providing `nil` for action.

Only one action will be performed for each purchase. Descendant views can override the action by using another [onInAppPurchaseCompletion(perform:)](<oninapppurchasecompletion(perform_).md>) modifier.

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
- [onInAppPurchaseStart(perform:)](<oninapppurchasestart(perform_).md>) — Add an action to perform when a user triggers the purchase button on a StoreKit view within this view.
- [productIconBorder()](<producticonborder().md>) — Adds a standard border to an in-app purchase product’s icon .
- [productViewStyle(_:)](<productviewstyle(__).md>) — Sets the style for In-App Purchase product views within a view.
- [productDescription(_:)](<productdescription(__).md>) — Configure the visibility of labels displaying an in-app purchase product description within the view.
- [storeButton(_:for:)](<storebutton(__for_).md>) — Specifies the visibility of auxiliary buttons that store view and subscription store view instances may use.
- [storeProductTask(for:priority:action:)](<storeproducttask(for_priority_action_).md>) — Declares the view as dependent on an In-App Purchase product and returns a modified view.

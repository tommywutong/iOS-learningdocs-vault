---
title: 'inAppPurchaseOptions(_:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/inapppurchaseoptions(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/inapppurchaseoptions(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/inapppurchaseoptions%28_%3A%29.json'
content_hash: 'sha256:d64f935958ce6429'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# inAppPurchaseOptions(_:)

<sub>Instance Method</sub>

Add a function to call before initiating a purchase from StoreKit view within this view, providing a set of options for the purchase.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func inAppPurchaseOptions(_ options: ((Product) async -> Set<Product.PurchaseOption>)?) -> some View

```

## Parameters

- `options` — The system calls this function before processing a purchase, with the product to  be purchased is provided as a parameter. Return a set of purchase options to add to the purchase.

## Discussion

In-app stores within this view will add any default purchase options to the set you return, and use the result for configuring the purchase. If you just want to react to in-app purchases beginning without adding purchase options, you can add an action with [onInAppPurchaseStart(perform:)](<oninapppurchasestart(perform_).md>).

You can remove any options ancestor views may have added by providing `nil` for the action. This will result in using the default set of purchase options.

## See Also

### Interacting with the App Store and Apple Music

- [appStoreOverlay(isPresented:configuration:)](<appstoreoverlay(ispresented_configuration_).md>) — Presents a StoreKit overlay when a given condition is true.
- [manageSubscriptionsSheet(isPresented:)](<managesubscriptionssheet(ispresented_).md>)
- [refundRequestSheet(for:isPresented:onDismiss:)](<refundrequestsheet(for_ispresented_ondismiss_).md>) — Display the refund request sheet for the given transaction.
- [offerCodeRedemption(options:isPresented:onCompletion:)](<offercoderedemption(options_ispresented_oncompletion_).md>) — Presents a sheet that enables customers to redeem offer codes that you configure in App Store Connect. _(beta)_
- [musicPicker(isPresented:title:selection:)](<musicpicker(ispresented_title_selection_).md>) — Presents a music picker to select items from the Apple Music catalog and the user’s music library. _(beta)_
- [musicSubscriptionOffer(isPresented:options:onLoadCompletion:)](<musicsubscriptionoffer(ispresented_options_onloadcompletion_).md>) — Initiates the process of presenting a sheet with subscription offers for Apple Music when the `isPresented` binding is `true`.
- [currentEntitlementTask(for:priority:action:)](<currententitlementtask(for_priority_action_).md>) — Declares the view as dependent on the entitlement of an In-App Purchase product, and returns a modified view.
- [manageSubscriptionsSheet(isPresented:subscriptionGroupID:)](<managesubscriptionssheet(ispresented_subscriptiongroupid_).md>)
- [onInAppPurchaseCompletion(perform:)](<oninapppurchasecompletion(perform_).md>) — Add an action to perform when a purchase initiated from a StoreKit view within this view completes.
- [onInAppPurchaseStart(perform:)](<oninapppurchasestart(perform_).md>) — Add an action to perform when a user triggers the purchase button on a StoreKit view within this view.
- [productIconBorder()](<producticonborder().md>) — Adds a standard border to an in-app purchase product’s icon .
- [productViewStyle(_:)](<productviewstyle(__).md>) — Sets the style for In-App Purchase product views within a view.
- [productDescription(_:)](<productdescription(__).md>) — Configure the visibility of labels displaying an in-app purchase product description within the view.
- [storeButton(_:for:)](<storebutton(__for_).md>) — Specifies the visibility of auxiliary buttons that store view and subscription store view instances may use.
- [storeProductTask(for:priority:action:)](<storeproducttask(for_priority_action_).md>) — Declares the view as dependent on an In-App Purchase product and returns a modified view.

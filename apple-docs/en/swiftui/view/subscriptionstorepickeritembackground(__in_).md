---
title: 'subscriptionStorePickerItemBackground(_:in:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/subscriptionstorepickeritembackground(_:in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/subscriptionstorepickeritembackground(_:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/subscriptionstorepickeritembackground%28_%3Ain%3A%29.json'
content_hash: 'sha256:9b414aa38f30db66'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# subscriptionStorePickerItemBackground(_:in:)

<sub>Instance Method</sub>

Sets the background shape and style for subscription store view picker items within a view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated func subscriptionStorePickerItemBackground(_ backgroundStyle: some ShapeStyle, in shape: some Shape) -> some View

```

## Parameters

- `backgroundStyle` — A [ShapeStyle](../shapestyle.md) that determines the background style for the subscription store view picker items.

- `shape` — An instance of a type that conforms to [Shape](../shape.md) and determines the shape of the subscription store view picker items. Omit the shape parameter to use the default shape.

## Discussion

Use this view modifier to customize the shape of the picker options in a subscription store view, as well as the background style.

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

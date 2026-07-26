---
title: 'refundRequestSheet(for:isPresented:onDismiss:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/refundrequestsheet(for:ispresented:ondismiss:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/refundrequestsheet(for:ispresented:ondismiss:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/refundrequestsheet%28for%3Aispresented%3Aondismiss%3A%29.json'
content_hash: 'sha256:596624e4aeb71e76'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# refundRequestSheet(for:isPresented:onDismiss:)

<sub>Instance Method</sub>

Display the refund request sheet for the given transaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@preconcurrency nonisolated func refundRequestSheet(for transactionID: Transaction.ID, isPresented: Binding<Bool>, onDismiss: (@MainActor (Result<Transaction.RefundRequestStatus, Transaction.RefundRequestError>) -> ())? = nil) -> some View

```

## Parameters

- `transactionID` — The transaction ID to request a refund for.

- `isPresented` — A binding to a Boolean value that determines whether the refund request sheet is presented.

- `onDismiss` — The closure to execute when dismissing the sheet, with the result of the refund request provided as a parameter.

## See Also

### Interacting with the App Store and Apple Music

- [appStoreOverlay(isPresented:configuration:)](<appstoreoverlay(ispresented_configuration_).md>) — Presents a StoreKit overlay when a given condition is true.
- [manageSubscriptionsSheet(isPresented:)](<managesubscriptionssheet(ispresented_).md>)
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
- [storeProductTask(for:priority:action:)](<storeproducttask(for_priority_action_).md>) — Declares the view as dependent on an In-App Purchase product and returns a modified view.

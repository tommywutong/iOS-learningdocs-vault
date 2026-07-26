---
title: 'currentEntitlementTask(for:priority:action:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/currententitlementtask(for:priority:action:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/currententitlementtask(for:priority:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/currententitlementtask%28for%3Apriority%3Aaction%3A%29.json'
content_hash: 'sha256:b285cbe3acfe67e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# currentEntitlementTask(for:priority:action:)

<sub>Instance Method</sub>

Declares the view as dependent on the entitlement of an In-App Purchase product, and returns a modified view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func currentEntitlementTask(for productID: String, priority: TaskPriority = .medium, action: @escaping (EntitlementTaskState<VerificationResult<Transaction>?>) async -> ()) -> some View

```

## Parameters

- `productID` — The product ID to get the entitlement for. The task restarts whenever this parameter changes.

- `priority` — The task priority to use when creating the task.

- `action` — The action to perform when the task’s state changes.

## Discussion

Before a view modified with this method appears, a task will start in the background to get the current entitlement. While the view is presented, the task will call `action` whenever the entitlement changes or the task’s state changes.

Consumable in-app purchases will always pass `nil` to `action`. For auto-renewable subscriptions, use `subscriptionStatusTask(for:priority:action:)` to get the full status information for the subscription.

## See Also

### Interacting with the App Store and Apple Music

- [appStoreOverlay(isPresented:configuration:)](<appstoreoverlay(ispresented_configuration_).md>) — Presents a StoreKit overlay when a given condition is true.
- [manageSubscriptionsSheet(isPresented:)](<managesubscriptionssheet(ispresented_).md>)
- [refundRequestSheet(for:isPresented:onDismiss:)](<refundrequestsheet(for_ispresented_ondismiss_).md>) — Display the refund request sheet for the given transaction.
- [offerCodeRedemption(options:isPresented:onCompletion:)](<offercoderedemption(options_ispresented_oncompletion_).md>) — Presents a sheet that enables customers to redeem offer codes that you configure in App Store Connect. _(beta)_
- [musicPicker(isPresented:title:selection:)](<musicpicker(ispresented_title_selection_).md>) — Presents a music picker to select items from the Apple Music catalog and the user’s music library. _(beta)_
- [musicSubscriptionOffer(isPresented:options:onLoadCompletion:)](<musicsubscriptionoffer(ispresented_options_onloadcompletion_).md>) — Initiates the process of presenting a sheet with subscription offers for Apple Music when the `isPresented` binding is `true`.
- [inAppPurchaseOptions(_:)](<inapppurchaseoptions(__).md>) — Add a function to call before initiating a purchase from StoreKit view within this view, providing a set of options for the purchase.
- [manageSubscriptionsSheet(isPresented:subscriptionGroupID:)](<managesubscriptionssheet(ispresented_subscriptiongroupid_).md>)
- [onInAppPurchaseCompletion(perform:)](<oninapppurchasecompletion(perform_).md>) — Add an action to perform when a purchase initiated from a StoreKit view within this view completes.
- [onInAppPurchaseStart(perform:)](<oninapppurchasestart(perform_).md>) — Add an action to perform when a user triggers the purchase button on a StoreKit view within this view.
- [productIconBorder()](<producticonborder().md>) — Adds a standard border to an in-app purchase product’s icon .
- [productViewStyle(_:)](<productviewstyle(__).md>) — Sets the style for In-App Purchase product views within a view.
- [productDescription(_:)](<productdescription(__).md>) — Configure the visibility of labels displaying an in-app purchase product description within the view.
- [storeButton(_:for:)](<storebutton(__for_).md>) — Specifies the visibility of auxiliary buttons that store view and subscription store view instances may use.
- [storeProductTask(for:priority:action:)](<storeproducttask(for_priority_action_).md>) — Declares the view as dependent on an In-App Purchase product and returns a modified view.

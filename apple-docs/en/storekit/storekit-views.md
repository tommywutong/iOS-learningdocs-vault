---
title: StoreKit views
framework: StoreKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/storekit-views
source_url: 'https://developer.apple.com/documentation/storekit/storekit-views'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/storekit-views.json'
content_hash: 'sha256:6fd60be5af5dc2a1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md) · [In-App Purchase](in-app-purchase.md)

# StoreKit views

<sub>API Collection</sub>

Display a customizable In-App Purchase store using StoreKit views for SwiftUI.

## Overview

The StoreKit views APIs provide UI to help you build a store for your In-App Purchases, and provide a way for customers to complete the purchase. The views support localization, so your customers see the product names, descriptions, and prices appropriate to their App Store storefront.

> [!note] Related session from WWDC23
> Session 10013: [Meet StoreKit for SwiftUI](https://developer.apple.com/videos/play/wwdc2023/10013)

StoreKit manages the layouts across all platforms, so the views look great on any device. You can use SwiftUI APIs to customize how the views integrate with your app.

To use StoreKit views, configure your In-App Purchase metadata in App Store Connect, or in a StoreKit configuration file in Xcode if you’re testing your app. Next, create the views using [StoreView](storeview.md), [ProductView](productview.md), or [SubscriptionStoreView](subscriptionstoreview.md). Finally, customize the default views to match your app by using your own icons, backgrounds, and other styling. Use [Previews in Xcode](../swiftui/previews-in-xcode.md) to see your progress as you iterate on your design.

For more information on configuring your In-App Purchase metadata, see [Manage In-App Purchases](https://help.apple.com/app-store-connect/#/devae49fb316). For more information on StoreKit configuration files in Xcode, see [Setting up StoreKit Testing in Xcode](../xcode/setting-up-storekit-testing-in-xcode.md).

## Topics

### Merchandising In-App Purchases, subscriptions, and offers

- [ProductView](productview.md) — A view that merchandises an individual In-App Purchase product.
- [StoreView](storeview.md) — A view that merchandises a collection of In-App Purchase products.
- [SubscriptionStoreView](subscriptionstoreview.md) — A view that merchandises a collection of auto-renewable subscription options that belong to the same subscription group.
- [SubscriptionOfferView](subscriptionofferview.md)
- [Backyard Birds: Building an app with SwiftData and widgets](../swiftui/backyard-birds-sample.md) — Create an app with persistent data, interactive widgets, and an all new in-app purchase experience.

### Styling product views

- [productViewStyle(_:)](<../swiftui/view/productviewstyle(__).md>) — Sets the style for In-App Purchase product views within a view.
- [productIconBorder()](<../swiftui/view/producticonborder().md>) — Adds a standard border to an in-app purchase product’s icon .
- [ProductViewStyle](productviewstyle.md) — A type that specifies the appearance and interaction of In-App Purchase products within the view hierarchy.
- [ProductViewStyleConfiguration](productviewstyleconfiguration.md) — The properties of an In-App Purchase product for use by custom product view styles.

### Styling subscription store controls

- [subscriptionStoreControlStyle(_:)](<../swiftui/view/subscriptionstorecontrolstyle(__).md>) — Sets the control style for subscription store views within a view.
- [subscriptionStoreControlStyle(_:placement:)](<../swiftui/view/subscriptionstorecontrolstyle(__placement_).md>) — Sets the control style and control placement for subscription store views within a view.
- [SubscriptionStoreControlStyle](subscriptionstorecontrolstyle.md) — A type that specifies the appearance and interaction of controls in the subscription store view instances within the view hierarchy.
- [SubscriptionStoreControlStyleConfiguration](subscriptionstorecontrolstyleconfiguration.md) — The properties of a subscription store control that includes the list of auto-renewable subscriptions to merchandise.
- [SubscriptionStoreControlPlacement](subscriptionstorecontrolplacement.md) — A type that specifies the placement of a subscription control in a subscription store view.

### Styling subscription offer views

- [AutomaticSubscriptionOfferViewStyle](automaticsubscriptionofferviewstyle.md)
- [CompactSubscriptionOfferViewStyle](compactsubscriptionofferviewstyle.md)
- [SubscriptionOfferViewStyleConfiguration](subscriptionofferviewstyleconfiguration.md)
- [SubscriptionOfferViewStyle](subscriptionofferviewstyle.md)

### Configuring subscription store controls

- [subscriptionStoreControlIcon(icon:)](<../swiftui/view/subscriptionstorecontrolicon(icon_).md>) — Sets a view to use to decorate individual subscription options within a subscription store view.
- [subscriptionStorePickerItemBackground(_:)](<../swiftui/view/subscriptionstorepickeritembackground(__).md>) — Sets the background style for picker items of the subscription store view instances within a view.
- [subscriptionStorePickerItemBackground(_:in:)](<../swiftui/view/subscriptionstorepickeritembackground(__in_).md>) — Sets the background shape and style for subscription store view picker items within a view.
- [subscriptionStoreButtonLabel(_:)](<../swiftui/view/subscriptionstorebuttonlabel(__).md>) — Configures subscription store view instances within a view to use the provided button label.
- [SubscriptionStoreButtonLabel](subscriptionstorebuttonlabel.md) — The label of the subscribe button that a subscription store view uses.

### Creating custom subscription store control styles

- [SubscriptionStoreButton](subscriptionstorebutton.md) — A button for subscribing to an in-app subscription with a localized label and optional caption.
- [SubscriptionStorePicker](subscriptionstorepicker.md) — A composite control with a picker for selecting a subscription option and a button for confirming the subscription.
- [SubscriptionStorePickerOption](subscriptionstorepickeroption.md) — A subscription option within a subscription picker control.

### Declaring the structure of a subscription store

- [SubscriptionOptionGroup](subscriptionoptiongroup.md) — A group of subscription options that includes optional views for labels and marketing content.
- [SubscriptionOptionGroupSet](subscriptionoptiongroupset.md) — A set of groups of subscription options that include optional views for labels and marketing content.
- [SubscriptionPeriodGroupSet](subscriptionperiodgroupset.md)
- [SubscriptionOptionSection](subscriptionoptionsection.md)
- [StoreContent](storecontent.md) — A type that represents the content of a store.
- [StoreContentBuilder](storecontentbuilder.md) — A result builder that creates store content from closures that you provide.

### Styling subscription option groups

- [subscriptionStoreOptionGroupStyle(_:)](<../swiftui/view/subscriptionstoreoptiongroupstyle(__).md>) — Sets the style subscription store views within this view use to display groups of subscription options.
- [subscriptionStoreOptionGroupStyle(_:)](<storecontent/subscriptionstoreoptiongroupstyle(__).md>)
- [SubscriptionOptionGroupStyle](subscriptionoptiongroupstyle.md)

### Adding backgrounds to subscription stores

- [containerBackground(_:for:)](<../swiftui/view/containerbackground(__for_).md>) — Sets the container background of the enclosing container using a view.
- [containerBackground(for:alignment:content:)](<../swiftui/view/containerbackground(for_alignment_content_).md>) — Sets the container background of the enclosing container using a view.
- [subscriptionStoreControlBackground(_:)](<../swiftui/view/subscriptionstorecontrolbackground(__)-7jxa9.md>) — Set a shape style to use for the background of subscription store view controls within the view.
- [subscriptionStoreControlBackground(_:)](<../swiftui/view/subscriptionstorecontrolbackground(__)-7ev89.md>) — Set a standard effect to use for the background of subscription store view controls within the view.
- [subscriptionStore](../swiftui/containerbackgroundplacement/subscriptionstore.md) — An automatic placement within a subscription store view, based on the view’s context.
- [subscriptionStoreHeader](../swiftui/containerbackgroundplacement/subscriptionstoreheader.md) — A background placement behind the marketing content of a subscription store view.
- [subscriptionStoreFullHeight](../swiftui/containerbackgroundplacement/subscriptionstorefullheight.md) — A background placement that spans the full height of a subscription store view.
- [SubscriptionStoreControlBackground](subscriptionstorecontrolbackground.md)

### Configuring accessory buttons

- [storeButton(_:for:)](<../swiftui/view/storebutton(__for_).md>) — Specifies the visibility of auxiliary buttons that store view and subscription store view instances may use.
- [subscriptionStoreSignInAction(_:)](<../swiftui/view/subscriptionstoresigninaction(__).md>) — Adds an action to perform when a person uses the sign-in button on a subscription store view within a view.
- [StoreButtonKind](storebuttonkind.md) — A button to display in a store view or subscription store view.
- [SubscriptionOfferViewButtonKind](subscriptionofferviewbuttonkind.md)

### Configuring the subscription store policies

- [subscriptionStorePolicyDestination(for:destination:)](<../swiftui/view/subscriptionstorepolicydestination(for_destination_).md>) — Configures a view as the destination for a policy button action in subscription store views.
- [subscriptionStorePolicyDestination(url:for:)](<../swiftui/view/subscriptionstorepolicydestination(url_for_).md>) — Configures a URL as the destination for a policy button action in subscription store views.
- [subscriptionStorePolicyForegroundStyle(_:)](<../swiftui/view/subscriptionstorepolicyforegroundstyle(__).md>) — Sets the style for the terms of service and privacy policy buttons within a subscription store view.
- [subscriptionStorePolicyForegroundStyle(_:_:)](<../swiftui/view/subscriptionstorepolicyforegroundstyle(____).md>) — Sets the primary and secondary style for the terms of service and privacy policy buttons within a subscription store view.
- [SubscriptionStorePolicyKind](subscriptionstorepolicykind.md) — The type of policy, such as the terms of service or privacy policies.

### Selecting subscription offers

- [subscriptionPromotionalOffer(offer:signature:)](<../swiftui/view/subscriptionpromotionaloffer(offer_signature_).md>) — Selects a promotional offer to apply to a purchase a customer makes from a subscription store view. _(deprecated)_
- [preferredSubscriptionOffer(_:)](<../swiftui/view/preferredsubscriptionoffer(__).md>) — Selects a subscription offer to apply to a purchase that a customer makes from a subscription store view, a store view, or a product view.
- [offerCodeRedemption(isPresented:onCompletion:)](<../swiftui/view/offercoderedemption(ispresented_oncompletion_).md>) _(deprecated)_

### Configuring purchase options and product descriptions

- [inAppPurchaseOptions(_:)](<../swiftui/view/inapppurchaseoptions(__).md>) — Add a function to call before initiating a purchase from StoreKit view within this view, providing a set of options for the purchase.
- [productDescription(_:)](<../swiftui/view/productdescription(__).md>) — Configure the visibility of labels displaying an in-app purchase product description within the view.

### Responding to store events

- [onInAppPurchaseStart(perform:)](<../swiftui/view/oninapppurchasestart(perform_).md>) — Add an action to perform when a user triggers the purchase button on a StoreKit view within this view.
- [onInAppPurchaseCompletion(perform:)](<../swiftui/view/oninapppurchasecompletion(perform_).md>) — Add an action to perform when a purchase initiated from a StoreKit view within this view completes.

### Loading StoreKit data

- [storeProductTask(for:priority:action:)](<../swiftui/view/storeproducttask(for_priority_action_).md>) — Declares the view as dependent on an In-App Purchase product and returns a modified view.
- [storeProductsTask(for:priority:action:)](<../swiftui/view/storeproductstask(for_priority_action_).md>) — Declares the view as dependent on a collection of In-App Purchase products and returns a modified view.
- [currentEntitlementTask(for:priority:action:)](<../swiftui/view/currententitlementtask(for_priority_action_).md>) — Declares the view as dependent on the entitlement of an In-App Purchase product, and returns a modified view.
- [subscriptionStatusTask(for:priority:action:)](<../swiftui/view/subscriptionstatustask(for_priority_action_).md>) — Declares the view as dependent on the status of an auto-renewable subscription group, and returns a modified view.
- [CollectionTaskState](product/collectiontaskstate.md) — The state of a task that loads a collection of products in the background.
- [TaskState](product/taskstate.md) — The state of a task that loads a product in the background.
- [EntitlementTaskState](entitlementtaskstate.md) — The state of an entitlement task.

### Requesting a refund

- [refundRequestSheet(for:isPresented:onDismiss:)](<../swiftui/view/refundrequestsheet(for_ispresented_ondismiss_).md>) — Display the refund request sheet for the given transaction.

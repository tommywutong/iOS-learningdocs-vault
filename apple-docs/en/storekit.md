---
title: StoreKit
framework: StoreKit
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.0+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 6.2+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit
source_url: 'https://developer.apple.com/documentation/storekit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit.json'
content_hash: 'sha256:19b662714848ab8e'
translated: false
---

> Navigation: [Technologies](technologies.md)

# StoreKit

<sub>Framework</sub>

Support In-App Purchases and interactions with the App Store.

## Overview

Use the StoreKit framework to provide the following features and services for your apps and In-App Purchases:

- **In-App Purchase** — Offer and promote In-App Purchases for content and services.
- **App transaction** — Verify a customer’s app purchase with an App Store-signed transaction.
- **Messages** — Control the display of App Store messages in your app.
- **Reviews** — Request App Store reviews and ratings from your customers.
- **Recommendations** — Provide recommendations for third-party content that customers can purchase from the App Store.
- **Ad network attribution** — Validate advertisement-driven app installations. See [AdAttributionKit](adattributionkit.md) for app ad campaigns on the App Store and alternative marketplaces.

The StoreKit framework also provides functionality for [External Purchase](storekit/external-purchase.md), [External link account](storekit/external-link-account.md), [PaymentMethodBinding](storekit/paymentmethodbinding.md), and [StoreDownloaderExtension](storekit/storedownloaderextension.md).

## Topics

### In-App Purchase

- [In-App Purchase](storekit/in-app-purchase.md) — Offer content and services in your app across Apple platforms using a Swift-based interface.
- [Understanding StoreKit workflows](storekit/understanding-storekit-workflows.md) — Implement an in-app store with several product types, using StoreKit views.
- [Getting started with In-App Purchase using StoreKit views](storekit/getting-started-with-in-app-purchases-using-storekit-views.md) — Set up an in-app store using SwiftUI and StoreKit views.

### App transaction

- [Supporting business model changes by using the app transaction](storekit/supporting-business-model-changes-by-using-the-app-transaction.md) — Access the app transaction to determine when a customer purchased an app and the features to which they’re entitled.
- [AppTransaction](storekit/apptransaction.md) — Information that represents the customer’s purchase of the app, cryptographically signed by the App Store.

### Messages

- [Message](storekit/message.md) — An instance for receiving and displaying App Store messages in your app.
- [Reason](storekit/message/reason-swift.struct.md) — Reasons for the App Store messages.
- [DisplayMessageAction](storekit/displaymessageaction.md) — An instance that asks StoreKit to display an App Store message, if appropriate.

### Reviews

- [Requesting App Store reviews](storekit/requesting-app-store-reviews.md) — Implement best practices for prompting users to review your app in the App Store.
- [RequestReviewAction](storekit/requestreviewaction.md) — An instance that tells StoreKit to request an App Store rating or review, if appropriate.
- [SKStoreReviewController](storekit/skstorereviewcontroller.md) — An object that controls the process of requesting App Store ratings and reviews from customers. _(deprecated)_

### Recommendations

- [Offering media for sale in your app](storekit/offering-media-for-sale-in-your-app.md) — Allow users to purchase media in the App Store from within your app.
- [SKStoreProductViewController](storekit/skstoreproductviewcontroller.md) — A view controller that provides a page where customers can purchase media from the App Store.
- [SKOverlay](storekit/skoverlay.md) — A class that displays an overlay you can use to recommend another app or an App Clip’s corresponding full app.

### Background assets extension

- [StoreDownloaderExtension](storekit/storedownloaderextension.md) — An app extension that uses the system implementation to schedule Apple-hosted asset-pack downloads automatically.

### Payment method binding

- [PaymentMethodBinding](storekit/paymentmethodbinding.md) — A binding that makes payment methods available in apps for an Apple Account.

### Ad network attribution

- [Ad network attribution](storekit/ad-network-attribution.md) — Validate advertisement-driven app installations.

### External Purchase

- [External Purchase](storekit/external-purchase.md) — Enable qualifying apps to offer external purchases.

### External link account

- [External link account](storekit/external-link-account.md) — Enable qualifying apps to link to an external website for account creation or management.

### Deprecated

- [SKCloudServiceSetupViewController](storekit/skcloudservicesetupviewcontroller.md) — A view controller that helps people perform setup for a cloud service, like an Apple Music subscription. _(deprecated)_
- [SKCloudServiceController](storekit/skcloudservicecontroller.md) — An object that determines the current capabilities of a person’s Music library. _(deprecated)_

### Articles

- [Supporting subscription offer codes in your app](storekit/supporting-subscription-offer-codes-in-your-app.md) — Provide subscription service for customers who redeem offer codes through the App Store or within your app.

### Structures

- [RedeemOption](storekit/redeemoption.md) — An option that customizes the behavior of an offer code redemption. _(beta)_

## See Also

### Related Documentation

- [App Store Server API](appstoreserverapi.md) — Manage your customers’ App Store transactions from your server.
- [StoreKit Test](storekittest.md) — Create and automate tests in Xcode for your app’s subscription and in-app purchase transactions, and SKAdNetwork implementations.
- [App Store Server Notifications](appstoreservernotifications.md) — Monitor In-App Purchase events in real time and learn of unreported external purchase tokens, with server notifications from the App Store.
- [App Store Connect API](appstoreconnectapi.md) — The data structure that represents an app store connect api resource.
- [Advanced Commerce API](advancedcommerceapi.md) — Support In-App Purchases through the App Store for exceptionally large catalogs of custom one-time purchases, subscriptions, and subscriptions with optional add-ons.
- [App Store Receipts](appstorereceipts.md) — Validate app and In-App Purchase receipts with the App Store. _(deprecated)_

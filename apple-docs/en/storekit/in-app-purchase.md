---
title: In-App Purchase
framework: StoreKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/in-app-purchase
source_url: 'https://developer.apple.com/documentation/storekit/in-app-purchase'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/in-app-purchase.json'
content_hash: 'sha256:ceb2507af293ea0f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# In-App Purchase

<sub>API Collection</sub>

Offer content and services in your app across Apple platforms using a Swift-based interface.

## Overview

With the In-App Purchase API, you can offer customers the opportunity to purchase digital content and services in your app. Customers can make the purchases within your app, and find your promoted products on the App Store.

The StoreKit framework connects to the App Store on your app’s behalf to prompt for, and securely process, payments. The framework then notifies your app, making the transactions for In-App Purchases available to your app on all of the customer’s devices. For each transaction that represents a current purchase, your app delivers the purchased products. To validate purchases, you can verify transactions on your server, or rely on StoreKit’s verification.

![](../../../attachments/3cddba76b6de9f552b4afc2d69fd0799/media-4447232@2x.png)

<sub>A diagram of the interactions between StoreKit, your app, the App Store, and your server that occur during a transaction.</sub>

The App Store can also communicate with your server. It notifies your server of transactions and auto-renewable subscription events through [App Store Server Notifications](../appstoreservernotifications.md), and provides the same transaction information, and more, through the [App Store Server API](../appstoreserverapi.md).

To learn how adding In-App Purchases fits in an overall app development workflow for the App Store, see [App Store Pathway](https://developer.apple.com/app-store/pathway/). For an overview of In-App Purchases and its features, including its configuration, testing capabilities, marketing for your products, and more, see [Simple and safe In-App Purchases](https://developer.apple.com/in-app-purchase/). For an overview on subscriptions, including creating subscription groups, Family Sharing, and more, see [Auto-renewable subscriptions](https://developer.apple.com/app-store/subscriptions/).

### Configure In-App Purchases

To use the In-App Purchase API, you first need to configure the products that your app merchandises.

- In the early stages of development, you can configure the products in the StoreKit configuration file in Xcode, and test your code without any dependency on App Store Connect. For more information, see [Setting up StoreKit Testing in Xcode](../xcode/setting-up-storekit-testing-in-xcode.md).
- When you’re ready for sandbox testing and production, configure the products in App Store Connect. You can add or remove products and refine or reconfigure existing products as you develop your app. For more information, see [Configure In-App Purchase settings](https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/overview-for-configuring-in-app-purchases).

You can also offer apps and In-App Purchases that run on multiple platforms as a single purchase. For more information on universal purchase, see [Add platforms](https://developer.apple.com/help/app-store-connect/create-an-app-record/add-platforms/).

### Support a store in your app

The In-App Purchase API takes advantage of Swift features like concurrency to simplify your In-App Purchase workflows, and SwiftUI to build stores with [StoreKit views](storekit-views.md). Use the API to manage access to content and subscriptions, receive App Store-signed transaction information, get the history of all In-App Purchase transactions, and more.

> [!note] Related sessions from WWDC21
> Session 10114: [Meet StoreKit 2](https://developer.apple.com/videos/play/wwdc2021/10114/)

The In-App Purchase API offers:

- Transaction information that’s App Store-signed in JSON Web Signature (JWS) format.
- Transaction and subscription status information that’s simple to parse in your app.
- An entitlements API, [currentEntitlements](transaction/currententitlements.md), that simplifies determining entitlements to unlock content and services for your customers.

> [!note] Related sessions from WWDC22
> Session 110404: [Implement proactive in-app purchase restore](https://developer.apple.com/videos/play/wwdc2022/110404/)

To support a store in your app, implement the following functionality:

- Listen for transaction state changes using the transaction listener, [updates](transaction/updates.md), to provide up-to-date service and content while your app is running.
- Use [StoreKit views](storekit-views.md) to merchandise your products; or request products to display from the App Store with [products(for:)](<product/products(for_).md>) and enable purchases using [purchase(options:)](<product/purchase(options_).md>). Unlock purchased content and services based on the purchase result, [PurchaseResult](product/purchaseresult.md).
- Iterate through a customer’s purchases anytime using the transaction sequence [all](transaction/all.md), and unlock the purchased content and services.
- Optionally, validate the signed transactions and signed subscription status information that you receive from the API.

## Topics

### In-App Purchase merchandising

- [StoreKit views](storekit-views.md) — Display a customizable In-App Purchase store using StoreKit views for SwiftUI.

### Product and subscription information

- [Implementing a store in your app using the StoreKit API](implementing-a-store-in-your-app-using-the-storekit-api.md) — Offer In-App Purchases and manage entitlements using signed transactions and status information.
- [Supporting monthly subscriptions with a 12-month commitment](supporting-monthly-subscriptions-with-a-12-month-commitment.md) — Configure, merchandise, and grant access to a monthly subscription with a 12-month commitment.
- [Managing the life cycle of monthly subscriptions with a 12-month commitment](managing-lifecycle-of-monthly-subscriptions-with-a-12-month-commitment-.md) — Handle renewals, cancellations, billing issues, refund requests, and price changes, and test subscriptions with a commitment plan.
- [Product](product.md) — Information about a product that you configure in App Store Connect.
- [SubscriptionInfo](product/subscriptioninfo.md) — Information about an auto-renewable subscription, such as its status, period, subscription group, and subscription offer details.
- [SubscriptionInfo](subscriptioninfo.md) — Information about an auto-renewable subscription.
- [SubscriptionStatus](subscriptionstatus.md) — Represents the renewal status information for an auto-renewable subscription.

### Purchase requests and results

- [PurchaseAction](purchaseaction.md) — An action that starts an In-App Purchase.
- [purchase(options:)](<product/purchase(options_).md>) — Initiates a purchase for the product with the App Store and displays the confirmation sheet.
- [PurchaseResult](product/purchaseresult.md) — The result of a purchase.

### Transaction history and entitlements

- [Transaction](transaction.md) — Information that represents the customer’s purchase of a product in your app.
- [updates](transaction/updates.md) — The asynchronous sequence that emits a transaction when the system creates or updates transactions that occur outside the app or on other devices.
- [all](transaction/all.md) — A sequence that emits all the customer’s transactions for your app.
- [currentEntitlements](transaction/currententitlements.md) — A sequence of the latest transactions that entitle a customer to In-App Purchases and subscriptions.

### JWS verification

- [VerificationResult](verificationresult.md) — A type that describes the result of a StoreKit verification.
- [VerificationError](verificationresult/verificationerror.md) — Error cases for StoreKit JWS verification.

### Subscription status and renewal information

- [Status](product/subscriptioninfo/status-swift.struct.md) — The renewal status information for an auto-renewable subscription.
- [RenewalInfo](product/subscriptioninfo/renewalinfo.md) — The renewal information for an auto-renewable subscription.
- [SubscriptionRenewalInfo](subscriptionrenewalinfo.md) — Represents the renewal information for an auto-renewable subscription.
- [RenewalState](product/subscriptioninfo/renewalstate.md) — The renewal states of auto-renewable subscriptions.
- [SubscriptionRenewalState](subscriptionrenewalstate.md) — The renewal states of auto-renewable subscriptions.
- [SubscriptionPeriod](subscriptionperiod.md) — Represents the duration of time between subscription renewals.

### Offers

- [Supporting offer codes in your app](supporting-offer-codes-in-your-app.md) — Enable customers to redeem offer codes through the App Store or within your app.
- [Supporting win-back offers in your app](supporting-win-back-offers-in-your-app.md) — Re-engage previous subscribers with a free or discounted offer for an auto-renewable subscription, for a specific duration.
- [Merchandising win-back offers in your app](merchandising-win-back-offers-in-your-app.md) — Present win-back offers to eligible customers in your app with the win-back offer sheet or by implementing custom merchandising.
- [SubscriptionOffer](product/subscriptionoffer.md) — Information about a subscription offer that you configure in App Store Connect.
- [OfferType](product/subscriptionoffer/offertype.md) — The types of offers for auto-renewable subscriptions.

### Promoted In-App Purchases

- [Supporting promoted In-App Purchases in your app](supporting-promoted-in-app-purchases-in-your-app.md) — Display promoted In-App Purchases on your product page and handle purchases that users initiate on the App Store.
- [PurchaseIntent](purchaseintent.md) — An instance that emits purchase intents, which indicate that the customer initiated a purchase outside of your app, for your app to complete.
- [PromotionInfo](product/promotioninfo.md) — Information about a promoted In-App Purchase that customizes its order and visibility on the device.
- [Testing promoted In-App Purchases](testing-promoted-in-app-purchases.md) — Test your In-App Purchases before making your app available in the App Store.

### App Store interactions

- [AppStore](appstore.md) — Interactions with the App Store, such as managing subscriptions, verifying devices, authorizing payments, synchronizing transactions, getting the environment, and more.
- [AppTransaction](apptransaction.md) — Information that represents the customer’s purchase of the app, cryptographically signed by the App Store.

### Storefront information

- [Storefront](storefront.md) — The region and unique identifier of the App Store storefront for the device.
- [current](storefront/current.md) — The current App Store storefront for product purchases.
- [updates](storefront/updates.md) — The asynchronous sequence that emits storefront information when the system updates the storefront.

### In-App Purchase Testing

- [Testing at all stages of development with Xcode and the sandbox](testing-at-all-stages-of-development-with-xcode-and-the-sandbox.md) — Verify your implementation of In-App Purchases by testing your code throughout its development.
- [Testing In-App Purchases with sandbox](testing-in-app-purchases-with-sandbox.md) — Test your implementation of In-App Purchases using real product information and server-to-server transactions in the sandbox environment.
- [Testing refund requests](testing-refund-requests.md) — Test your app’s implementation of refund requests, and your app’s and server’s handling of approved and declined refunds.
- [Testing win-back offers in Xcode](testing-win-back-offers-in-xcode.md) — Validate your app’s handling of win-back offers that you configure for the testing environment.
- [Testing Ask to Buy in Xcode](testing-ask-to-buy-in-xcode.md) — Validate your app’s handling of Ask To Buy in the testing environment.

### Advanced Commerce API interactions

- [AdvancedCommerceProduct](advancedcommerceproduct.md) — A product configured as a generic SKU in App Store Connect for use with the Advanced Commerce API.
- [Sending Advanced Commerce API requests from your app](sending-advanced-commerce-api-requests-from-your-app.md) — Send Advanced Commerce API requests from your app that you authorize with a JSON Web Signature (JWS) you generate on your server.
- [Generating JWS to sign App Store requests](generating-jws-to-sign-app-store-requests.md) — Create signed JSON Web Signature (JWS) strings on your server to authorize your API requests in your app.

### Errors

- [StoreKitError](storekiterror.md) — StoreKit In-App Purchase error codes.

### Deprecated

- [Choosing a StoreKit API for In-App Purchases](choosing-a-storekit-api-for-in-app-purchases.md) — Use the latest API to support In-App Purchases in new or existing apps, or the original API to support In-App Purchases in earlier operating systems.
- [Original API for In-App Purchase](original-api-for-in-app-purchase.md) — Offer additional content and services in your app using the Original In-App Purchase API.

## See Also

### In-App Purchase

- [Understanding StoreKit workflows](understanding-storekit-workflows.md) — Implement an in-app store with several product types, using StoreKit views.
- [Getting started with In-App Purchase using StoreKit views](getting-started-with-in-app-purchases-using-storekit-views.md) — Set up an in-app store using SwiftUI and StoreKit views.

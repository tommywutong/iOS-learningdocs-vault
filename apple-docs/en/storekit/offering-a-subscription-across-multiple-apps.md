---
title: Offering a Subscription Across Multiple Apps
framework: StoreKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/offering-a-subscription-across-multiple-apps
source_url: 'https://developer.apple.com/documentation/storekit/offering-a-subscription-across-multiple-apps'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/offering-a-subscription-across-multiple-apps.json'
content_hash: 'sha256:569ff96283c84b03'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md) · [In-App Purchase](in-app-purchase.md) · [Original API for In-App Purchase](original-api-for-in-app-purchase.md) · [Subscriptions and offers](subscriptions-and-offers.md)

# Offering a Subscription Across Multiple Apps

<sub>Article</sub>

Support a single auto-renewable subscription across multiple apps.

## Overview

You can offer customers auto-renewable subscription services that are accessible through multiple apps across one or more operating systems.

To offer this functionality, your server must grant access to the subscription content across all apps, despite the user having purchased the subscription within a specific app. You can use a unified account management database along with server-side receipt validation to validate a user’s purchase and handle in-app transactions. By entitling subscription access from your server, you can provide users the ability to access your subscription across multiple apps.

### Create the Subscription for Each App

To get started, use App Store Connect to create a separate and equivalent [auto-renewable subscription](https://help.apple.com/app-store-connect/#/dev06f89ce98) for each app that offers the multi-app subscription so that users can subscribe from any app. For design guidance, see [Human Interface Guidelines \> In-App Purchase](https://developer.apple.com/design/human-interface-guidelines/in-app-purchase/overview/introduction/).

> [!tip] Tip
> Use an [app bundle](https://help.apple.com/app-store-connect/#/dev96d99635a) to group apps that share auto-renewable subscriptions on the same platform in a single App Store product page. An app bundle enables customers to view and download apps in a single purchase.

The following image illustrates the steps for implementing a multi-app subscription:

![](../../../attachments/c8625dbac1c5c2caacdd8f3fd0f5f76d/media-3174488@2x.png)

<sub>A diagram of a subscription shared across multiple apps showing the flow of implementation between apps, developer account database, and the App Store.</sub>

### Authenticate the User

When providing auto-renewable subscription access across multiple apps, you must authenticate the user in a way that correlates across apps. Authenticating users using a login allows you to determine if the user has access to the content. To provide a consistent user experience, ensure that the login process is similar across your apps.

To provide an easy and secure login, take advantage of [Sign in with Apple](https://developer.apple.com/sign-in-with-apple/). Sign in with Apple allows you to identify a user across your apps, while maintaining user privacy and protecting your app against fraud. You can store and retrieve user account data across your apps and the user’s devices, and use that data to unlock access appropriately.

### Check Billing Status

After authenticating the user, determine whether to grant access to the content based on their transaction history in the receipt.

Check if the user has purchased any subscription products before showing a subscription offer in the app. If there’s a subscription purchase from any app, verify if the subscription is active by looking at the [subscription expiration date](https://developer.apple.com/library/archive/releasenotes/General/ValidateAppStoreReceipt/Chapters/ReceiptFields.html#//apple_ref/doc/uid/TP40010573-CH106-SW28) in the receipt.

Present users who don’t have an active subscription with the subscription for purchase. Consider all potential billing scenarios within your account database when determining eligibility and granting access to a user.

> [!important] Important
> If the user has purchased the subscription from an app, you must propagate the purchase across all the apps that provide the subscription service. Failing to persist the purchase to the other apps opens the possibility of a user paying multiple times for the same service.

### Validate Subscription Status

A user’s subscription status can change any time. Validate the receipt and check the latest [subscription expiration date](https://developer.apple.com/library/archive/releasenotes/General/ValidateAppStoreReceipt/Chapters/ReceiptFields.html#//apple_ref/doc/uid/TP40010573-CH106-SW28) to maintain the billing status for each user and reflect any changes.

[Enabling App Store Server Notifications](enabling-app-store-server-notifications.md) keeps your server aware of changes made to a customer’s subscription status. Update your records to keep users’ subscription status and content current. The billing status must be accurate in your account database to provide the expected user experience across all apps.

### Enable Access to Purchased Content

After determining that the user should have access, you can enable access in each app based on the [subscription expiration date](https://developer.apple.com/library/archive/releasenotes/General/ValidateAppStoreReceipt/Chapters/ReceiptFields.html#//apple_ref/doc/uid/TP40010573-CH106-SW28). The user can access the subscription within any app that offers the same service. Repeat the previous steps as necessary across each app or user’s session to unlock the subscription.

## See Also

### Essentials

- [Handling Subscriptions Billing](handling-subscriptions-billing.md) — Build logic around the date and time constraints of subscription products, while planning for all scenarios where you control access to content.
- [Enabling App Store Server Notifications](enabling-app-store-server-notifications.md) — Configure your server and provide an HTTPS URL to receive notifications about in-app purchase events and unreported external purchase tokens.
- [Reducing Involuntary Subscriber Churn](reducing-involuntary-subscriber-churn.md) — Prevent unintentional loss of subscribers due to billing issues.

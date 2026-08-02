---
title: In-App Purchase Programming Guide
apple_id: TP40008267
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: StoreKit
published: '2018-02-06'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html
archived_at: '2026-07-27T06:57:07.302891Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Designing%20Your%20App%E2%80%99s%20Products.md)

# About In-App Purchase

In-App Purchase allows you to embed a store inside your app using the StoreKit framework. This framework connects to the App Store on your app’s behalf to securely process payments from users, prompting them to authorize payment. The framework then notifies your app, which provides the purchased items to users. Use In-App Purchase to collect payment for additional features and content.

（原归档配图未能恢复：`remote_store_fetch_2x.png`）

For example, using In-App Purchase, you can implement the following scenarios:

- A basic version of your app with additional premium features
- A magazine app that lets users purchase and download new issues
- A game that offers new levels to explore
- An online game that allows players to purchase virtual property

## At a Glance

At a high level, the interactions between the user, your app, and the App Store during the In-App Purchase process take place in three stages, as shown in Figure I-1. First, the user navigates to your app’s store and your app displays its products. Second, the user selects a product to buy and the app requests payment from the App Store. Third, the App Store processes the payment and your app delivers the purchased product.

__Figure I-1__  Stages of the purchase process

（原归档配图未能恢复：`intro_2x.png`）

### You Create and Configure Products in App Store Connect

Understanding what kinds of products and behaviors are supported by In-App Purchase lets you design your app and in-app store to make the best use of this technology.

__Relevant Chapter:__ [Designing Your App’s Products](Designing%20Your%20App%E2%80%99s%20Products.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4denrxfvbuqmrnknlte)

### Your App Interacts with the App Store to Sell Products

All apps that use In-App Purchase need to implement the core functionality described in these chapters to let users make purchases and then deliver the purchased products.

These development tasks need to be done in order. The relevant chapters introduce them in the order you implement them, and they’re listed in full in [Implementation Checklist](Preparing%20for%20App%20Review.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4denrxfvbuqmjqfvjvona). To help plan your development, you may want to read the full checklist before you begin.

__Relevant Chapters:__ [Retrieving Product Information](Retrieving%20Product%20Information.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4denrxfvbuqmznknltk), [Requesting Payment](Requesting%20Payment.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4denrxfvbuqnbnknlte), [Promoting In-App Purchases](Promoting%20In-App%20Purchases.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4denrxfvbuqmjrfvjvomi), [Delivering Products](Delivering%20Products.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4denrxfvbuqnjnknltg)

### Subscriptions Require Additional Application Logic

Apps that offer subscriptions need to keep track of when the user has an active subscription, respond to expiration and renewal, and determine what content the user has access to.

__Relevant Chapter:__ [Working with Subscriptions](Working%20with%20Subscriptions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4denrxfvbuqnznknltm)

### Users Can Restore Purchases

Users can restore products that they previously purchased—for example, to bring content they’ve already paid for onto their new phone.

__Relevant Chapter:__ [Restoring Purchased Products](Restoring%20Purchased%20Products.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4denrxfvbuqobnknlts)

### Apps and Products Are Submitted for Review

When you’re done developing and testing, you submit your app and your In-App Purchase products for review.

__Relevant Chapter:__ [Preparing for App Review](Preparing%20for%20App%20Review.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4denrxfvbuqmjqfvjvomi)

## See Also

- Configure Capabilities > Add a capability in [Xcode Help](http://help.apple.com/xcode/mac) shows how to enable In-App purchase (among other capabilities) for your app.
- _[Receipt Validation Programming Guide](../../../releasenotes/General/Receipt%20Validation%20Programming%20Guide/About%20Receipt%20Validation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknzt)_ describes how to work with receipts, in particular with the record of successful in-app purchases.

[Next](Designing%20Your%20App%E2%80%99s%20Products.md)

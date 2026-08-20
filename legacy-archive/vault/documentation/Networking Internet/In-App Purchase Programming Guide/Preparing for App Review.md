---
title: In-App Purchase Programming Guide
apple_id: TP40008267
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: StoreKit
published: '2018-02-06'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Chapters/AppReview.html
archived_at: '2026-07-27T06:57:07.410866Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [In-App Purchase Programming Guide](About%20In-App%20Purchase.md)


[Next](Document%20Revision%20History.md)[Previous](Restoring%20Purchased%20Products.md)

# Preparing for App Review

After you finish testing, you’re ready to submit your app for review. This chapter highlights a few tips to help you through the review process.

## Submitting Products for Review

The first time you submit your app for review, you also need to submit in-app products to be reviewed at the same time. After the first submission, you can submit updates to your app and products for review independently of each other.

## Receipts in the Test Environment

Your app runs different environments while in development, review, and production, as show in Figure 8-1.

__Figure 8-1__  Development, review, and production environments

（原归档配图获取待重试：`app_review_2x.png`）

During development, you run a development-signed version of your app, which connects to your development servers and the test environment for the App Store. In production, your users run a production-signed version of your app which connects to your production servers and the production App Store. However, during app review, your app runs in a mixed production/test environment: it’s production signed and connects to your production servers, but it connects to the test environment for the App Store.

When validating receipts on your server, your server needs to be able to handle a production-signed app getting its receipts from Apple’s test environment. The recommended approach is for your production server to always validate receipts against the production App Store first. If validation fails with the error code “Sandbox receipt used in production”, validate against the test environment instead.

## Implementation Checklist

Before you submit your app for review, verify that you’ve implemented all of the required behavior. Make sure you’ve implemented the following core In-App Purchase behavior (listed in order of a typical development process):

- Create and configure products in App Store Connect.

  You can change your products throughout the process, but you need at least one product configured before you can test any code.
- Get a list of product identifiers, either from the app bundle or your own server. Send that list to the App Store using an instance of `SKProductsRequest`.
- Implement a user interface for your app’s store, using the instances of `SKProduct` returned by the App Store. Start with a simple interface during development, such as a table view or a few buttons.

  Implement a final user interface for your app’s store at whatever point makes sense in your development process.
- Request payment by adding an instance of `SKPayment` to the transaction queue using the `addPayment:` method of `SKPaymentQueue`.
- Implement a transaction queue observer, starting with the `paymentQueue:updatedTransactions:` method.

  Implement the other methods in the `SKPaymentTransactionObserver` protocol at whatever point makes sense in your development process.
- Deliver the purchased product by making a persistent record of the purchase for future launches, downloading any associated content, and finally calling the `finishTransaction:` method of `SKPaymentQueue`.

  During development, you can implement a trivial version of this code at first—for example, simply displaying “Product Delivered” on the screen—and then implement the real version at whatever point makes sense in your development process.

If your app sells non-consumable items, auto-renewable subscriptions, or non-renewing subscriptions, verify that you’ve implemented the following restoration logic:

- Provide UI to begin the restoration process.
- Retrieve information about past purchases by either refreshing the app receipt using the `SKReceiptRefreshRequest` class or restoring completed transactions using the `restoreCompletedTransactions` method of the `SKPaymentQueue` class.
- Let the user re-download content.

  If you use Apple-hosted content, restore completed transactions and use the transaction’s `downloads` property to get an instance of `SKDownload`.

  If you host your own content, make the appropriate calls to your server.

If your app sells auto-renewable or non-renewing subscriptions, verify that you’ve implemented the following subscription logic:

- Handle a newly-purchased subscription by delivering the most recently published piece of content—for example, the latest issue of a magazine.
- When new content is published, make it available to the user.
- When a subscription expires, let the user renew it.

  If your app sells auto-renewable subscriptions, let the App Store handle this process. Don’t try to handle it yourself.

  If your app sells non-renewing subscriptions, your app is responsible for this process.
- When a subscription becomes inactive, stop making new content available. Update your interface so the user has the option to purchase the subscription again, re-activating it.
- Implement some system to keep track of when content was published. Use this system when restoring purchases to give the user access to the content that was paid for, based on the periods of time the subscription was active.

[Next](Document%20Revision%20History.md)[Previous](Restoring%20Purchased%20Products.md)

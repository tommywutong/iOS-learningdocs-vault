---
title: In-App Purchase Programming Guide
apple_id: TP40008267
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: StoreKit
published: '2018-02-06'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Chapters/Products.html
archived_at: '2026-07-27T06:57:07.312936Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [In-App Purchase Programming Guide](About%20In-App%20Purchase.md)


[Next](Retrieving%20Product%20Information.md)[Previous](About%20In-App%20Purchase.md)

# Designing Your App’s Products

A _product_ is something you want to sell in your app’s store. You create and configure products in App Store Connect, and your app interacts with products using the `SKProduct` and `SKProductsRequest` classes.

## Understanding What You Can Sell Using In-App Purchase

You can use In-App Purchase to sell content, app functionality, and services.

- __Content.__ Deliver digital content or assets, such as magazines, photos, and artwork. Content can also be used by the app itself—for example, additional characters and levels in a game, filters in a camera app, and stationery in a word processor.
- __App functionality.__ Unlock behavior and expand features you’ve already delivered. Examples include a free game that offers multiplayer mode as an in-app purchase and a free weather app that lets users make a one-time purchase to remove ads.
- __Services.__ Have users pay for one-time services such as voice transcription and for ongoing services such as access to a collection of data.

You _can’t_ use In-App Purchase to sell real-world goods and services or to sell unsuitable content.

- __Real-world goods and services.__ You must deliver a digital good or service within your app when using In-App Purchase. Use a different payment mechanism to let your users buy real-world goods and services in your app, such as a credit card or payment service.
- __Unsuitable content.__ Don’t use In-App Purchase to sell content that the isn’t allowed by the App Review Guidelines—for example, pornography, hate speech, or defamation.

For detailed information about what you can offer using In-App Purchase, see [your license agreement and the App Review Guidelines](https://developer.apple.com/appstore/guidelines.html). Reviewing the guidelines carefully before you start coding helps you avoid delays and rejection during the review process. If the guidelines don’t address your case in sufficient detail, you can ask the App Review team specific questions using the [online contact form](https://developer.apple.com/appstore/contact/).

After you know what products you want to sell in your app and determine that In-App Purchase is the appropriate way to sell those products, you need to create the products in App Store Connect.

## Creating Products in App Store Connect

Before you start coding, you need to configure products in App Store Connect for your app to interact with. See [Create an in-app purchase](https://help.apple.com/itunes-connect/developer/#/devae49fb316) for detailed information. As you develop your app, you can add and remove products and refine or reconfigure your existing products.

Every product is associated with a specific app. Products created for use by one app are not available in other apps. Companion apps on a different platform are different apps—the products of the Mac app are not available in the iOS app and vice versa.

Products are reviewed when you submit your app as part of the app review process. Before users can buy a product, it must be approved by the reviewer and you must mark it as “cleared for sale” in App Store Connect.

## Product Types

Product types let you use In-App Purchase in a range of apps by providing several different product behaviors. In App Store Connect, you select one of the following product types:

- __Consumable products.__ Items that get used up over the course of running your app. Examples include minutes for a Voice over IP app and one-time services such as voice transcription.
- __Non-consumable products.__ Items that remain available to the user indefinitely on all of the user’s devices. They’re made available to all of the user’s devices. Examples include content, such as books and game levels, and additional app functionality.
- __Auto-renewable subscriptions.__ Episodic content. Like non-consumable products, auto-renewable subscriptions remain available to the user indefinitely on all of the user’s devices. Unlike non-consumable products, auto-renewable subscriptions have an expiration date. You deliver new content regularly, and users get access to content published during the time period their subscription is active. When an auto-renewable subscription is about to expire, the system automatically renews it on the user’s behalf.
- __Non-renewable subscriptions.__ Subscriptions that don’t involve delivering episodic content. Examples include access to a database of historic photos or a collection of flight maps. It’s your app’s responsibility to make the subscription available on all of the user’s devices and to let users restore the purchase. This product type is often used when your users already have an account on your server that you can use to identify them when restoring content. Expiration and the duration of the subscription are also left to your app (or your server) to implement and enforce.

## Differences Between Product Types

Each product type is designed for a particular use. The behavior of different product types varies in certain ways, as summarized in Table 1-1 and Table 1-2.

__Table 1-1__  Comparison of product types

| Product type | Non-consumable | Consumable |
| Users can buy | Once | Multiple times |
| Appears in the receipt | Always | Once |
| Synced across devices | By the system | Not synced |
| Restored | By the system | Not restored |

__Table 1-2__  Comparison of subscription types

| Subscription type | Auto-renewable | Non-renewing |
| Users can buy | Multiple times | Multiple times |
| Appears in the receipt | Always | Always |
| Synced across devices | By the system | By your app |
| Restored | By the system | By your app |

Products that expire or get used up—consumable products, auto-renewable subscriptions, and non-renewing subscriptions—can be purchased multiple times to get the consumable item again or extend the subscription. Non-consumable products unlock content that remains available to the user indefinitely, so these can only be purchased once.

Consumable products subscriptions appear in the receipt after being purchased but are removed the next time the receipt is updated, as discussed in more detail in [Persisting Using the App Receipt](Delivering%20Products.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4denrxfvbuqnjnknltcnq). All other types of products have an entry in the receipt that isn’t removed.

Consumable products, by their nature, aren’t synced or restored. Users understand that, for example, buying ten more bubbles on their iPhone doesn’t also give them ten more bubbles on their iPad. All other types of products are made available across all of the user’s devices. They’re also restored so users can continue to access their purchased content even after buying a new device. StoreKit handles the syncing and restoring process for auto-renewable subscriptions and for non-consumable products.

Non-renewing subscriptions differ from auto-renewable subscriptions in a few key ways. These differences give your app the flexibility to implement the correct behavior for your needs, as follows:

- Your app is responsible for calculating the time period that the subscription is active and determining what content needs to be made available to the user.
- Your app is responsible for detecting that a subscription is approaching its expiration date and prompting the user to renew the subscription by purchasing the product again.
- Your app is responsible for making subscriptions available across all the user’s devices after they’re purchased and for letting users restore past purchases. For example, most subscriptions are provided by a server; your server would need some mechanism to identify users and associate subscription purchases with the user who purchased them.

[Next](Retrieving%20Product%20Information.md)[Previous](About%20In-App%20Purchase.md)

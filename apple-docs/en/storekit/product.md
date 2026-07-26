---
title: Product
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product
source_url: 'https://developer.apple.com/documentation/storekit/product'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product.json'
content_hash: 'sha256:5b19ff0de0222858'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# Product

<sub>Structure</sub>

Information about a product that you configure in App Store Connect.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Product
```

## Overview

The `Product` type represents the in-app purchases that you configure in App Store Connect and make available for purchase within your app. Use `Product` to perform all product-related tasks in your app, from displaying in-app purchases and offers to making a purchase and getting transaction and subscription status information.

To get a `Product` instance, call [products(for:)](<product/products(for_).md>) and provide one or more in-app purchase product identifiers. Use a `Product` instance to display in-app purchases and subscription offers in your store, as follows:

- Show the localized name, description, and pricing information using [displayName](product/displayname.md), [description](product/description.md), and [displayPrice](product/displayprice.md), respectively.
- Determine whether a user is eligible for an introductory offer for the product using [isEligibleForIntroOffer](product/subscriptioninfo/iseligibleforintrooffer.md).
- Display your subscription offers using the subscription information in [subscription](product/subscription.md).

When users initiate a purchase, call [purchase(options:)](<product/purchase(options_).md>) or [purchase(confirmIn:options:)](<product/purchase(confirmin_options_)-3bivf.md>) on the product instance. If your app uses SwiftUI, you can also use [PurchaseAction](purchaseaction.md). Set purchase options ([PurchaseOption](product/purchaseoption.md)) to define an optional app account token, apply a promotional offer, or set a product quantity. Purchase options can also simulate an Ask to Buy scenario when you’re testing your app in the sandbox environment.

Use a `Product` instance to learn whether a user is entitled to a product by checking [currentEntitlement](product/currententitlement.md), which holds the transaction that entitles the user to the product. This transaction information, as well as the transaction in [latestTransaction](product/latesttransaction.md), are cryptographically signed by the App Store in JSON Web Signature (JWS) format.

If the product is an auto-renewable subscription, use the [status](product/subscriptioninfo/status-swift.property.md) and [renewalInfo](product/subscriptioninfo/status-swift.struct/renewalinfo.md) in the [subscription](product/subscription.md) information to help manage subscriptions and inform business decisions, such as presenting subscription offers.

For information about configuring In-App Purchases in App Store Connect, see [Overview for configuring In-App Purchases](https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/overview-for-configuring-in-app-purchases).

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Identifiable](../swift/identifiable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Requesting products from the App Store

- [products(for:)](<product/products(for_).md>) — Requests product data from the App Store.

### Displaying a product description and price

- [displayName](product/displayname.md) — The localized display name of the product, if it exists.
- [description](product/description.md) — The localized description of the product.
- [displayPrice](product/displayprice.md) — The localized string representation of the product price, suitable for display.
- [price](product/price.md) — The decimal representation of the cost of the product, in local currency.
- [priceFormatStyle](product/priceformatstyle.md) — The format style for the numbers in the price of the product.
- [subscriptionPeriodFormatStyle](product/subscriptionperiodformatstyle.md) — The format style for the date components related to a subscription’s duration.
- [subscriptionPeriodUnitFormatStyle](product/subscriptionperiodunitformatstyle.md) — The format style for subscription period units, such as week, month, or year.

### Purchasing a product

- [purchase(options:)](<product/purchase(options_).md>) — Initiates a purchase for the product with the App Store and displays the confirmation sheet.
- [purchase(confirmIn:options:)](<product/purchase(confirmin_options_)-6dj6y.md>) — Initiates a purchase for the product with the App Store and displays the confirmation sheet.
- [purchase(confirmIn:options:)](<product/purchase(confirmin_options_)-3bivf.md>) — Processes a purchase for the product.
- [purchase(confirmIn:options:)](<product/purchase(confirmin_options_)-8eai6.md>) — Processes a purchase for the product.
- [PurchaseOption](product/purchaseoption.md) — Optional settings for a product purchase that add account information, purchase details, and offers, or that specify behaviors.
- [PurchaseResult](product/purchaseresult.md) — The result of a purchase.
- [PurchaseError](product/purchaseerror.md) — Error information for product purchase errors.

### Receiving current entitlement information

- [currentEntitlements](product/currententitlements.md)

### Getting the latest transaction

- [latestTransaction](product/latesttransaction.md) — The most recent transaction for the product.

### Getting subscription information

- [subscription](product/subscription.md) — The subscription information for an auto-renewable subscripton.
- [SubscriptionInfo](product/subscriptioninfo.md) — Information about an auto-renewable subscription, such as its status, period, subscription group, and subscription offer details.
- [SubscriptionPeriod](product/subscriptionperiod.md) — Values that represent the duration of time between subscription renewals.
- [SubscriptionOffer](product/subscriptionoffer.md) — Information about a subscription offer that you configure in App Store Connect.
- [Status](product/subscriptioninfo/status-swift.struct.md) — The renewal status information for an auto-renewable subscription.

### Getting product identifiers and type

- [id](product/id.md) — The unique product identifier.
- [type](product/type.md) — The in-app purchase product type.
- [ProductType](product/producttype.md) — The types of in-app purchases.

### Getting Family Sharing status

- [isFamilyShareable](product/isfamilyshareable.md) — A Boolean value that indicates whether the product is available for Family Sharing in App Store Connect.

### Managing promoted in-app purchases

- [PromotionInfo](product/promotioninfo.md) — Information about a promoted In-App Purchase that customizes its order and visibility on the device.

### Loading products

- [CollectionTaskState](product/collectiontaskstate.md) — The state of a task that loads a collection of products in the background.
- [TaskState](product/taskstate.md) — The state of a task that loads a product in the background.

### Getting product info in JSON format

- [jsonRepresentation](product/jsonrepresentation.md) — The JSON representation of the product information.

### Getting subscription relationship

- [SubscriptionRelationship](product/subscriptionrelationship.md)

### Deprecated

- [currentEntitlement](product/currententitlement.md) — The transaction that entitles the user to the product. _(deprecated)_

## See Also

### Product and subscription information

- [Implementing a store in your app using the StoreKit API](implementing-a-store-in-your-app-using-the-storekit-api.md) — Offer In-App Purchases and manage entitlements using signed transactions and status information.
- [Supporting monthly subscriptions with a 12-month commitment](supporting-monthly-subscriptions-with-a-12-month-commitment.md) — Configure, merchandise, and grant access to a monthly subscription with a 12-month commitment.
- [Managing the life cycle of monthly subscriptions with a 12-month commitment](managing-lifecycle-of-monthly-subscriptions-with-a-12-month-commitment-.md) — Handle renewals, cancellations, billing issues, refund requests, and price changes, and test subscriptions with a commitment plan.
- [SubscriptionInfo](product/subscriptioninfo.md) — Information about an auto-renewable subscription, such as its status, period, subscription group, and subscription offer details.
- [SubscriptionInfo](subscriptioninfo.md) — Information about an auto-renewable subscription.
- [SubscriptionStatus](subscriptionstatus.md) — Represents the renewal status information for an auto-renewable subscription.

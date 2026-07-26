---
title: Product.PurchaseOption
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/purchaseoption
source_url: 'https://developer.apple.com/documentation/storekit/product/purchaseoption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/purchaseoption.json'
content_hash: 'sha256:2d2db70b594b48be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Product](../product.md)

# Product.PurchaseOption

<sub>Structure</sub>

Optional settings for a product purchase that add account information, purchase details, and offers, or that specify behaviors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PurchaseOption
```

## Overview

Associate purchase options with an in-app purchase when you call the methods to initiate a purchase, such as [purchase(options:)](<purchase(options_).md>) or [purchase(confirmIn:options:)](<purchase(confirmin_options_)-6dj6y.md>). Use the testing-specific options with [StoreKit Test](../../storekittest.md) or in the sandbox testing environment.

Purchase options enable you to provide additional information for the purchase, such as an app account token, promotional offer, win back offer, and quantity. You can also use purchase options to indicate how the transaction behaves if the storefront changes, and to indicate whether the transaction is eligible for an introductory offer.

> [!important] Important
> Purchases fail if a purchase option is invalid, and can result in the purchase method throwing a [StoreKitError](../storekiterror.md) or [PurchaseError](purchaseerror.md).

### Use purchase options during testing

In the sandbox testing environment, use [simulatesAskToBuyInSandbox(_:)](<purchaseoption/simulatesasktobuyinsandbox(__).md>) to test Ask To Buy scenarios.

In the Xcode testing environment with [StoreKit Test](../../storekittest.md), use the following testing-specific purchase options when you call [buyProduct(identifier:options:)](<../../storekittest/sktestsession/buyproduct(identifier_options_).md>):

- Use [codeOffer(referenceName:)](<purchaseoption/codeoffer(referencename_).md>) and [promotionalOffer(id:)](<purchaseoption/promotionaloffer(id_).md>) to simulate customers redeeming the offers.
- Use [purchaseDate(_:renewalBehavior:)](<purchaseoption/purchasedate(__renewalbehavior_).md>) to control the transaction date and subscription renewal behavior.

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Setting the purchase options

- [appAccountToken(_:)](<purchaseoption/appaccounttoken(__).md>) — Sets a UUID to associate the purchase with an account in your system.
- [winBackOffer(_:)](<purchaseoption/winbackoffer(__).md>) — Sets a win-back offer to apply to the purchase.
- [promotionalOffer(offerID:keyID:nonce:signature:timestamp:)](<purchaseoption/promotionaloffer(offerid_keyid_nonce_signature_timestamp_).md>) — Applies a promotional offer for an auto-renewable subscription. _(deprecated)_
- [promotionalOffer(offerID:signature:)](<purchaseoption/promotionaloffer(offerid_signature_).md>) _(deprecated)_
- [quantity(_:)](<purchaseoption/quantity(__).md>) — Indicates the quantity of items the customer is purchasing.

### Specifying the behavior for storefront changes

- [onStorefrontChange(shouldContinuePurchase:)](<purchaseoption/onstorefrontchange(shouldcontinuepurchase_).md>) — Indicates whether a transaction needs to continue if the App Store storefront changes on the device during the transaction.

### Specifying eligibility for an introductory offer

- [introductoryOfferEligibility(compactJWS:)](<purchaseoption/introductoryoffereligibility(compactjws_).md>) — Set the eligibility of an introductory offer for a purchase.

### Setting options for StoreKit Testing in Xcode

- [purchaseDate(_:renewalBehavior:)](<purchaseoption/purchasedate(__renewalbehavior_).md>) — Sets the purchase date for the transaction in the testing environment, and indicates the renewal behavior for an auto-renewable subscription.
- [SubscriptionRenewalBehavior](purchaseoption/subscriptionrenewalbehavior.md) — Renewal options for auto-renewable subscriptions that you purchase in the testing environment.
- [codeOffer(referenceName:)](<purchaseoption/codeoffer(referencename_).md>) — Sets an offer code for the transaction in the testing environment.
- [promotionalOffer(id:)](<purchaseoption/promotionaloffer(id_).md>) — Sets a promotional offer for the transaction in the testing environment.

### Setting options for sandbox testing

- [simulatesAskToBuyInSandbox(_:)](<purchaseoption/simulatesasktobuyinsandbox(__).md>) — Simulates an Ask to Buy scenario when testing your app in the sandbox environment.

### Setting custom purchase options

- [custom(key:value:)](<purchaseoption/custom(key_value_)-80cvh.md>) — Adds data for a custom key to a purchase.
- [custom(key:value:)](<purchaseoption/custom(key_value_)-3g3nc.md>) — Adds a string for a custom key to a purchase.
- [custom(key:value:)](<purchaseoption/custom(key_value_)-8tjim.md>) — Adds a Boolean value for a custom key to a purchase.
- [custom(key:value:)](<purchaseoption/custom(key_value_)-7rju9.md>) — Adds a number for a custom key to a purchase.

### Type Methods

- [promotionalOffer(_:compactJWS:)](<purchaseoption/promotionaloffer(__compactjws_).md>) — Apply a promotional offer to a purchase.
- [billingPlanType(_:)](<purchaseoption/billingplantype(__).md>)

## See Also

### Purchasing a product

- [purchase(options:)](<purchase(options_).md>) — Initiates a purchase for the product with the App Store and displays the confirmation sheet.
- [purchase(confirmIn:options:)](<purchase(confirmin_options_)-6dj6y.md>) — Initiates a purchase for the product with the App Store and displays the confirmation sheet.
- [purchase(confirmIn:options:)](<purchase(confirmin_options_)-3bivf.md>) — Processes a purchase for the product.
- [purchase(confirmIn:options:)](<purchase(confirmin_options_)-8eai6.md>) — Processes a purchase for the product.
- [PurchaseResult](purchaseresult.md) — The result of a purchase.
- [PurchaseError](purchaseerror.md) — Error information for product purchase errors.

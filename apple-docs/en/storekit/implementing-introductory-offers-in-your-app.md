---
title: Implementing introductory offers in your app
framework: StoreKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/implementing-introductory-offers-in-your-app
source_url: 'https://developer.apple.com/documentation/storekit/implementing-introductory-offers-in-your-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/implementing-introductory-offers-in-your-app.json'
content_hash: 'sha256:ba131df38c6feb58'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md) · [In-App Purchase](in-app-purchase.md) · [Original API for In-App Purchase](original-api-for-in-app-purchase.md) · [Subscriptions and offers](subscriptions-and-offers.md)

# Implementing introductory offers in your app

<sub>Article</sub>

Offer introductory pricing for auto-renewable subscriptions to eligible users.

## Overview

Apps with auto-renewable subscriptions can offer a discounted introductory price, including a free trial, to eligible users. You can make introductory offers to customers who haven’t previously received an introductory offer for the given product, or for any products in the same subscription group.

Start by setting up introductory offers in App Store Connect. Then, in your app, determine if the user is eligible to receive an introductory offer. When the app queries the App Store for a list of available products, display the introductory pricing if the user is eligible to receive them.

### Set Up Introductory Offers

Before you can display introductory offers in your app, you must first configure the offers in App Store Connect. For more information, see [Set an introductory offer for an auto-renewable subscription](https://help.apple.com/app-store-connect/#/deve1d49254f).

Choose from one of three types of introductory offers, which differ in their mode of payment. All subscriptions renew at the regular price when the introductory period is over. The offer types are “pay as you go”, “pay up front”, and “free trial”.

#### Pay As You Go

The [SKProductDiscountPaymentModePayAsYouGo](skproductdiscount/paymentmode-swift.enum/payasyougo.md) value represents the pay as you go offer type. In this introductory offer, new subscribers pay an introductory price each billing period for a specific duration (for example, $1.99 per month for 3 months).

![Pay as you go timeline](../../../attachments/cdf7424c589eb68fe7962e3c551ebba1/media-3149470@2x.png)

#### Pay Up Front

The [SKProductDiscountPaymentModePayUpFront](skproductdiscount/paymentmode-swift.enum/payupfront.md) value represents the pay up front offer type. In this introductory offer, new subscribers pay a one-time introductory price for a specific duration (for example, $1.99 for 2 months).

![Pay up front timeline](../../../attachments/d4efc45f4203f1875f488fa0f304656f/media-3149471@2x.png)

#### Free Trial

The [SKProductDiscountPaymentModeFreeTrial](skproductdiscount/paymentmode-swift.enum/freetrial.md) value represents a free trial offer type. In this introductory offer, new subscribers access content for free for a specified duration. Subscriptions begin immediately, but subscribers won’t be billed until the free trial period is over.

![Free trial timeline](../../../attachments/987bbe3dd419145066746cc36e06f45c/media-3174516@2x.png)

### Determine Eligibility

To determine if a user is eligible for an introductory offer, check their receipt:

1. Validate the receipt as described in [Validating receipts with the App Store](validating-receipts-with-the-app-store.md).
2. In the receipt, check the values of the [is_trial_period](../appstorereceipts/is_trial_period.md) and the [is_in_intro_offer_period](../appstorereceipts/is_in_intro_offer_period.md) for all in-app purchase transactions. If either of these fields are `true` for a given subscription, the user is not eligible for an introductory offer on that subscription product or any other products within the same subscription group. Use `subscription_group_identifier` in the [responseBody.Pending_renewal_info](../appstorereceipts/responsebody/pending_renewal_info-data.dictionary.md) array to determine the subscription group to which the subscription belongs.

Typically, you check the user’s eligibility from your server. Determine eligibility early—for example, on the first launch of the app, if possible.

![](../../../attachments/3700fb494140a08886656f52e6c8f493/media-2942147@2x.png)

<sub>Diagram showing that introductory offers are available to new subscribers, and to lapsed subscribers who receive an introductory offer for the first time.</sub>

Based on the receipt, you will find that new and returning customers are eligible for introductory offers, including free trials:

- New subscribers are always eligible.
- Lapsed subscribers who renew are eligible if they haven’t previously used an introductory offer for the given product (or any product within the same subscription group).

Existing subscribers are not eligible for an introductory offer for any product within the same subscription group. For example, customers are not eligible if they are upgrading, downgrading, or crossgrading their subscription from another product, regardless of whether they consumed an introductory offer in the past.

### Display the Introductory Offer

Once you determine the user is eligible for an introductory offer, query the App Store for available products, and present the offer to the user:

1. Retrieve localized information from the App Store about a specified list of subscription products using the [SKProductsRequest](skproductsrequest.md) class. Products that have an available discount defined in App Store Connect always include an [introductoryPrice](skproduct/introductoryprice.md) object.
2. Use the properties in the [introductoryPrice](skproduct/introductoryprice.md) object to display the discounted price for the subscription. Based on the type of the introductory offer (represented by [PaymentMode](skproductdiscount/paymentmode-swift.enum.md)), display a UI that describes the offer accordingly.

For design guidance, see [Human Interface Guidelines \> In-App Purchase](https://developer.apple.com/design/human-interface-guidelines/in-app-purchase/overview/).

## See Also

### Related Documentation

- [Receipt Validation Programming Guide](https://developer.apple.com/library/archive/releasenotes/General/ValidateAppStoreReceipt/Introduction.html#//apple_ref/doc/uid/TP40010573)

### Introductory offers

- [Testing introductory offers](testing-introductory-offers.md) — Test your introductory pricing in a variety of user scenarios.
- [SKProductDiscount](skproductdiscount.md) — The details of an introductory offer or a promotional offer for an auto-renewable subscription. _(deprecated)_

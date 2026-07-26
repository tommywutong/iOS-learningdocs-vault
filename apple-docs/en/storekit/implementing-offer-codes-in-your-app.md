---
title: Implementing offer codes in your app
framework: StoreKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/implementing-offer-codes-in-your-app
source_url: 'https://developer.apple.com/documentation/storekit/implementing-offer-codes-in-your-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/implementing-offer-codes-in-your-app.json'
content_hash: 'sha256:1f5d9e323eb7d404'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md) · [In-App Purchase](in-app-purchase.md) · [Original API for In-App Purchase](original-api-for-in-app-purchase.md) · [Subscriptions and offers](subscriptions-and-offers.md)

# Implementing offer codes in your app

<sub>Article</sub>

Enable customers to redeem offer codes through the App Store or within an app that uses receipts.

## Overview

> [!important] Important
> This article refers to some deprecated APIs from the [Original API for In-App Purchase](original-api-for-in-app-purchase.md) and receipts, also deprecated. To implement offer codes using the  [In-App Purchase](in-app-purchase.md) APIs with the [Transaction](transaction.md) class, see [Supporting offer codes in your app](supporting-offer-codes-in-your-app.md).

To help you acquire, retain, and win back customers, you can use offer codes. Offer codes are available for all in-app purchase types: consumables, non-consumables, non-renewing subscriptions, and auto-renewable subscriptions.

Offer codes are alphanumeric codes that provide In-App Purchases at a discount or for free for a specific duration. Configure the offers and create offer codes in App Store Connect, and distribute them to your customers. Customers can redeem offer codes in the App Store, using offer code redemption URLs, or in your app if you’ve implemented one of the following APIs:

- [offerCodeRedemption(isPresented:onCompletion:)](<../swiftui/view/offercoderedemption(ispresented_oncompletion_).md>) or [presentOfferCodeRedeemSheet(in:)](<appstore/presentoffercoderedeemsheet(in_).md>), which are available in iOS 16 and later and iPadOS 16 and later
- [- presentCodeRedemptionSheet](<skpaymentqueue/presentcoderedemptionsheet().md>), which is available in iOS 14 and later and iPadOS 14 and later.

When customers redeem a valid offer code, your app receives a successful transaction on the payment queue, and you receive a server notification if you’ve enabled [App Store Server Notifications](../appstoreservernotifications.md). The receipt contains an `offer_code_ref_name` field that identifies the offer.

For information on subscription offer types and choosing the offer type to suit your business needs, see [Providing subscription offers](https://developer.apple.com/app-store/subscriptions/#providing-subscription-offers).

### Set up offer codes in App Store Connect

Configure offers and manage your offer codes in App Store Connect. You can have up to 10 active offers per subscription, and create codes for a maximum of 1,000,000 redemptions per app, per quarter. There are two types of offer codes: one-time use codes, and custom codes. The offer code redemption APIs support both.

Download the offer codes from App Store Connect to distribute them to your customers. For more information on creating and distributing offer codes, and to learn which type of offer code may work for your campaign, see [Set up offer codes](https://help.apple.com/app-store-connect/#/dev6a098e4b1).

### Redeem offer codes in your app

To display the system sheet for customers to redeem offer codes within your app, call one of the redemption APIs, depending on your app’s UI implementation:

- Call [offerCodeRedemption(isPresented:onCompletion:)](<../swiftui/view/offercoderedemption(ispresented_oncompletion_).md>) if your app uses SwiftUI.
- Call [presentOfferCodeRedeemSheet(in:)](<appstore/presentoffercoderedeemsheet(in_).md>) if your app uses UIKit.
- Call [- presentCodeRedemptionSheet](<skpaymentqueue/presentcoderedemptionsheet().md>) for apps running on devices prior to iOS 16 and iPadOS 16.

The redemption sheet takes care of the redemption flow, including alerting customers about invalid entries, as appropriate. Invalid entries may include, for example, expired offer codes, invalid codes, or codes that would result in a subscription downgrade.

Including the redemption sheet in your app is recommended, but optional. For more guidance on supporting offer code redemption within your app, see Human Interface Guidelines \> [In-app purchase](https://developer.apple.com/design/human-interface-guidelines/in-app-purchase).

### Support offer codes redeemed outside your app

Customers may redeem offer codes outside your app. If a customer doesn’t have your app, the App Store prompts them to download it as part of the redemption flow.

To handle offer codes — and other transactions that can occur outside of your app – you need to set up a transaction observer at app launch. For more information on this best practice, see [Setting up the transaction observer for the payment queue](setting-up-the-transaction-observer-for-the-payment-queue.md). Check that your app’s customer-onboarding experience verifies the receipt and provides service for all products related to the redeemed offer code. Update your records if you keep a backend system to manage your customers.

### Identify subscriptions purchased with offer codes, in receipts

When a customer successfully redeems an offer code, the receipt contains a transaction with the field: `offer_code_ref_name`. This field’s value is the offer reference name that you configure in App Store Connect. The field appears in the [responseBody.Latest_receipt_info](../appstorereceipts/responsebody/latest_receipt_info-data.dictionary.md) and [responseBody.Pending_renewal_info](../appstorereceipts/responsebody/pending_renewal_info-data.dictionary.md) objects for receipts, and in the [unified_receipt.Latest_receipt_info](../appstoreservernotifications/unified_receipt/latest_receipt_info-data.dictionary.md) and [unified_receipt.Pending_renewal_info](../appstoreservernotifications/unified_receipt/pending_renewal_info-data.dictionary.md) objects for server notifications.

> [!note] Note
> The `offer_code_ref_name` field is not populated for consumables, non-consumables, and non-renewing subscriptions.

### Provide service to existing and new customers

When an existing customer redeems an offer code, your app receives a transaction on the payment queue ([- paymentQueue:updatedTransactions:](<skpaymenttransactionobserver/paymentqueue(__updatedtransactions_).md>) in the [SKPaymentTransactionStatePurchased](skpaymenttransactionstate/purchased.md) state. This flow is the same as a typical subscription purchase flow, but the receipt contains the offer code reference. Your app follows these steps:

1. Validates the receipt. For more information, see [Validating receipts with the App Store](validating-receipts-with-the-app-store.md).
2. Looks for the `offer_code_ref_name` field in the receipt to determine if the subscription is from an offer code.
3. Provides the subscription service based on the offer.
4. Calls [- finishTransaction:](<skpaymentqueue/finishtransaction(__).md>).

When you acquire new customers with an offer code, they open your app for the first time already having a subscription. In addition to providing subscription service, you may need to update your backend system’s records. Your app follows these steps:

1. When the app first launches, validate the receipt.
2. In the receipt, look for a transaction with the `offer_code_ref_name` field to determine if the subscription is from an offer code.
3. Provide the subscription service based on the offer.
4. Guide the customer through your new-customer experience as needed. Update your backend system’s records.
5. Call [- finishTransaction:](<skpaymentqueue/finishtransaction(__).md>).

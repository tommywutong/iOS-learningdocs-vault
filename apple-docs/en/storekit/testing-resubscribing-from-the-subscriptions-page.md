---
title: Testing resubscribing from the subscriptions page
framework: StoreKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/testing-resubscribing-from-the-subscriptions-page
source_url: 'https://developer.apple.com/documentation/storekit/testing-resubscribing-from-the-subscriptions-page'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/testing-resubscribing-from-the-subscriptions-page.json'
content_hash: 'sha256:0ad0b14ac4040ffd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md) · [In-App Purchase](in-app-purchase.md) · [Testing In-App Purchases with sandbox](testing-in-app-purchases-with-sandbox.md)

# Testing resubscribing from the subscriptions page

<sub>Article</sub>

Verify that your app can reactivate an expired subscription by receiving a transaction callback or inspecting an updated receipt.

## Overview

Customers can manage their active subscriptions, as well as their expired subscriptions for up to a year after expiry, on the Subscriptions page in iOS, tvOS, iPadOS, and macOS. From this page, customers can upgrade, downgrade, cancel, or change the type of their subscriptions.

In this test scenario, the customer resubscribes to an expired subscription from the Subscriptions page in the App Store.

### Set up testing

This test case requires one or more subscriptions configured in App Store Connect and an expired subscription for your Sandbox Apple Account. If you don’t already have an expired subscription, purchase an auto-renewable subscription and let it expire.

### Begin testing

To test resubscribing from the Subscriptions page:

1. On the test iOS device, open Settings \> Developer.
2. In the Sandbox Account section, tap your highlighted Sandbox Apple Account, and tap Manage.
3. On devices running iOS 16 or later, tap Subscriptions on the Account Settings sheet.
4. In the sandbox Subscriptions page, select the expired subscription you want to reactivate. The subscription products that appear are those you configured in App Store Connect under the same subscription group.
5. Select a subscription product to resubscribe to.
6. To complete the purchase, authenticate the payment sheet that appears.
7. Open your app.
8. In Xcode, verify that your [SKPaymentTransactionObserver](skpaymenttransactionobserver.md) gets a callback on [- paymentQueue:updatedTransactions:](<skpaymenttransactionobserver/paymentqueue(__updatedtransactions_).md>) with a transaction in the [SKPaymentTransactionStatePurchased](skpaymenttransactionstate/purchased.md) state.
9. Check that your app retrieves and verifies the app receipt. Verify that the successful transaction is in the receipt.
10. Check that your app makes the in-app purchase available and updates the subscriber’s status.
11. In Xcode, check that your app calls [- finishTransaction:](<skpaymentqueue/finishtransaction(__).md>). For more information, see [Finishing a transaction](finishing-a-transaction.md).

### Conclude testing

This test case requires no cleanup. For auto-renewable subscriptions, you can perform the test again when the subscription expires.

## See Also

### Subscriptions

- [Testing an auto-renewable subscription](testing-an-auto-renewable-subscription.md) — Verify that your app handles a subscription lapse properly using the accelerated time rates within the sandbox environment.
- [Testing disabling auto-renew](testing-disabling-auto-renew.md) — Verify that your app receives subscription updates when a user cancels a subscription by verifying the receipt or receiving a notification.

---
title: Subscriptions and offers
framework: StoreKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/subscriptions-and-offers
source_url: 'https://developer.apple.com/documentation/storekit/subscriptions-and-offers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptions-and-offers.json'
content_hash: 'sha256:ee0447aa16cce201'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md) · [In-App Purchase](in-app-purchase.md) · [Original API for In-App Purchase](original-api-for-in-app-purchase.md)

# Subscriptions and offers

<sub>API Collection</sub>

Offer customers additional time-based content and services through purchases they make within your app.

## Topics

### Essentials

- [Handling Subscriptions Billing](handling-subscriptions-billing.md) — Build logic around the date and time constraints of subscription products, while planning for all scenarios where you control access to content.
- [Enabling App Store Server Notifications](enabling-app-store-server-notifications.md) — Configure your server and provide an HTTPS URL to receive notifications about in-app purchase events and unreported external purchase tokens.
- [Offering a Subscription Across Multiple Apps](offering-a-subscription-across-multiple-apps.md) — Support a single auto-renewable subscription across multiple apps.
- [Reducing Involuntary Subscriber Churn](reducing-involuntary-subscriber-churn.md) — Prevent unintentional loss of subscribers due to billing issues.

### Introductory offers

- [Implementing introductory offers in your app](implementing-introductory-offers-in-your-app.md) — Offer introductory pricing for auto-renewable subscriptions to eligible users.
- [Testing introductory offers](testing-introductory-offers.md) — Test your introductory pricing in a variety of user scenarios.
- [SKProductDiscount](skproductdiscount.md) — The details of an introductory offer or a promotional offer for an auto-renewable subscription. _(deprecated)_

### Promotional offers

- [Setting up promotional offers](setting-up-promotional-offers.md) — Generate a key and configure offers for auto-renewable subscriptions in App Store Connect.
- [Implementing promotional offers in your app](implementing-promotional-offers-in-your-app.md) — Offer discounted pricing for auto-renewable subscription products to eligible subscribers.
- [Generating a signature for promotional offers](generating-a-signature-for-promotional-offers.md) — Create a signature to validate a promotional offer using your private key.
- [Generating a Promotional Offer Signature on the Server](generating-a-promotional-offer-signature-on-the-server.md) — Generate a signature using your private key and lightweight cryptography libraries.
- [SKPaymentDiscount](skpaymentdiscount.md) — The signed discount to apply to a payment. _(deprecated)_

### Offer codes

- [Implementing offer codes in your app](implementing-offer-codes-in-your-app.md) — Enable customers to redeem offer codes through the App Store or within an app that uses receipts.

### Subscription service entitlement

- [Determining service entitlement on the server](determining-service-entitlement-on-the-server.md) — Identify a customer’s entitlement to your service, offers, and messaging by analyzing a validated receipt and the state of their subscription.

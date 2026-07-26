---
title: Testing an auto-renewable subscription
framework: StoreKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/testing-an-auto-renewable-subscription
source_url: 'https://developer.apple.com/documentation/storekit/testing-an-auto-renewable-subscription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/testing-an-auto-renewable-subscription.json'
content_hash: 'sha256:f09262a302ac2685'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md) · [In-App Purchase](in-app-purchase.md) · [Testing In-App Purchases with sandbox](testing-in-app-purchases-with-sandbox.md)

# Testing an auto-renewable subscription

<sub>Article</sub>

Verify that your app handles a subscription lapse properly using the accelerated time rates within the sandbox environment.

## Overview

Auto-renewable subscriptions behave differently in the sandbox environment and the production environment.

In the sandbox environment, subscription renewals happen at an accelerated rate, and auto-renewable subscriptions renew up to 12 times after the initial purchase. This enables you to test how your app handles a subscription renewal, a subscription lapse, and a subscription history that includes gaps.

You can choose a subscription renewal speed for each Sandbox Apple Account in App Store Connect. For a complete list of subscription durations within the sandbox environment and more information, see [Manage Sandbox Apple Account settings](https://developer.apple.com/help/app-store-connect/test-in-app-purchases/manage-sandbox-apple-account-settings/).

The accelerated expiration and renewal rates in the sandbox environment make it possible for subscriptions to expire before the system tries to renew them. When a subscription expires before the system tries to renew it, it results in a short lapse in the subscription period. These lapses are possible in production; verify that your app handles them appropriately.

## See Also

### Subscriptions

- [Testing resubscribing from the subscriptions page](testing-resubscribing-from-the-subscriptions-page.md) — Verify that your app can reactivate an expired subscription by receiving a transaction callback or inspecting an updated receipt.
- [Testing disabling auto-renew](testing-disabling-auto-renew.md) — Verify that your app receives subscription updates when a user cancels a subscription by verifying the receipt or receiving a notification.

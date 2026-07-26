---
title: Testing a successful transaction
framework: StoreKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/testing-a-successful-transaction
source_url: 'https://developer.apple.com/documentation/storekit/testing-a-successful-transaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/testing-a-successful-transaction.json'
content_hash: 'sha256:6acd831534dbc7a9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md) · [In-App Purchase](in-app-purchase.md) · [Testing In-App Purchases with sandbox](testing-in-app-purchases-with-sandbox.md)

# Testing a successful transaction

<sub>Article</sub>

Confirm that your app can make a successful transaction in the sandbox environment by inspecting the transaction.

## Overview

Set a breakpoint in your implementation of the transaction queue observer’s [- paymentQueue:updatedTransactions:](<skpaymenttransactionobserver/paymentqueue(__updatedtransactions_).md>) method. Then sign in to the App Store with a Sandbox Apple Account, and make a purchase in your app. Inspect the transaction to verify that its status is [SKPaymentTransactionStatePurchased](skpaymenttransactionstate/purchased.md).

Set a breakpoint at the point in your code where your app stores the purchase, and confirm that your code saves the data in response to a successful purchase. Inspect the user default or iCloud key-value store, to verify that your code correctly records the information. For more information on saving data in response to a successful purchase, see [Persisting a purchase](persisting-a-purchase.md).

## See Also

### Transaction observer

- [Testing transaction observer code](testing-transaction-observer-code.md) — Verify that your app activates its payment transaction observer by using breakpoints.
- [Testing complete transactions](testing-complete-transactions.md) — Verify that your app completes transactions properly by confirming that any downloadable purchases are present on your test device.

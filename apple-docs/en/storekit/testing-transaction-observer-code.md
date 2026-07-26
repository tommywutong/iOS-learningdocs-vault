---
title: Testing transaction observer code
framework: StoreKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/testing-transaction-observer-code
source_url: 'https://developer.apple.com/documentation/storekit/testing-transaction-observer-code'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/testing-transaction-observer-code.json'
content_hash: 'sha256:3f2f15843177f660'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md) · [In-App Purchase](in-app-purchase.md) · [Testing In-App Purchases with sandbox](testing-in-app-purchases-with-sandbox.md)

# Testing transaction observer code

<sub>Article</sub>

Verify that your app activates its payment transaction observer by using breakpoints.

## Overview

Review the transaction observer’s implementation of the [SKPaymentTransactionObserver](skpaymenttransactionobserver.md) protocol. Verify that the [SKPaymentTransactionObserver](skpaymenttransactionobserver.md) listens for transactions when:

- Your app isn’t displaying its store UI
- If you didn’t recently initiate a purchase

Locate the call to the [- addTransactionObserver:](<skpaymentqueue/add(__)-5ciz2.md>) method of [SKPaymentQueue](skpaymentqueue.md) in your code. Verify that your app calls this method at app launch. For more information, see [Setting up the transaction observer for the payment queue](setting-up-the-transaction-observer-for-the-payment-queue.md).

## See Also

### Transaction observer

- [Testing a successful transaction](testing-a-successful-transaction.md) — Confirm that your app can make a successful transaction in the sandbox environment by inspecting the transaction.
- [Testing complete transactions](testing-complete-transactions.md) — Verify that your app completes transactions properly by confirming that any downloadable purchases are present on your test device.

---
title: Testing complete transactions
framework: StoreKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/testing-complete-transactions
source_url: 'https://developer.apple.com/documentation/storekit/testing-complete-transactions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/testing-complete-transactions.json'
content_hash: 'sha256:f93204a2c55d8bfd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md) · [In-App Purchase](in-app-purchase.md) · [Testing In-App Purchases with sandbox](testing-in-app-purchases-with-sandbox.md)

# Testing complete transactions

<sub>Article</sub>

Verify that your app completes transactions properly by confirming that any downloadable purchases are present on your test device.

## Overview

Locate where your app calls the [- finishTransaction:](<skpaymentqueue/finishtransaction(__).md>) method, and verify that your app completes all work related to the transaction before calling the method. For example, if the purchase includes downloadable content, verify your app downloaded the content to your test device as described in [Persisting a purchase](persisting-a-purchase.md). Verify that you call [- finishTransaction:](<skpaymentqueue/finishtransaction(__).md>) for every transaction, whether it succeeded or failed. For more information, see [Finishing a transaction](finishing-a-transaction.md).

## See Also

### Transaction observer

- [Testing transaction observer code](testing-transaction-observer-code.md) — Verify that your app activates its payment transaction observer by using breakpoints.
- [Testing a successful transaction](testing-a-successful-transaction.md) — Confirm that your app can make a successful transaction in the sandbox environment by inspecting the transaction.

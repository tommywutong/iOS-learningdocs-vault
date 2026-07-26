---
title: Finishing a transaction
framework: StoreKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/finishing-a-transaction
source_url: 'https://developer.apple.com/documentation/storekit/finishing-a-transaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/finishing-a-transaction.json'
content_hash: 'sha256:7a27ea11a138d2fd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md) · [In-App Purchase](in-app-purchase.md) · [Original API for In-App Purchase](original-api-for-in-app-purchase.md)

# Finishing a transaction

<sub>Article</sub>

Finish the transaction to complete the purchase process.

## Overview

Finishing a transaction tells StoreKit that your app completed its workflow to make a purchase complete. Unfinished transactions remain in the queue until they’re finished, so be sure to add the transaction queue observer every time your app launches, to enable your app to finish the transactions. Your app needs to finish each transaction, whether it succeeds or fails.

Do all of the following before you finish a transaction:

- Persist the purchase.
- Deliver, download, or unlock the purchased content.
- Update your app’s UI so the user can access the product.

To finish the transaction, call the [- finishTransaction:](<skpaymentqueue/finishtransaction(__).md>) method on the payment queue.

**Swift**

```swift
let transaction: SKPaymentTransaction = <# The current transaction #>
SKPaymentQueue.default().finishTransaction(transaction)
```

**Objective-C**

```objc
SKPaymentTransaction *transaction = <# The currrent transaction #>;
[[SKPaymentQueue defaultQueue] finishTransaction:transaction];
```

After you finish a transaction, don’t take any actions on it or do any work to deliver the product. If any work remains, your app isn’t ready to finish the transaction.

> [!important] Important
> Don’t call the [- finishTransaction:](<skpaymentqueue/finishtransaction(__).md>) method before the transaction is actually complete and attempt to use some other mechanism in your app to track the transaction as unfinished. StoreKit doesn’t function that way, and doing that prevents your app from downloading Apple-hosted content and can lead to other issues.

## See Also

### Content delivery

- [Unlocking purchased content](unlocking-purchased-content.md) — Deliver content to the customer after validating the purchase.
- [Persisting a purchase](persisting-a-purchase.md) — Keep a persistent record of a purchase to continue making the product available as needed.
- [SKDownload](skdownload.md) — Downloadable content associated with a product. _(deprecated)_

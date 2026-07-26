---
title: unfinished
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/unfinished
source_url: 'https://developer.apple.com/documentation/storekit/transaction/unfinished'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/unfinished.json'
content_hash: 'sha256:d39d268b6af24fd1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# unfinished

<sub>Type Property</sub>

A sequence that emits unfinished transactions for the customer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var unfinished: Transaction.Transactions { get }
```

## Discussion

A transaction is unfinished until you call [finish()](<finish().md>). Use the [unfinished](unfinished.md) sequence to find the transactions your app needs to process to deliver purchased content or enable service.

## See Also

### Getting transaction history

- [latest(for:)](<latest(for_).md>) — Gets the customer’s most recent transaction for an In-App Purchase.
- [all](all.md) — A sequence that emits all the customer’s transactions for your app.
- [SKIncludeConsumableInAppPurchaseHistory](../../bundleresources/information-property-list/skincludeconsumableinapppurchasehistory.md) — A Boolean value that determines whether StoreKit includes finished consumable In-App Purchases in transaction information.

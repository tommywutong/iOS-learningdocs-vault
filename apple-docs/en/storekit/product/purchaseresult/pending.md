---
title: Product.PurchaseResult.pending
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/purchaseresult/pending
source_url: 'https://developer.apple.com/documentation/storekit/product/purchaseresult/pending'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/purchaseresult/pending.json'
content_hash: 'sha256:d560c015928adbf9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [PurchaseResult](../purchaseresult.md)

# Product.PurchaseResult.pending

<sub>Case</sub>

The purchase is pending, and requires action from the customer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case pending
```

## Discussion

If a pending purchase succeeds, StoreKit delivers the resulting [Transaction](../../transaction.md) in the transaction [updates](../../transaction/updates.md).

## See Also

### Getting the Purchase Results

- [Product.PurchaseResult.success(_:)](<success(__).md>) — The purchase succeeded and results in a transaction.
- [Product.PurchaseResult.userCancelled](usercancelled.md) — The user canceled the purchase.

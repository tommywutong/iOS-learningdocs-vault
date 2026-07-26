---
title: 'Product.PurchaseResult.success(_:)'
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/product/purchaseresult/success(_:)'
source_url: 'https://developer.apple.com/documentation/storekit/product/purchaseresult/success(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/purchaseresult/success%28_%3A%29.json'
content_hash: 'sha256:e2e7be4833c788fc'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [PurchaseResult](../purchaseresult.md)

# Product.PurchaseResult.success(_:)

<sub>Case</sub>

The purchase succeeded and results in a transaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case success(VerificationResult<Transaction>)
```

## See Also

### Getting the Purchase Results

- [Product.PurchaseResult.userCancelled](usercancelled.md) — The user canceled the purchase.
- [Product.PurchaseResult.pending](pending.md) — The purchase is pending, and requires action from the customer.

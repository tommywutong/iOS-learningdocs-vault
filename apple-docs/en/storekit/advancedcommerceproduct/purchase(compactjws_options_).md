---
title: 'purchase(compactJWS:options:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [watchOS 11.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/advancedcommerceproduct/purchase(compactjws:options:)'
source_url: 'https://developer.apple.com/documentation/storekit/advancedcommerceproduct/purchase(compactjws:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/advancedcommerceproduct/purchase%28compactjws%3Aoptions%3A%29.json'
content_hash: 'sha256:066c48b7556625c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [AdvancedCommerceProduct](../advancedcommerceproduct.md)

# purchase(compactJWS:options:)

<sub>Instance Method</sub>

Processes a purchase for the product.

<sub>watchOS</sub>

```swift
@MainActor func purchase(compactJWS: String, options: Set<AdvancedCommerceProduct.PurchaseOption> = []) async throws -> AdvancedCommerceProduct.PurchaseResult
```

## Parameters

- `compactJWS` — The compact JSON Web Signature (JWS) string for the operation.

- `options` — A set of purchase options.

## Return Value

The result of the purchase.

## Discussion

> [!danger] Throws
> A `PurchaseError`, `StoreKitError`, or `InvalidRequest` error.

## See Also

### Initiating purchases

- [PurchaseOption](purchaseoption.md)
- [purchase(compactJWS:confirmIn:options:)](<purchase(compactjws_confirmin_options_)-7x4bh.md>) — Processes a purchase for the product.
- [purchase(compactJWS:confirmIn:options:)](<purchase(compactjws_confirmin_options_)-54lkw.md>) — Processes a purchase for the product.
- [PurchaseResult](purchaseresult.md)

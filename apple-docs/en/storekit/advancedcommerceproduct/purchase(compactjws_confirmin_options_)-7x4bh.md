---
title: 'purchase(compactJWS:confirmIn:options:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 15.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/advancedcommerceproduct/purchase(compactjws:confirmin:options:)-7x4bh'
source_url: 'https://developer.apple.com/documentation/storekit/advancedcommerceproduct/purchase(compactjws:confirmin:options:)-7x4bh'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/advancedcommerceproduct/purchase%28compactjws%3Aconfirmin%3Aoptions%3A%29-7x4bh.json'
content_hash: 'sha256:ac64d8fe86069b06'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [AdvancedCommerceProduct](../advancedcommerceproduct.md)

# purchase(compactJWS:confirmIn:options:)

<sub>Instance Method</sub>

Processes a purchase for the product.

<sub>macOS</sub>

```swift
func purchase(compactJWS: String, confirmIn window: NSWindow, options: Set<AdvancedCommerceProduct.PurchaseOption> = []) async throws -> AdvancedCommerceProduct.PurchaseResult
```

## Parameters

- `compactJWS` — The compact JSON Web Signature (JWS) string for the operation.

- `window` — The window the system uses to display purchase confirmation UI in proximity to.

- `options` — A set of purchase options.

## Return Value

The result of the purchase.

## Discussion

> [!danger] Throws
> A `PurchaseError`, `StoreKitError`, or `InvalidRequest` error.

## See Also

### Initiating purchases

- [PurchaseOption](purchaseoption.md)
- [purchase(compactJWS:confirmIn:options:)](<purchase(compactjws_confirmin_options_)-54lkw.md>) — Processes a purchase for the product.
- [purchase(compactJWS:options:)](<purchase(compactjws_options_).md>) — Processes a purchase for the product.
- [PurchaseResult](purchaseresult.md)

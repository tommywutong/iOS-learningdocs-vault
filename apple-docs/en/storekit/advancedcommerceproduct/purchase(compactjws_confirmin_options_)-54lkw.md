---
title: 'purchase(compactJWS:confirmIn:options:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.4+, iPadOS 18.4+, tvOS 18.4+, visionOS 2.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/advancedcommerceproduct/purchase(compactjws:confirmin:options:)-54lkw'
source_url: 'https://developer.apple.com/documentation/storekit/advancedcommerceproduct/purchase(compactjws:confirmin:options:)-54lkw'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/advancedcommerceproduct/purchase%28compactjws%3Aconfirmin%3Aoptions%3A%29-54lkw.json'
content_hash: 'sha256:03c4d60518378b72'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [AdvancedCommerceProduct](../advancedcommerceproduct.md)

# purchase(compactJWS:confirmIn:options:)

<sub>Instance Method</sub>

Processes a purchase for the product.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func purchase(compactJWS: String, confirmIn viewController: UIViewController, options: Set<AdvancedCommerceProduct.PurchaseOption> = []) async throws -> AdvancedCommerceProduct.PurchaseResult
```

## Parameters

- `compactJWS` — The compact JSON Web Signature (JWS) string for the operation.

- `viewController` — The window the system uses to display purchase confirmation UI in proximity to.

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
- [purchase(compactJWS:options:)](<purchase(compactjws_options_).md>) — Processes a purchase for the product.
- [PurchaseResult](purchaseresult.md)

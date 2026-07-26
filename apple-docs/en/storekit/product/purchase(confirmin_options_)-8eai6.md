---
title: 'purchase(confirmIn:options:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 15.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/product/purchase(confirmin:options:)-8eai6'
source_url: 'https://developer.apple.com/documentation/storekit/product/purchase(confirmin:options:)-8eai6'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/purchase%28confirmin%3Aoptions%3A%29-8eai6.json'
content_hash: 'sha256:dc20e4f472569a65'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Product](../product.md)

# purchase(confirmIn:options:)

<sub>Instance Method</sub>

Processes a purchase for the product.

<sub>macOS</sub>

```swift
func purchase(confirmIn window: NSWindow, options: Set<Product.PurchaseOption> = []) async throws -> Product.PurchaseResult
```

## Parameters

- `window` — The window to show purchase confirmation UI in proximity to.

- `options` — A set of options to configure the purchase.

## Return Value

The result of the purchase

## Discussion

> [!danger] Throws
> A `PurchaseError` or `StoreKitError`.

## See Also

### Purchasing a product

- [purchase(options:)](<purchase(options_).md>) — Initiates a purchase for the product with the App Store and displays the confirmation sheet.
- [purchase(confirmIn:options:)](<purchase(confirmin_options_)-6dj6y.md>) — Initiates a purchase for the product with the App Store and displays the confirmation sheet.
- [purchase(confirmIn:options:)](<purchase(confirmin_options_)-3bivf.md>) — Processes a purchase for the product.
- [PurchaseOption](purchaseoption.md) — Optional settings for a product purchase that add account information, purchase details, and offers, or that specify behaviors.
- [PurchaseResult](purchaseresult.md) — The result of a purchase.
- [PurchaseError](purchaseerror.md) — Error information for product purchase errors.

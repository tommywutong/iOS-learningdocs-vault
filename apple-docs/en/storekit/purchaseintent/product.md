---
title: product
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 14.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/purchaseintent/product
source_url: 'https://developer.apple.com/documentation/storekit/purchaseintent/product'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/purchaseintent/product.json'
content_hash: 'sha256:43c04a6ee76d2aa0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [PurchaseIntent](../purchaseintent.md)

# product

<sub>Instance Property</sub>

The product information of the In-App Purchase the customer selects to purchase outside of the app.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
let product: Product
```

## Discussion

To enable users to complete the purchase they start on the App Store, call [purchase(options:)](<../product/purchase(options_).md>) on this product instance.

## See Also

### Identifying the product

- [id](id.md) — The product identifier of the In-App Purchase that the customer selects to purchase outside of the app.

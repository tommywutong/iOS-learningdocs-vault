---
title: id
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 14.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/purchaseintent/id
source_url: 'https://developer.apple.com/documentation/storekit/purchaseintent/id'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/purchaseintent/id.json'
content_hash: 'sha256:653bfd383a35623f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [PurchaseIntent](../purchaseintent.md)

# id

<sub>Instance Property</sub>

The product identifier of the In-App Purchase that the customer selects to purchase outside of the app.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
@backDeployed(before: iOS 18.0, macOS 15.0, macCatalyst 18.0)
var id: Product.ID { get }
```

## See Also

### Identifying the product

- [product](product.md) — The product information of the In-App Purchase the customer selects to purchase outside of the app.

---
title: products
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/collectiontaskstate/products
source_url: 'https://developer.apple.com/documentation/storekit/product/collectiontaskstate/products'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/collectiontaskstate/products.json'
content_hash: 'sha256:b01e10d9c0f0a7c4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [CollectionTaskState](../collectiontaskstate.md)

# products

<sub>Instance Property</sub>

An array of available products if the task was successful.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var products: [Product]? { get }
```

## Discussion

Use this as a convenience to access the products in code that doesn’t depend on the reason the reason a product can’t be accessed. The value is `nil` while the task is loading, or if the task fails.

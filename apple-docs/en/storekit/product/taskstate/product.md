---
title: product
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/taskstate/product
source_url: 'https://developer.apple.com/documentation/storekit/product/taskstate/product'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/taskstate/product.json'
content_hash: 'sha256:b818437b471d0859'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [TaskState](../taskstate.md)

# product

<sub>Instance Property</sub>

The product value if the task was successful.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var product: Product? { get }
```

## Discussion

Use this as a convenience to access the product value in code that doesn’t depend on the reason the product can’t be accessed. The value is `nil` while the product is loading, or if the product can’t be accessed for any reason.

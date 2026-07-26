---
title: 'Product.TaskState.failure(_:)'
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/product/taskstate/failure(_:)'
source_url: 'https://developer.apple.com/documentation/storekit/product/taskstate/failure(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/taskstate/failure%28_%3A%29.json'
content_hash: 'sha256:a768c92d94ecad6c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [TaskState](../taskstate.md)

# Product.TaskState.failure(_:)

<sub>Case</sub>

The task failed with an error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case failure(any Error)
```

## See Also

### Task states

- [Product.TaskState.loading](loading.md) — The task is loading the product in the background.
- [Product.TaskState.success(_:)](<success(__).md>) — The task successfully loaded the product.
- [Product.TaskState.unavailable](unavailable.md) — The product is unavailable in the current storefront.

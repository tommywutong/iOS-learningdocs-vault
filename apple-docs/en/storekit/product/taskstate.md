---
title: Product.TaskState
framework: StoreKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/taskstate
source_url: 'https://developer.apple.com/documentation/storekit/product/taskstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/taskstate.json'
content_hash: 'sha256:f90ce0397c4383d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Product](../product.md)

# Product.TaskState

<sub>Enumeration</sub>

The state of a task that loads a product in the background.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum TaskState
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Task states

- [Product.TaskState.loading](taskstate/loading.md) — The task is loading the product in the background.
- [Product.TaskState.success(_:)](<taskstate/success(__).md>) — The task successfully loaded the product.
- [Product.TaskState.unavailable](taskstate/unavailable.md) — The product is unavailable in the current storefront.
- [Product.TaskState.failure(_:)](<taskstate/failure(__).md>) — The task failed with an error.

### Instance Properties

- [product](taskstate/product.md) — The product value if the task was successful.

## See Also

### Loading products

- [CollectionTaskState](collectiontaskstate.md) — The state of a task that loads a collection of products in the background.

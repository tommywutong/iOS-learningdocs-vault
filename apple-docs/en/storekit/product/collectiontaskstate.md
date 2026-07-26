---
title: Product.CollectionTaskState
framework: StoreKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/collectiontaskstate
source_url: 'https://developer.apple.com/documentation/storekit/product/collectiontaskstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/collectiontaskstate.json'
content_hash: 'sha256:51a844256475c13c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Product](../product.md)

# Product.CollectionTaskState

<sub>Enumeration</sub>

The state of a task that loads a collection of products in the background.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CollectionTaskState
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Collection task states

- [Product.CollectionTaskState.loading](collectiontaskstate/loading.md) — The task is loading the collection in the background.
- [Product.CollectionTaskState.success(_:unavailable:)](<collectiontaskstate/success(__unavailable_).md>) — The task completed loading the collection.
- [Product.CollectionTaskState.failure(_:)](<collectiontaskstate/failure(__).md>) — The task failed with an error.

### Instance Properties

- [products](collectiontaskstate/products.md) — An array of available products if the task was successful.

## See Also

### Loading products

- [TaskState](taskstate.md) — The state of a task that loads a product in the background.

---
title: 'Product.CollectionTaskState.failure(_:)'
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/product/collectiontaskstate/failure(_:)'
source_url: 'https://developer.apple.com/documentation/storekit/product/collectiontaskstate/failure(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/collectiontaskstate/failure%28_%3A%29.json'
content_hash: 'sha256:6b742cc6f1a33051'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [CollectionTaskState](../collectiontaskstate.md)

# Product.CollectionTaskState.failure(_:)

<sub>Case</sub>

The task failed with an error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case failure(any Error)
```

## See Also

### Collection task states

- [Product.CollectionTaskState.loading](loading.md) — The task is loading the collection in the background.
- [Product.CollectionTaskState.success(_:unavailable:)](<success(__unavailable_).md>) — The task completed loading the collection.

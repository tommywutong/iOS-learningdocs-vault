---
title: 'Product.CollectionTaskState.success(_:unavailable:)'
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/product/collectiontaskstate/success(_:unavailable:)'
source_url: 'https://developer.apple.com/documentation/storekit/product/collectiontaskstate/success(_:unavailable:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/collectiontaskstate/success%28_%3Aunavailable%3A%29.json'
content_hash: 'sha256:6c60effdee0b7357'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [CollectionTaskState](../collectiontaskstate.md)

# Product.CollectionTaskState.success(_:unavailable:)

<sub>Case</sub>

The task completed loading the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case success([Product], unavailable: [Product.ID])
```

## See Also

### Collection task states

- [Product.CollectionTaskState.loading](loading.md) — The task is loading the collection in the background.
- [Product.CollectionTaskState.failure(_:)](<failure(__).md>) — The task failed with an error.

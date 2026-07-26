---
title: prefetchDataSource
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionview/prefetchdatasource
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/prefetchdatasource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/prefetchdatasource.json'
content_hash: 'sha256:3abd049bf3b95497'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# prefetchDataSource

<sub>Instance Property</sub>

The object that acts as the prefetching data source for the collection view, receiving notifications of upcoming cell data requirements.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var prefetchDataSource: (any UICollectionViewDataSourcePrefetching)? { get set }
```

## Discussion

Assign an object that conforms to the [UICollectionViewDataSourcePrefetching](../uicollectionviewdatasourceprefetching.md) protocol to facilitate prefetching of data for cells to be displayed in the near future. To disable data prefetching behavior, set this property to `nil`.

## See Also

### Prefetching collection view cells and data

- [prefetchingEnabled](isprefetchingenabled.md) — A Boolean value that indicates whether cell and data prefetching are enabled.
- [UICollectionViewDataSourcePrefetching](../uicollectionviewdatasourceprefetching.md) — A protocol that provides advance warning of the data requirements for a collection view, allowing the triggering of asynchronous data load operations.

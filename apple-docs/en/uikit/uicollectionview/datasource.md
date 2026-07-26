---
title: dataSource
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionview/datasource
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/datasource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/datasource.json'
content_hash: 'sha256:d6ca7627b03e93c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# dataSource

<sub>Instance Property</sub>

The object that provides the data for the collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var dataSource: (any UICollectionViewDataSource)? { get set }
```

## Discussion

The data source must adopt the [UICollectionViewDataSource](../uicollectionviewdatasource.md) protocol. The collection view maintains a weak reference to the data source object.

## See Also

### Providing the collection view data

- [UICollectionViewDiffableDataSource](../uicollectionviewdiffabledatasource-9tqpa.md) — The object you use to manage data and provide cells for a collection view.
- [UICollectionViewDataSource](../uicollectionviewdatasource.md) — The methods adopted by the object you use to manage data and provide cells for a collection view.
- [Building high-performance lists and collection views](../building-high-performance-lists-and-collection-views.md) — Improve the performance of lists and collections in your app with prefetching and image preparation.

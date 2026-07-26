---
title: 'collectionView(_:prefetchItemsAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdatasourceprefetching/collectionview(_:prefetchitemsat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdatasourceprefetching/collectionview(_:prefetchitemsat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdatasourceprefetching/collectionview%28_%3Aprefetchitemsat%3A%29.json'
content_hash: 'sha256:4b99eeb8f3b8c034'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDataSourcePrefetching](../uicollectionviewdatasourceprefetching.md)

# collectionView(_:prefetchItemsAt:)

<sub>Instance Method</sub>

Tells your prefetch data source object to begin preparing data for the cells at the supplied index paths.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func collectionView(_ collectionView: UICollectionView, prefetchItemsAt indexPaths: [IndexPath])
```

## Parameters

- `collectionView` — The collection view issuing the prefetch request.

- `indexPaths` — The index paths that specify the locations of the items for which the data is to be prefetched.

## Discussion

The collection view calls this method as the user scrolls, providing the index paths for cells it’s likely to display in the near future. Your implementation of this method is responsible for starting any expensive data loading processes. The data loading must be performed asynchronously, and the results made available to the [- collectionView:cellForItemAtIndexPath:](<../uicollectionviewdatasource/collectionview(__cellforitemat_).md>) method on the collection view’s data source.

The collection view doesn’t call this method for cells it requires immediately, so your code must not rely on this method to load data. The order of the index paths provided represents the priority.

For further information about creating an asynchronous data loading task, see [Concurrency Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008091).

## See Also

### Managing data prefetching

- [Prefetching collection view data](../prefetching-collection-view-data.md) — Load data for collection view cells before they display.
- [- collectionView:cancelPrefetchingForItemsAtIndexPaths:](<collectionview(__cancelprefetchingforitemsat_).md>) — Cancels a previously triggered data prefetch request.

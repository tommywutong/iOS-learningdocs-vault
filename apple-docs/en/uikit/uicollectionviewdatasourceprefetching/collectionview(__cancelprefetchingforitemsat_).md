---
title: 'collectionView(_:cancelPrefetchingForItemsAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdatasourceprefetching/collectionview(_:cancelprefetchingforitemsat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdatasourceprefetching/collectionview(_:cancelprefetchingforitemsat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdatasourceprefetching/collectionview%28_%3Acancelprefetchingforitemsat%3A%29.json'
content_hash: 'sha256:23843e267dd5247a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDataSourcePrefetching](../uicollectionviewdatasourceprefetching.md)

# collectionView(_:cancelPrefetchingForItemsAt:)

<sub>Instance Method</sub>

Cancels a previously triggered data prefetch request.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, cancelPrefetchingForItemsAt indexPaths: [IndexPath])
```

## Parameters

- `collectionView` — The collection view issuing the cancellation of the prefetch request.

- `indexPaths` — The index paths that specify the locations of the items for which data is no longer required.

## Discussion

The collection view calls this method to cancel prefetch requests as cells scroll out of view. Your implementation of this method is responsible for canceling the operations initiated by a previous call to [- collectionView:prefetchItemsAtIndexPaths:](<collectionview(__prefetchitemsat_).md>). For further information about canceling an asynchronous data loading task, see [Concurrency Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008091).

## See Also

### Managing data prefetching

- [Prefetching collection view data](../prefetching-collection-view-data.md) — Load data for collection view cells before they display.
- [- collectionView:prefetchItemsAtIndexPaths:](<collectionview(__prefetchitemsat_).md>) — Tells your prefetch data source object to begin preparing data for the cells at the supplied index paths.

---
title: isPrefetchingEnabled
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionview/isprefetchingenabled
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/isprefetchingenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/isprefetchingenabled.json'
content_hash: 'sha256:641139dbeeb49ff1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# isPrefetchingEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether cell and data prefetching are enabled.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isPrefetchingEnabled: Bool { get set }
```

## Discussion

When [true](../../swift/true.md), the collection view requests cells in advance of when they will be displayed, spreading the rendering over multiple layout passes. When [false](../../swift/false.md), the cells are requested as they are needed for display, often with multiple cells being requested in the same render loop. Setting this property to [false](../../swift/false.md) also disables data prefetching. The default value of this property is [true](../../swift/true.md).

> [!note] Note
> When prefetching is enabled the [- collectionView:cellForItemAtIndexPath:](<../uicollectionviewdatasource/collectionview(__cellforitemat_).md>) method on the collection view delegate is called in advance of when the cell is required. To avoid inconsistencies in the visual appearance, use the [- collectionView:willDisplayCell:forItemAtIndexPath:](<../uicollectionviewdelegate/collectionview(__willdisplay_foritemat_).md>) delegate method to update the cell to reflect visual state such as selection.

## See Also

### Prefetching collection view cells and data

- [prefetchDataSource](prefetchdatasource.md) — The object that acts as the prefetching data source for the collection view, receiving notifications of upcoming cell data requirements.
- [UICollectionViewDataSourcePrefetching](../uicollectionviewdatasourceprefetching.md) — A protocol that provides advance warning of the data requirements for a collection view, allowing the triggering of asynchronous data load operations.

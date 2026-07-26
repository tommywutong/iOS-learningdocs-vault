---
title: UICollectionViewDiffableDataSource.CellProvider
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/cellprovider
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/cellprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/cellprovider.json'
content_hash: 'sha256:b0184f0eb5b43d96'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDiffableDataSource](../uicollectionviewdiffabledatasource-9tqpa.md)

# UICollectionViewDiffableDataSource.CellProvider

<sub>Type Alias</sub>

A closure that configures and returns a cell for a collection view from its diffable data source.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
typealias CellProvider = (UICollectionView, IndexPath, ItemIdentifierType) -> UICollectionViewCell?
```

## Parameters

- `collectionView` — The collection view to configure this cell for.

- `indexPath` — The index path that specifies the location of the cell in the collection view.

- `itemIdentifier` — An object, with a type that implements the [Hashable](../../swift/hashable.md) protocol, the data source uses to uniquely identify the item for this cell.

## Return Value

A non-`nil` configured cell object. The cell provider must return a valid cell object to the collection view.

## Discussion

You use this closure to configure and return cells when creating a diffable data source using [init(collectionView:cellProvider:)](<init(collectionview_cellprovider_).md>).

## See Also

### Related Documentation

- [UICollectionViewDiffableDataSourceReference](../uicollectionviewdiffabledatasourcereference.md) — The object you use to manage data and provide cells for a collection view.
- [Updating collection views using diffable data sources](../updating-collection-views-using-diffable-data-sources.md) — Streamline the display and update of data in a collection view using a diffable data source that contains identifiers.
- [Implementing modern collection views](../implementing-modern-collection-views.md) — Bring compositional layouts to your app and simplify updating your user interface with diffable data sources.

### Creating a diffable data source

- [init(collectionView:cellProvider:)](<init(collectionview_cellprovider_).md>) — Creates a diffable data source with the specified cell provider, and connects it to the specified collection view.

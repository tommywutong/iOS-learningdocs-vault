---
title: UICollectionViewDiffableDataSourceReferenceCellProvider
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdiffabledatasourcereferencecellprovider
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasourcereferencecellprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdiffabledatasourcereferencecellprovider.json'
content_hash: 'sha256:2fff94c0871d58b9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICollectionViewDiffableDataSourceReferenceCellProvider

<sub>Type Alias</sub>

A closure that configures and returns a cell for a collection view from its diffable data source.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
typealias UICollectionViewDiffableDataSourceReferenceCellProvider = (UICollectionView, IndexPath, Any) -> UICollectionViewCell?
```

## Parameters

- `collectionView` — The collection view to configure this cell for.

- `indexPath` — The index path that specifies the location of the cell in the collection view.

- `identifier` — The identifier of the item for this cell.

## Return Value

A non-`nil` configured cell object. The cell provider must return a valid cell object to the collection view.

## See Also

### Creating a diffable data source

- [- initWithCollectionView:cellProvider:](<uicollectionviewdiffabledatasourcereference/init(collectionview_cellprovider_).md>) — Creates a diffable data source with the specified cell provider, and connects it to the specified collection view.

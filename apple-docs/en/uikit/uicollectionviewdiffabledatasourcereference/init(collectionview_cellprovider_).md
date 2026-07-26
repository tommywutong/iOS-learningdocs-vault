---
title: 'init(collectionView:cellProvider:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdiffabledatasourcereference/init(collectionview:cellprovider:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasourcereference/init(collectionview:cellprovider:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdiffabledatasourcereference/init%28collectionview%3Acellprovider%3A%29.json'
content_hash: 'sha256:bda5c83c19eaf12e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDiffableDataSourceReference](../uicollectionviewdiffabledatasourcereference.md)

# init(collectionView:cellProvider:)

<sub>Initializer</sub>

Creates a diffable data source with the specified cell provider, and connects it to the specified collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(collectionView: UICollectionView, cellProvider: @escaping UICollectionViewDiffableDataSourceReferenceCellProvider)
```

## Parameters

- `collectionView` — The initialized collection view object to connect to the diffable data source.

- `cellProvider` — A closure that creates and returns each of the cells for the collection view from the data the diffable data source provides.

## Discussion

To connect a diffable data source to a collection view, you create the diffable data source using this initializer, passing in the collection view you want to associate with that data source. You also pass in a cell provider, where you configure each of your cells to determine how to display your data in the UI.

```objc
self.dataSource = [[UICollectionViewDiffableDataSource alloc] initWithCollectionView:self.collectionView cellProvider:^UICollectionViewCell *(UICollectionView *collectionView, NSIndexPath *indexPath, id item) {
    // configure and return cell
}];
```

## See Also

### Creating a diffable data source

- [UICollectionViewDiffableDataSourceReferenceCellProvider](../uicollectionviewdiffabledatasourcereferencecellprovider.md) — A closure that configures and returns a cell for a collection view from its diffable data source.

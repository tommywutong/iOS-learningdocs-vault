---
title: UICollectionViewDiffableDataSource.SupplementaryViewProvider
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/supplementaryviewprovider-swift.typealias
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/supplementaryviewprovider-swift.typealias'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/supplementaryviewprovider-swift.typealias.json'
content_hash: 'sha256:b158bed8e0223a04'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDiffableDataSource](../uicollectionviewdiffabledatasource-9tqpa.md)

# UICollectionViewDiffableDataSource.SupplementaryViewProvider

<sub>Type Alias</sub>

A closure that configures and returns a collection view’s supplementary view, such as a header or footer, from a diffable data source.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
typealias SupplementaryViewProvider = (UICollectionView, String, IndexPath) -> UICollectionReusableView?
```

## Parameters

- `collectionView` — The collection view to configure this supplementary view for.

- `kind` — The kind of supplementary view to provide. The layout object that supports the supplementary view defines the value of this string.

- `indexPath` — The index path that specifies the location of the supplementary view in the collection view.

## Return Value

A non-`nil` configured supplementary view object. The supplementary view provider must return a valid view object to the collection view.

## See Also

### Creating supplementary views

- [supplementaryViewProvider](supplementaryviewprovider-swift.property.md) — The closure that configures and returns the collection view’s supplementary views, such as headers and footers, from the diffable data source.

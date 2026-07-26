---
title: UICollectionViewDiffableDataSourceReferenceSupplementaryViewProvider
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdiffabledatasourcereferencesupplementaryviewprovider
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasourcereferencesupplementaryviewprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdiffabledatasourcereferencesupplementaryviewprovider.json'
content_hash: 'sha256:b42d700cf395aac2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICollectionViewDiffableDataSourceReferenceSupplementaryViewProvider

<sub>Type Alias</sub>

A closure that configures and returns a collection view’s supplementary view, such as a header or footer, from a diffable data source.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
typealias UICollectionViewDiffableDataSourceReferenceSupplementaryViewProvider = (UICollectionView, String, IndexPath) -> UICollectionReusableView?
```

## Parameters

- `collectionView` — The collection view to configure this supplementary view for.

- `kind` — The kind of supplementary view to provide. The layout object that supports the supplementary view defines the value of this string.

- `indexPath` — The index path that specifies the location of the supplementary view in the collection view.

## Return Value

A non-`nil` configured supplementary view object. The supplementary view provider must return a valid view object to the collection view.

## See Also

### Creating supplementary views

- [supplementaryViewProvider](uicollectionviewdiffabledatasourcereference/supplementaryviewprovider.md) — The closure that configures and returns the collection view’s supplementary views, such as headers and footers, from the diffable data source.

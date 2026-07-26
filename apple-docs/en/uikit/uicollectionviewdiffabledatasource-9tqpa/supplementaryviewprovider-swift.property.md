---
title: supplementaryViewProvider
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/supplementaryviewprovider-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/supplementaryviewprovider-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/supplementaryviewprovider-swift.property.json'
content_hash: 'sha256:91623ababdf97774'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDiffableDataSource](../uicollectionviewdiffabledatasource-9tqpa.md)

# supplementaryViewProvider

<sub>Instance Property</sub>

The closure that configures and returns the collection view’s supplementary views, such as headers and footers, from the diffable data source.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency var supplementaryViewProvider: UICollectionViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType>.SupplementaryViewProvider? { get set }
```

## See Also

### Creating supplementary views

- [SupplementaryViewProvider](supplementaryviewprovider-swift.typealias.md) — A closure that configures and returns a collection view’s supplementary view, such as a header or footer, from a diffable data source.

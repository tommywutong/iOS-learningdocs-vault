---
title: 'numberOfSections(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdatasource/numberofsections(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdatasource/numberofsections(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdatasource/numberofsections%28in%3A%29.json'
content_hash: 'sha256:b141e0d1cd88fd77'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDataSource](../uicollectionviewdatasource.md)

# numberOfSections(in:)

<sub>Instance Method</sub>

Asks your data source object for the number of sections in the collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func numberOfSections(in collectionView: UICollectionView) -> Int
```

## Parameters

- `collectionView` — The collection view requesting this information.

## Return Value

The number of sections in `collectionView`.

## Discussion

If you don’t implement this method, the collection view uses a default value of 1.

## See Also

### Getting item and section metrics

- [- collectionView:numberOfItemsInSection:](<collectionview(__numberofitemsinsection_).md>) — Asks your data source object for the number of items in the specified section.

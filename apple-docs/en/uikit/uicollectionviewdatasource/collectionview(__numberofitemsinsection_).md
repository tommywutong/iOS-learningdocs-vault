---
title: 'collectionView(_:numberOfItemsInSection:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdatasource/collectionview(_:numberofitemsinsection:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdatasource/collectionview(_:numberofitemsinsection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdatasource/collectionview%28_%3Anumberofitemsinsection%3A%29.json'
content_hash: 'sha256:3a8a5b2c6309198c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDataSource](../uicollectionviewdatasource.md)

# collectionView(_:numberOfItemsInSection:)

<sub>Instance Method</sub>

Asks your data source object for the number of items in the specified section.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int
```

## Parameters

- `collectionView` — The collection view requesting this information.

- `section` — An index number identifying a section in `collectionView`. This index value is 0-based.

## Return Value

The number of items in `section`.

## See Also

### Getting item and section metrics

- [- numberOfSectionsInCollectionView:](<numberofsections(in_).md>) — Asks your data source object for the number of sections in the collection view.

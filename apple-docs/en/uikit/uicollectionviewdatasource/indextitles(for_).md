---
title: 'indexTitles(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 10.2+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdatasource/indextitles(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdatasource/indextitles(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdatasource/indextitles%28for%3A%29.json'
content_hash: 'sha256:a8551c832f88a128'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDataSource](../uicollectionviewdatasource.md)

# indexTitles(for:)

<sub>Instance Method</sub>

Asks the data source to return the titles for the index items to display for the collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func indexTitles(for collectionView: UICollectionView) -> [String]?
```

## Parameters

- `collectionView` — The collection view requesting this information.

## Return Value

An array of strings to use for the title of each index entry. For example, you might return an array of strings containing the letters of the alphabet (`["A", "B", "C", ..., "Z"]`).

## Discussion

Use this method to support fast scrolling through your collection view’s content. The strings you return are displayed in an index view that can be used to jump to specific locations in the collection view’s content. If you implement this method, you must also implement the [- collectionView:indexPathForIndexTitle:atIndex:](<collectionview(__indexpathforindextitle_at_).md>) method to specify the collection view item associated with each index title.

## See Also

### Configuring an index

- [- collectionView:indexPathForIndexTitle:atIndex:](<collectionview(__indexpathforindextitle_at_).md>) — Asks the data source to return the index path of a collection view item that corresponds to one of your index entries.

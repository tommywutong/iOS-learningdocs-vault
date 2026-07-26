---
title: 'collectionView(_:indexPathForIndexTitle:at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 10.2+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdatasource/collectionview(_:indexpathforindextitle:at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdatasource/collectionview(_:indexpathforindextitle:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdatasource/collectionview%28_%3Aindexpathforindextitle%3Aat%3A%29.json'
content_hash: 'sha256:9fb89e421ef0619e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDataSource](../uicollectionviewdatasource.md)

# collectionView(_:indexPathForIndexTitle:at:)

<sub>Instance Method</sub>

Asks the data source to return the index path of a collection view item that corresponds to one of your index entries.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, indexPathForIndexTitle title: String, at index: Int) -> IndexPath
```

## Parameters

- `collectionView` — The collection view requesting this information.

- `title` — The title of the index item. This string corresponds to one of the strings you returned in your [- indexTitlesForCollectionView:](<indextitles(for_).md>) method.

- `index` — The index into the array returned by the [- indexTitlesForCollectionView:](<indextitles(for_).md>) method that corresponds to the index title.

## Return Value

The index path for the collection view item that should appear when the user selects the index.

## Discussion

Use this method to support fast scrolling through your collection view’s content. After returning a set of index strings from your [- indexTitlesForCollectionView:](<indextitles(for_).md>) method, the collection view calls this method for each string to fetch the collection view item to use as the scrolling destination.

## See Also

### Configuring an index

- [- indexTitlesForCollectionView:](<indextitles(for_).md>) — Asks the data source to return the titles for the index items to display for the collection view.

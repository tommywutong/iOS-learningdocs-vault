---
title: 'indexPath(forSupplementaryView:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/indexpath(forsupplementaryview:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/indexpath(forsupplementaryview:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/indexpath%28forsupplementaryview%3A%29.json'
content_hash: 'sha256:41709fa4ada05f74'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# indexPath(forSupplementaryView:)

<sub>Instance Method</sub>

Gets the index path of the specified supplementary view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func indexPath(forSupplementaryView supplementaryView: UICollectionReusableView) -> IndexPath?
```

## Parameters

- `supplementaryView` — The supplementary or decoration view whose index path you want.

## Return Value

The index path of the specified view if it is in the collection view, else `nil`.

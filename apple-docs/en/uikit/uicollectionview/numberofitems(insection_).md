---
title: 'numberOfItems(inSection:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/numberofitems(insection:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/numberofitems(insection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/numberofitems%28insection%3A%29.json'
content_hash: 'sha256:415cd2d519ba9f01'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# numberOfItems(inSection:)

<sub>Instance Method</sub>

Fetches the count of items in the specified section.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func numberOfItems(inSection section: Int) -> Int
```

## Parameters

- `section` — The index of the section for which you want a count of the items.

## Return Value

The number of items in the specified section.

## See Also

### Getting the state of the collection view

- [numberOfSections](numberofsections.md) — The number of sections displayed by the collection view.
- [visibleCells](visiblecells.md) — An array of visible cells currently displayed by the collection view.

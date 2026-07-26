---
title: visibleCells
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionview/visiblecells
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/visiblecells'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/visiblecells.json'
content_hash: 'sha256:33ef827e0a27d86e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# visibleCells

<sub>Instance Property</sub>

An array of visible cells currently displayed by the collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var visibleCells: [UICollectionViewCell] { get }
```

## Return Value

An array of [UICollectionViewCell](../uicollectionviewcell.md) objects. If no cells are visible, this method returns an empty array.

## Discussion

This method returns the complete list of visible cells displayed by the collection view.

## See Also

### Related Documentation

- [indexPathsForVisibleItems](indexpathsforvisibleitems.md) — An array of the visible items in the collection view.

### Getting the state of the collection view

- [numberOfSections](numberofsections.md) — The number of sections displayed by the collection view.
- [- numberOfItemsInSection:](<numberofitems(insection_).md>) — Fetches the count of items in the specified section.

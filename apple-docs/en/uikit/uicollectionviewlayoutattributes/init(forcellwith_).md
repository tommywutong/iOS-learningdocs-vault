---
title: 'init(forCellWith:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewlayoutattributes/init(forcellwith:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/init(forcellwith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayoutattributes/init%28forcellwith%3A%29.json'
content_hash: 'sha256:0eeba9bc7577ff78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayoutAttributes](../uicollectionviewlayoutattributes.md)

# init(forCellWith:)

<sub>Initializer</sub>

Creates and returns a layout attributes object that represents a cell with the specified index path.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(forCellWith indexPath: IndexPath)
```

## Parameters

- `indexPath` — The index path of the cell.

## Return Value

A new layout attributes object whose precise type matches the type of the class used to call this method.

## Discussion

Use this method to create a layout attributes object for a cell in the collection view. Cells are the main type of view presented by a collection view. The index path for a cell typically includes both a section index and an item index for locating the cell’s contents in the collection view’s data source.

## See Also

### Creating layout attributes

- [+ layoutAttributesForSupplementaryViewOfKind:withIndexPath:](<init(forsupplementaryviewofkind_with_).md>) — Creates and returns a layout attributes object that represents the specified supplementary view.
- [+ layoutAttributesForDecorationViewOfKind:withIndexPath:](<init(fordecorationviewofkind_with_).md>) — Creates and returns a layout attributes object that represents the specified decoration view.

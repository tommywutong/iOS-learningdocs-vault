---
title: 'init(forSupplementaryViewOfKind:with:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewlayoutattributes/init(forsupplementaryviewofkind:with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/init(forsupplementaryviewofkind:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayoutattributes/init%28forsupplementaryviewofkind%3Awith%3A%29.json'
content_hash: 'sha256:17c91ec62550f6a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayoutAttributes](../uicollectionviewlayoutattributes.md)

# init(forSupplementaryViewOfKind:with:)

<sub>Initializer</sub>

Creates and returns a layout attributes object that represents the specified supplementary view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(forSupplementaryViewOfKind elementKind: String, with indexPath: IndexPath)
```

## Parameters

- `elementKind` — A string that identifies the type of supplementary view.

- `indexPath` — The index path of the view.

## Return Value

A new layout attributes object whose precise type matches the type of the class used to call this method.

## Discussion

Use this method to create a layout attributes object for a supplementary view in the collection view. Like cells, supplementary views present data that is managed by the collection view’s data source. But unlike cells, supplementary views are typically designed for a special purpose. For example, header and footer views are laid out differently than cells and can be provided for individual sections or for the collection view as a whole.

It is up to you to decide how to use the `indexPath` parameter to identify a given supplementary view. Typically, you use the `elementKind` parameter to identify the type of the supplementary view and the `indexPath` information to distinguish between different instances of that view.

## See Also

### Creating layout attributes

- [+ layoutAttributesForCellWithIndexPath:](<init(forcellwith_).md>) — Creates and returns a layout attributes object that represents a cell with the specified index path.
- [+ layoutAttributesForDecorationViewOfKind:withIndexPath:](<init(fordecorationviewofkind_with_).md>) — Creates and returns a layout attributes object that represents the specified decoration view.

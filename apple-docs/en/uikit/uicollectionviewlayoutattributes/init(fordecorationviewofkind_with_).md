---
title: 'init(forDecorationViewOfKind:with:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewlayoutattributes/init(fordecorationviewofkind:with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/init(fordecorationviewofkind:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayoutattributes/init%28fordecorationviewofkind%3Awith%3A%29.json'
content_hash: 'sha256:bc2b6edf7bf5cf64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayoutAttributes](../uicollectionviewlayoutattributes.md)

# init(forDecorationViewOfKind:with:)

<sub>Initializer</sub>

Creates and returns a layout attributes object that represents the specified decoration view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(forDecorationViewOfKind decorationViewKind: String, with indexPath: IndexPath)
```

## Parameters

- `decorationViewKind` — The kind identifier for the specified decoration view.

- `indexPath` — An index path related to the decoration view.

## Return Value

A new layout attributes object whose precise type matches the type of the class used to call this method.

## Discussion

Use this method to create a layout attributes object for a decoration view in the collection view. Decoration views are a type of supplementary view but do not present data that is managed by the collection view’s data source. Instead, they mostly present visual adornments for a section or for the entire collection view.

It is up to you to decide how to use the `indexPath` parameter to identify a given decoration view. Typically, you use the `decorationViewKind` parameter to identify the type of the decoration view and the `indexPath` information to distinguish between different instances of that view.

## See Also

### Creating layout attributes

- [+ layoutAttributesForCellWithIndexPath:](<init(forcellwith_).md>) — Creates and returns a layout attributes object that represents a cell with the specified index path.
- [+ layoutAttributesForSupplementaryViewOfKind:withIndexPath:](<init(forsupplementaryviewofkind_with_).md>) — Creates and returns a layout attributes object that represents the specified supplementary view.

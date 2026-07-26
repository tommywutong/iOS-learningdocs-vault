---
title: representedElementKind
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewlayoutattributes/representedelementkind
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/representedelementkind'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayoutattributes/representedelementkind.json'
content_hash: 'sha256:179964288263d29e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayoutAttributes](../uicollectionviewlayoutattributes.md)

# representedElementKind

<sub>Instance Property</sub>

The layout-specific identifier for the target view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var representedElementKind: String? { get }
```

## Discussion

You can use the value in this property to identify the specific purpose of the supplementary or decoration view associated with the attributes. This property is `nil` if the [representedElementCategory](representedelementcategory.md) property contains the value [UICollectionElementCategoryCell](../uicollectionview/elementcategory/cell.md).

## See Also

### Identifying the referenced item

- [indexPath](indexpath.md) — The index path of the item in the collection view.
- [representedElementCategory](representedelementcategory.md) — The type of the item.
- [ElementCategory](../uicollectionview/elementcategory.md) — Constants specifying the type of view.

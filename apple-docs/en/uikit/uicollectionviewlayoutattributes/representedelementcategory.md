---
title: representedElementCategory
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewlayoutattributes/representedelementcategory
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/representedelementcategory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayoutattributes/representedelementcategory.json'
content_hash: 'sha256:6db05592262e488f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayoutAttributes](../uicollectionviewlayoutattributes.md)

# representedElementCategory

<sub>Instance Property</sub>

The type of the item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var representedElementCategory: UICollectionView.ElementCategory { get }
```

## Discussion

You can use the value in this property to distinguish whether the layout attributes are intended for a cell, supplementary view, or decoration view.

## See Also

### Identifying the referenced item

- [indexPath](indexpath.md) — The index path of the item in the collection view.
- [representedElementKind](representedelementkind.md) — The layout-specific identifier for the target view.
- [ElementCategory](../uicollectionview/elementcategory.md) — Constants specifying the type of view.

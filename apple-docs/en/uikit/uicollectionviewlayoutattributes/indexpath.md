---
title: indexPath
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewlayoutattributes/indexpath
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/indexpath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayoutattributes/indexpath.json'
content_hash: 'sha256:3851a789cc3216ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayoutAttributes](../uicollectionviewlayoutattributes.md)

# indexPath

<sub>Instance Property</sub>

The index path of the item in the collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var indexPath: IndexPath { get set }
```

## Discussion

The index path contains the index of the section and the index of the item within that section. These two values uniquely identify the position of the corresponding item in the collection view.

## See Also

### Identifying the referenced item

- [representedElementKind](representedelementkind.md) — The layout-specific identifier for the target view.
- [representedElementCategory](representedelementcategory.md) — The type of the item.
- [ElementCategory](../uicollectionview/elementcategory.md) — Constants specifying the type of view.

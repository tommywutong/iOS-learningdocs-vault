---
title: previewSize
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdropitem/previewsize
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdropitem/previewsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdropitem/previewsize.json'
content_hash: 'sha256:f8741e397a4f090d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDropItem](../uicollectionviewdropitem.md)

# previewSize

<sub>Instance Property</sub>

The size of the drag item’s preview.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var previewSize: CGSize { get }
```

## Discussion

You might use this property when configuring animations. If the item does not have an associated preview, this property is set to `CGSizeZero`.

## See Also

### Getting the Item Information

- [sourceIndexPath](sourceindexpath.md) — The index path of the item in the collection view, if any.

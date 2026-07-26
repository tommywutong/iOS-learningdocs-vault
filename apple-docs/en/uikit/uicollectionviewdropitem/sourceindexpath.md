---
title: sourceIndexPath
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdropitem/sourceindexpath
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdropitem/sourceindexpath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdropitem/sourceindexpath.json'
content_hash: 'sha256:8393ce4566691c17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDropItem](../uicollectionviewdropitem.md)

# sourceIndexPath

<sub>Instance Property</sub>

The index path of the item in the collection view, if any.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var sourceIndexPath: IndexPath? { get }
```

## Discussion

If the item originated from the collection view, this property contains the item’s original index path.

## See Also

### Getting the Item Information

- [previewSize](previewsize.md) — The size of the drag item’s preview.

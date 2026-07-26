---
title: 'reloadItems(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/reloaditems(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/reloaditems(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/reloaditems%28at%3A%29.json'
content_hash: 'sha256:a5915dbc373de5f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# reloadItems(at:)

<sub>Instance Method</sub>

Reloads just the items at the specified index paths.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func reloadItems(at indexPaths: [IndexPath])
```

## Parameters

- `indexPaths` — An array of [NSIndexPath](../../foundation/nsindexpath.md) objects identifying the items you want to update.

## Discussion

Call this method to selectively reload only the specified items. This causes the collection view to discard any cells associated with those items and redisplay them.

## See Also

### Reloading content

- [hasUncommittedUpdates](hasuncommittedupdates.md) — A Boolean value that indicates whether the collection view contains drop placeholders or is reordering its items as part of handling a drop.
- [- reconfigureItemsAtIndexPaths:](<reconfigureitems(at_).md>) — Updates the data for the items at the index paths you specify, preserving the existing cells for the items.
- [- reloadData](<reloaddata().md>) — Reloads all of the data for the collection view.
- [- reloadSections:](<reloadsections(__).md>) — Reloads the data in the specified sections of the collection view.

---
title: 'reloadSections(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/reloadsections(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/reloadsections(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/reloadsections%28_%3A%29.json'
content_hash: 'sha256:98a302d57b272885'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# reloadSections(_:)

<sub>Instance Method</sub>

Reloads the data in the specified sections of the collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func reloadSections(_ sections: IndexSet)
```

## Parameters

- `sections` — The indexes of the sections to reload.

## Discussion

Call this method to selectively reload only the items in the specified sections. This causes the collection view to discard any cells associated with those items and redisplay them. This method also discards any placeholders in the specified sections.

## See Also

### Reloading content

- [hasUncommittedUpdates](hasuncommittedupdates.md) — A Boolean value that indicates whether the collection view contains drop placeholders or is reordering its items as part of handling a drop.
- [- reconfigureItemsAtIndexPaths:](<reconfigureitems(at_).md>) — Updates the data for the items at the index paths you specify, preserving the existing cells for the items.
- [- reloadData](<reloaddata().md>) — Reloads all of the data for the collection view.
- [- reloadItemsAtIndexPaths:](<reloaditems(at_).md>) — Reloads just the items at the specified index paths.

---
title: reloadData()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionview/reloaddata()
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/reloaddata()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/reloaddata%28%29.json'
content_hash: 'sha256:843788179a56e522'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# reloadData()

<sub>Instance Method</sub>

Reloads all of the data for the collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func reloadData()
```

## Discussion

Call this method sparingly when you need to reload all of the items in the collection view. This causes the collection view to discard any currently visible items (including placeholders) and recreate items based on the current state of the data source object. For efficiency, the collection view only displays those cells and supplementary views that are visible. If the collection data shrinks as a result of the reload, the collection view adjusts its scrolling offsets accordingly.

You shouldn’t call this method in the middle of animation blocks where items are being inserted or deleted. Insertions and deletions automatically cause the collection’s data to be updated appropriately.

## See Also

### Reloading content

- [hasUncommittedUpdates](hasuncommittedupdates.md) — A Boolean value that indicates whether the collection view contains drop placeholders or is reordering its items as part of handling a drop.
- [- reconfigureItemsAtIndexPaths:](<reconfigureitems(at_).md>) — Updates the data for the items at the index paths you specify, preserving the existing cells for the items.
- [- reloadSections:](<reloadsections(__).md>) — Reloads the data in the specified sections of the collection view.
- [- reloadItemsAtIndexPaths:](<reloaditems(at_).md>) — Reloads just the items at the specified index paths.

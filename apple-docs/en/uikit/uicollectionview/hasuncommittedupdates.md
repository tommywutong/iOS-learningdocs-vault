---
title: hasUncommittedUpdates
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionview/hasuncommittedupdates
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/hasuncommittedupdates'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/hasuncommittedupdates.json'
content_hash: 'sha256:63c708f70014f197'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# hasUncommittedUpdates

<sub>Instance Property</sub>

A Boolean value that indicates whether the collection view contains drop placeholders or is reordering its items as part of handling a drop.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var hasUncommittedUpdates: Bool { get }
```

## Discussion

When the value of this property is [true](../../swift/true.md), avoid making any significant changes to the collection view. Specifically, don’t reload the collection view’s data, as doing so deletes all placeholders and recreates items from the data source.

## See Also

### Reloading content

- [- reconfigureItemsAtIndexPaths:](<reconfigureitems(at_).md>) — Updates the data for the items at the index paths you specify, preserving the existing cells for the items.
- [- reloadData](<reloaddata().md>) — Reloads all of the data for the collection view.
- [- reloadSections:](<reloadsections(__).md>) — Reloads the data in the specified sections of the collection view.
- [- reloadItemsAtIndexPaths:](<reloaditems(at_).md>) — Reloads just the items at the specified index paths.

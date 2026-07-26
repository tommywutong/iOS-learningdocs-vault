---
title: 'ofParentItem(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdiffabledatasourcesectionsnapshotreference/ofparentitem(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshotreference/ofparentitem(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesectionsnapshotreference/ofparentitem%28_%3A%29.json'
content_hash: 'sha256:16985fbf8d510419'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSectionSnapshotReference](../nsdiffabledatasourcesectionsnapshotreference.md)

# ofParentItem(_:)

<sub>Instance Method</sub>

Creates a section snapshot containing the child items of the specified parent item, excluding the parent item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func ofParentItem(_ parentItem: Any) -> NSDiffableDataSourceSectionSnapshotReference
```

## See Also

### Creating a section snapshot

- [- init](<init().md>) — Creates an empty section snapshot.
- [- snapshotOfParentItem:includingParentItem:](<ofparentitem(__includingparentitem_).md>) — Creates a section snapshot containing the child items of the specified parent item, including the parent item.
- [- appendItems:](<appenditems(__).md>) — Adds the specified items to the section snapshot.
- [- appendItems:intoParentItem:](<appenditems(__intoparentitem_).md>) — Adds the specified items as child items of the specified parent item in the section snapshot.

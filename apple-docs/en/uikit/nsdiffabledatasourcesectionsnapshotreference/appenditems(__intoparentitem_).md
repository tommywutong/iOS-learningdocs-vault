---
title: 'appendItems(_:intoParentItem:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsdiffabledatasourcesectionsnapshotreference/appenditems(_:intoparentitem:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshotreference/appenditems(_:intoparentitem:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesectionsnapshotreference/appenditems%28_%3Aintoparentitem%3A%29.json'
content_hash: 'sha256:82fdc841f82ea875'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSectionSnapshotReference](../nsdiffabledatasourcesectionsnapshotreference.md)

# appendItems(_:intoParentItem:)

<sub>Instance Method</sub>

Adds the specified items as child items of the specified parent item in the section snapshot.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func appendItems(_ items: [Any], intoParentItem parentItem: Any?)
```

## Parameters

- `items` — The identifiers of the items to append to the parent item in the section snapshot.

- `parentItem` — The parent item to append the items to.

## See Also

### Creating a section snapshot

- [- init](<init().md>) — Creates an empty section snapshot.
- [- snapshotOfParentItem:](<ofparentitem(__).md>) — Creates a section snapshot containing the child items of the specified parent item, excluding the parent item.
- [- snapshotOfParentItem:includingParentItem:](<ofparentitem(__includingparentitem_).md>) — Creates a section snapshot containing the child items of the specified parent item, including the parent item.
- [- appendItems:](<appenditems(__).md>) — Adds the specified items to the section snapshot.

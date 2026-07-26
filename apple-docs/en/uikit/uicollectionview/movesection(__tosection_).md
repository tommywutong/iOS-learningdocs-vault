---
title: 'moveSection(_:toSection:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/movesection(_:tosection:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/movesection(_:tosection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/movesection%28_%3Atosection%3A%29.json'
content_hash: 'sha256:1871e0950e136f29'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# moveSection(_:toSection:)

<sub>Instance Method</sub>

Moves a section from one location to another in the collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func moveSection(_ section: Int, toSection newSection: Int)
```

## Parameters

- `section` — The index of the section you want to move.

- `newSection` — The index in the collection view that is the destination of the move for the section. The existing section at that location moves up or down to an adjoining index position to make room for it.

## Discussion

Use this method to reorganize existing sections and their contained items. You might do this when you rearrange sections within your data source object or in response to user interactions with the collection view. The collection view updates the layout as needed to account for the move, animating new views into position as needed.

You can also call this method from a block passed to the [- performBatchUpdates:completion:](<performbatchupdates(__completion_).md>) method when you want to animate multiple separate changes into place at the same time. See the description of that method for more information.

## See Also

### Inserting, moving, and deleting sections

- [- insertSections:](<insertsections(__).md>) — Inserts new sections at the specified indexes.
- [- deleteSections:](<deletesections(__).md>) — Deletes the sections at the specified indexes.

---
title: 'deleteSections(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/deletesections(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/deletesections(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/deletesections%28_%3A%29.json'
content_hash: 'sha256:6be8ce1f9bf00fdf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# deleteSections(_:)

<sub>Instance Method</sub>

Deletes the sections at the specified indexes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func deleteSections(_ sections: IndexSet)
```

## Parameters

- `sections` — The indexes of the sections you want to delete. This parameter must not be `nil`.

## Discussion

Use this method to remove the sections and their items from the collection view. You might do this when you remove the sections from your data source object or in response to user interactions with the collection view. The collection view updates the layout of the remaining sections and items to account for the deletions, animating the remaining items into position as needed.

You can also call this method from a block passed to the [- performBatchUpdates:completion:](<performbatchupdates(__completion_).md>) method when you want to animate multiple separate changes into place at the same time. See the description of that method for more information.

## See Also

### Inserting, moving, and deleting sections

- [- insertSections:](<insertsections(__).md>) — Inserts new sections at the specified indexes.
- [- moveSection:toSection:](<movesection(__tosection_).md>) — Moves a section from one location to another in the collection view.

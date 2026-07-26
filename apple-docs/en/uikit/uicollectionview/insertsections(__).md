---
title: 'insertSections(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/insertsections(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/insertsections(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/insertsections%28_%3A%29.json'
content_hash: 'sha256:28cb27113a4c3274'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# insertSections(_:)

<sub>Instance Method</sub>

Inserts new sections at the specified indexes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func insertSections(_ sections: IndexSet)
```

## Parameters

- `sections` — An index set containing the indexes of the sections you want to insert. This parameter must not be `nil`.

## Discussion

Use this method to insert one or more sections into the collection view. This method adds the sections, and it is up to your data source to report the number of items in each section when asked for the information. The collection view then uses that information to get updated layout attributes for the newly inserted sections and items. If the insertions cause a change in the collection view’s visible content, those changes are animated into place.

You can also call this method from a block passed to the [- performBatchUpdates:completion:](<performbatchupdates(__completion_).md>) method when you want to animate multiple separate changes into place at the same time. See the description of that method for more information.

## See Also

### Inserting, moving, and deleting sections

- [- moveSection:toSection:](<movesection(__tosection_).md>) — Moves a section from one location to another in the collection view.
- [- deleteSections:](<deletesections(__).md>) — Deletes the sections at the specified indexes.

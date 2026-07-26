---
title: 'snapshot(forSection:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdiffabledatasourcereference/snapshot(forsection:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasourcereference/snapshot(forsection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdiffabledatasourcereference/snapshot%28forsection%3A%29.json'
content_hash: 'sha256:115f68761d1d7eb1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDiffableDataSourceReference](../uicollectionviewdiffabledatasourcereference.md)

# snapshot(forSection:)

<sub>Instance Method</sub>

Returns a representation of the current state of the data in the specified section of the collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func snapshot(forSection section: Any) -> NSDiffableDataSourceSectionSnapshotReference
```

## See Also

### Updating section data

- [- applySnapshot:toSection:animatingDifferences:completion:](<applysnapshot(__tosection_animatingdifferences_completion_).md>) — Updates the section UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes and executing a completion handler.
- [- applySnapshot:toSection:animatingDifferences:](<applysnapshot(__tosection_animatingdifferences_).md>) — Updates the section UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes.

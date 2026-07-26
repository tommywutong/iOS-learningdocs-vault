---
title: 'applySnapshot(_:toSection:animatingDifferences:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdiffabledatasourcereference/applysnapshot(_:tosection:animatingdifferences:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasourcereference/applysnapshot(_:tosection:animatingdifferences:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdiffabledatasourcereference/applysnapshot%28_%3Atosection%3Aanimatingdifferences%3A%29.json'
content_hash: 'sha256:aeae21dcb94c621e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDiffableDataSourceReference](../uicollectionviewdiffabledatasourcereference.md)

# applySnapshot(_:toSection:animatingDifferences:)

<sub>Instance Method</sub>

Updates the section UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func applySnapshot(_ snapshot: NSDiffableDataSourceSectionSnapshotReference, toSection sectionIdentifier: Any, animatingDifferences: Bool)
```

## See Also

### Updating section data

- [- snapshotForSection:](<snapshot(forsection_).md>) — Returns a representation of the current state of the data in the specified section of the collection view.
- [- applySnapshot:toSection:animatingDifferences:completion:](<applysnapshot(__tosection_animatingdifferences_completion_).md>) — Updates the section UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes and executing a completion handler.

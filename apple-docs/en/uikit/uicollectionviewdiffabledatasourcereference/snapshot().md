---
title: snapshot()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdiffabledatasourcereference/snapshot()
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasourcereference/snapshot()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdiffabledatasourcereference/snapshot%28%29.json'
content_hash: 'sha256:373f4d866a85a7ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDiffableDataSourceReference](../uicollectionviewdiffabledatasourcereference.md)

# snapshot()

<sub>Instance Method</sub>

Returns a representation of the current state of the data in the collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func snapshot() -> NSDiffableDataSourceSnapshotReference
```

## Return Value

A snapshot containing section and item identifiers in the order that they appear in the UI.

## See Also

### Updating data

- [- applySnapshot:animatingDifferences:](<applysnapshot(__animatingdifferences_).md>) — Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes.
- [- applySnapshot:animatingDifferences:completion:](<applysnapshot(__animatingdifferences_completion_).md>) — Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes and executing a completion handler.
- [- applySnapshotUsingReloadData:](<applysnapshot(usingreloaddata_).md>) — Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes.
- [- applySnapshotUsingReloadData:completion:](<applysnapshot(usingreloaddata_completion_).md>) — Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes, optionally executing a completion handler.

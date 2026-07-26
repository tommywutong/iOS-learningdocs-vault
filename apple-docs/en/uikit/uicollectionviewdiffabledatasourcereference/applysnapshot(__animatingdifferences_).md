---
title: 'applySnapshot(_:animatingDifferences:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdiffabledatasourcereference/applysnapshot(_:animatingdifferences:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasourcereference/applysnapshot(_:animatingdifferences:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdiffabledatasourcereference/applysnapshot%28_%3Aanimatingdifferences%3A%29.json'
content_hash: 'sha256:6eb849e18ef3b86a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDiffableDataSourceReference](../uicollectionviewdiffabledatasourcereference.md)

# applySnapshot(_:animatingDifferences:)

<sub>Instance Method</sub>

Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func applySnapshot(_ snapshot: NSDiffableDataSourceSnapshotReference, animatingDifferences: Bool)
```

## Parameters

- `snapshot` — The snapshot that reflects the new state of the data in the collection view.

- `animatingDifferences` — If [true](../../swift/true.md), the system animates the updates to the collection view. If [false](../../swift/false.md), the system doesn’t animate the updates to the collection view.

## Discussion

The diffable data source computes the difference between the collection view’s current state and the new state in the applied snapshot, which is an O(_n_) operation, where _n_ is the number of items in the snapshot.

You can safely call this method from a background queue, but you must do so consistently in your app. Always call this method exclusively from the main queue or from a background queue.

## See Also

### Updating data

- [- snapshot](<snapshot().md>) — Returns a representation of the current state of the data in the collection view.
- [- applySnapshot:animatingDifferences:completion:](<applysnapshot(__animatingdifferences_completion_).md>) — Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes and executing a completion handler.
- [- applySnapshotUsingReloadData:](<applysnapshot(usingreloaddata_).md>) — Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes.
- [- applySnapshotUsingReloadData:completion:](<applysnapshot(usingreloaddata_completion_).md>) — Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes, optionally executing a completion handler.

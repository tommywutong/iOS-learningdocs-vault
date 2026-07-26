---
title: 'applySnapshot(usingReloadData:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdiffabledatasourcereference/applysnapshot(usingreloaddata:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasourcereference/applysnapshot(usingreloaddata:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdiffabledatasourcereference/applysnapshot%28usingreloaddata%3A%29.json'
content_hash: 'sha256:b0ff49260bd01562'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDiffableDataSourceReference](../uicollectionviewdiffabledatasourcereference.md)

# applySnapshot(usingReloadData:)

<sub>Instance Method</sub>

Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func applySnapshot(usingReloadData snapshot: NSDiffableDataSourceSnapshotReference)
```

## Parameters

- `snapshot` — The snapshot that reflects the new state of the data in the collection view.

## Discussion

The system interrupts any ongoing item animations and immediately reloads the collection view’s content.

You can safely call this method from a background queue, but you must do so consistently in your app. Always call this method exclusively from the main queue or from a background queue.

## See Also

### Updating data

- [- snapshot](<snapshot().md>) — Returns a representation of the current state of the data in the collection view.
- [- applySnapshot:animatingDifferences:](<applysnapshot(__animatingdifferences_).md>) — Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes.
- [- applySnapshot:animatingDifferences:completion:](<applysnapshot(__animatingdifferences_completion_).md>) — Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes and executing a completion handler.
- [- applySnapshotUsingReloadData:completion:](<applysnapshot(usingreloaddata_completion_).md>) — Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes, optionally executing a completion handler.

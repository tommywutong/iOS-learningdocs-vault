---
title: 'applySnapshot(usingReloadData:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdiffabledatasourcereference/applysnapshot(usingreloaddata:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdiffabledatasourcereference/applysnapshot(usingreloaddata:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdiffabledatasourcereference/applysnapshot%28usingreloaddata%3A%29.json'
content_hash: 'sha256:9a51b1473f173c2b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDiffableDataSourceReference](../uitableviewdiffabledatasourcereference.md)

# applySnapshot(usingReloadData:)

<sub>Instance Method</sub>

Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func applySnapshot(usingReloadData snapshot: NSDiffableDataSourceSnapshotReference)
```

## Parameters

- `snapshot` — The snapshot that reflects the new state of the data in the table view.

## Discussion

The system interrupts any ongoing item animations and immediately reloads the table view’s content.

You can safely call this method from a background queue, but you must do so consistently in your app. Always call this method exclusively from the main queue or from a background queue.

## See Also

### Updating data

- [- snapshot](<snapshot().md>) — Returns a representation of the current state of the data in the table view.
- [- applySnapshot:animatingDifferences:](<applysnapshot(__animatingdifferences_).md>) — Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes.
- [- applySnapshot:animatingDifferences:completion:](<applysnapshot(__animatingdifferences_completion_).md>) — Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes and executing a completion handler.
- [- applySnapshotUsingReloadData:completion:](<applysnapshot(usingreloaddata_completion_).md>) — Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes, optionally executing a completion handler.
- [defaultRowAnimation](defaultrowanimation.md) — The default type of animation to use when inserting or deleting rows.

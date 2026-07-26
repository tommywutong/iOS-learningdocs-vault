---
title: 'apply(_:animatingDifferences:completion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/apply(_:animatingdifferences:completion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/apply(_:animatingdifferences:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/apply%28_%3Aanimatingdifferences%3Acompletion%3A%29.json'
content_hash: 'sha256:4a4b7b7070d5658d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDiffableDataSource](../uicollectionviewdiffabledatasource-9tqpa.md)

# apply(_:animatingDifferences:completion:)

<sub>Instance Method</sub>

Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes and executing a completion handler.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func apply(_ snapshot: NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>, animatingDifferences: Bool = true, completion: (() -> Void)? = nil)
```

## Parameters

- `snapshot` — The snapshot that reflects the new state of the data in the collection view.

- `animatingDifferences` — If [true](../../swift/true.md), the system animates the updates to the collection view. If [false](../../swift/false.md), the system doesn’t animate the updates to the collection view.

- `completion` — A closure to execute when the animations are complete. This closure has no return value and takes no parameters. The system calls this closure from the main queue.

## Discussion

The diffable data source computes the difference between the collection view’s current state and the new state in the applied snapshot, which is an O(_n_) operation, where _n_ is the number of items in the snapshot.

You can safely call this method from a background queue, but you must do so consistently in your app. Always call this method exclusively from the main queue or from a background queue.

## See Also

### Updating data

- [snapshot()](<snapshot().md>) — Returns a representation of the current state of the data in the collection view.
- [apply(_:animatingDifferences:)](<apply(__animatingdifferences_).md>) — Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes.
- [applySnapshotUsingReloadData(_:)](<applysnapshotusingreloaddata(__).md>) — Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes.
- [applySnapshotUsingReloadData(_:completion:)](<applysnapshotusingreloaddata(__completion_).md>) — Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes, optionally executing a completion handler.

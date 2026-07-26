---
title: 'applySnapshotUsingReloadData(_:completion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdiffabledatasource-2euir/applysnapshotusingreloaddata(_:completion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdiffabledatasource-2euir/applysnapshotusingreloaddata(_:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdiffabledatasource-2euir/applysnapshotusingreloaddata%28_%3Acompletion%3A%29.json'
content_hash: 'sha256:2379388fade0cd3b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDiffableDataSource](../uitableviewdiffabledatasource-2euir.md)

# applySnapshotUsingReloadData(_:completion:)

<sub>Instance Method</sub>

Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes, optionally executing a completion handler.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func applySnapshotUsingReloadData(_ snapshot: NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>, completion: (() -> Void)? = nil)
```

## Parameters

- `snapshot` — The snapshot that reflects the new state of the data in the table view.

- `completion` — A closure to execute when the reload completes. This closure has no return value and takes no parameters. The system calls this closure from the main queue.

## Discussion

The system interrupts any ongoing item animations and immediately reloads the table view’s content.

You can safely call this method from a background queue, but you must do so consistently in your app. Always call this method exclusively from the main queue or from a background queue.

## See Also

### Updating data

- [snapshot()](<snapshot().md>) — Returns a representation of the current state of the data in the table view.
- [apply(_:animatingDifferences:)](<apply(__animatingdifferences_).md>) — Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes.
- [apply(_:animatingDifferences:completion:)](<apply(__animatingdifferences_completion_).md>) — Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes and executing a completion handler.
- [applySnapshotUsingReloadData(_:)](<applysnapshotusingreloaddata(__).md>) — Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes.
- [defaultRowAnimation](defaultrowanimation.md) — The default type of animation to use when inserting or deleting rows.

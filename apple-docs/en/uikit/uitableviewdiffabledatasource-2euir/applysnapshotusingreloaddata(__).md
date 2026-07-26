---
title: 'applySnapshotUsingReloadData(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdiffabledatasource-2euir/applysnapshotusingreloaddata(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdiffabledatasource-2euir/applysnapshotusingreloaddata(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdiffabledatasource-2euir/applysnapshotusingreloaddata%28_%3A%29.json'
content_hash: 'sha256:61e9f7e4ab8035cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDiffableDataSource](../uitableviewdiffabledatasource-2euir.md)

# applySnapshotUsingReloadData(_:)

<sub>Instance Method</sub>

Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func applySnapshotUsingReloadData(_ snapshot: NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>) async
```

## Parameters

- `snapshot` — The snapshot that reflects the new state of the data in the table view.

## Discussion

The system interrupts any ongoing item animations and immediately reloads the table view’s content.

You can safely call this method from a background queue, but you must do so consistently in your app. Always call this method exclusively from the main queue or from a background queue.

## See Also

### Updating data

- [snapshot()](<snapshot().md>) — Returns a representation of the current state of the data in the table view.
- [apply(_:animatingDifferences:)](<apply(__animatingdifferences_).md>) — Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes.
- [apply(_:animatingDifferences:completion:)](<apply(__animatingdifferences_completion_).md>) — Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes and executing a completion handler.
- [applySnapshotUsingReloadData(_:completion:)](<applysnapshotusingreloaddata(__completion_).md>) — Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes, optionally executing a completion handler.
- [defaultRowAnimation](defaultrowanimation.md) — The default type of animation to use when inserting or deleting rows.

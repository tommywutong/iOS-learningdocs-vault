---
title: 'apply(_:animatingDifferences:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdiffabledatasource-2euir/apply(_:animatingdifferences:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdiffabledatasource-2euir/apply(_:animatingdifferences:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdiffabledatasource-2euir/apply%28_%3Aanimatingdifferences%3A%29.json'
content_hash: 'sha256:41b4f9ed04548167'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDiffableDataSource](../uitableviewdiffabledatasource-2euir.md)

# apply(_:animatingDifferences:)

<sub>Instance Method</sub>

Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func apply(_ snapshot: NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>, animatingDifferences: Bool = true) async
```

## See Also

### Updating data

- [snapshot()](<snapshot().md>) — Returns a representation of the current state of the data in the table view.
- [apply(_:animatingDifferences:completion:)](<apply(__animatingdifferences_completion_).md>) — Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes and executing a completion handler.
- [applySnapshotUsingReloadData(_:)](<applysnapshotusingreloaddata(__).md>) — Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes.
- [applySnapshotUsingReloadData(_:completion:)](<applysnapshotusingreloaddata(__completion_).md>) — Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes, optionally executing a completion handler.
- [defaultRowAnimation](defaultrowanimation.md) — The default type of animation to use when inserting or deleting rows.

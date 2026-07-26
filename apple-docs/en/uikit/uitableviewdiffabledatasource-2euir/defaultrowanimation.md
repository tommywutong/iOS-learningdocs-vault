---
title: defaultRowAnimation
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewdiffabledatasource-2euir/defaultrowanimation
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdiffabledatasource-2euir/defaultrowanimation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdiffabledatasource-2euir/defaultrowanimation.json'
content_hash: 'sha256:a19006d42cbc305c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDiffableDataSource](../uitableviewdiffabledatasource-2euir.md)

# defaultRowAnimation

<sub>Instance Property</sub>

The default type of animation to use when inserting or deleting rows.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency var defaultRowAnimation: UITableView.RowAnimation { get set }
```

## Discussion

The default value of this property is [UITableViewRowAnimationAutomatic](../uitableview/rowanimation/automatic.md).

If you set the value of this property, the new value becomes the default row animation for the next update that uses [apply(_:animatingDifferences:completion:)](<apply(__animatingdifferences_completion_).md>).

## See Also

### Updating data

- [snapshot()](<snapshot().md>) — Returns a representation of the current state of the data in the table view.
- [apply(_:animatingDifferences:)](<apply(__animatingdifferences_).md>) — Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes.
- [apply(_:animatingDifferences:completion:)](<apply(__animatingdifferences_completion_).md>) — Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes and executing a completion handler.
- [applySnapshotUsingReloadData(_:)](<applysnapshotusingreloaddata(__).md>) — Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes.
- [applySnapshotUsingReloadData(_:completion:)](<applysnapshotusingreloaddata(__completion_).md>) — Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes, optionally executing a completion handler.

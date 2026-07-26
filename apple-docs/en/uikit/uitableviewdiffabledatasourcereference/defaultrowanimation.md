---
title: defaultRowAnimation
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewdiffabledatasourcereference/defaultrowanimation
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdiffabledatasourcereference/defaultrowanimation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdiffabledatasourcereference/defaultrowanimation.json'
content_hash: 'sha256:7afaae02efa8c4fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDiffableDataSourceReference](../uitableviewdiffabledatasourcereference.md)

# defaultRowAnimation

<sub>Instance Property</sub>

The default type of animation to use when inserting or deleting rows.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var defaultRowAnimation: UITableView.RowAnimation { get set }
```

## Discussion

The default value of this property is [UITableViewRowAnimationAutomatic](../uitableview/rowanimation/automatic.md).

If you set the value of this property, the new value becomes the default row animation for the next update that uses [- applySnapshot:animatingDifferences:](<applysnapshot(__animatingdifferences_).md>) or [- applySnapshot:animatingDifferences:completion:](<applysnapshot(__animatingdifferences_completion_).md>).

## See Also

### Updating data

- [- snapshot](<snapshot().md>) — Returns a representation of the current state of the data in the table view.
- [- applySnapshot:animatingDifferences:](<applysnapshot(__animatingdifferences_).md>) — Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes.
- [- applySnapshot:animatingDifferences:completion:](<applysnapshot(__animatingdifferences_completion_).md>) — Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes and executing a completion handler.
- [- applySnapshotUsingReloadData:](<applysnapshot(usingreloaddata_).md>) — Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes.
- [- applySnapshotUsingReloadData:completion:](<applysnapshot(usingreloaddata_completion_).md>) — Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes, optionally executing a completion handler.

---
title: 'tableView(_:targetIndexPathForMoveFromRowAt:toProposedIndexPath:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:targetindexpathformovefromrowat:toproposedindexpath:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:targetindexpathformovefromrowat:toproposedindexpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Atargetindexpathformovefromrowat%3Atoproposedindexpath%3A%29.json'
content_hash: 'sha256:cc83c561b996aff4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:targetIndexPathForMoveFromRowAt:toProposedIndexPath:)

<sub>Instance Method</sub>

Asks the delegate to return a new index path to retarget a proposed move of a row.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, targetIndexPathForMoveFromRowAt sourceIndexPath: IndexPath, toProposedIndexPath proposedDestinationIndexPath: IndexPath) -> IndexPath
```

## Parameters

- `tableView` — The table view that is requesting this information.

- `sourceIndexPath` — An index path identifying the original location of a row (in its section) that is being dragged.

- `proposedDestinationIndexPath` — An index path identifying the currently proposed destination of the row being dragged.

## Return Value

An index path locating the desired row destination for the move operation. Return `proposedDestinationIndexPath` if that location is suitable.

## Discussion

This method allows customization of the target row for a particular row as it is being moved up and down a table view.  As the dragged row hovers over another row, the destination row slides downward to visually make room for the relocation; this is the location identified by `proposedDestinationIndexPath`.

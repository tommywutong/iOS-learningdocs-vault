---
title: 'cellForRow(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableview/cellforrow(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/cellforrow(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/cellforrow%28at%3A%29.json'
content_hash: 'sha256:3a045222ec661379'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# cellForRow(at:)

<sub>Instance Method</sub>

Returns the table cell at the index path you specify.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func cellForRow(at indexPath: IndexPath) -> UITableViewCell?
```

## Parameters

- `indexPath` — The index path locating the row in the table view.

## Return Value

The cell object at the corresponding index path. In versions of iOS earlier than iOS 15, this method returns `nil` if the cell isn’t visible or if `indexPath` is out of range. In iOS 15 and later, this method returns a non-`nil` cell if the table view retains a prepared cell at the specified index path, even if the cell isn’t currently visible.

## Discussion

In iOS 15 and later, the table view retains a prepared cell in the following situations:

- Cells that the table view prefetches and retains in its cache of prepared cells, but that aren’t visible because the table view hasn’t displayed them yet.
- Cells that the table view finishes displaying and continues to retain in its cache of prepared cells because they remain near the visible region and might scroll back into view.
- The cell that contains the first responder.
- The cell that has focus.

## See Also

### Getting cells and section-based views

- [- headerViewForSection:](<headerview(forsection_).md>) — Returns the header view for the specified section.
- [- footerViewForSection:](<footerview(forsection_).md>) — Returns the footer view for the specified section.
- [- indexPathForCell:](<indexpath(for_).md>) — Returns an index path that represents the row and section of a specified table-view cell.
- [- indexPathForRowAtPoint:](<indexpathforrow(at_).md>) — Returns an index path that identifies the row and section at the specified point.
- [- indexPathsForRowsInRect:](<indexpathsforrows(in_).md>) — Returns an array of index paths, each representing a row that the specified rectangle encloses.
- [visibleCells](visiblecells.md) — The table cells that are visible in the table view.
- [indexPathsForVisibleRows](indexpathsforvisiblerows.md) — An array of index paths, each identifying a visible row in the table view.

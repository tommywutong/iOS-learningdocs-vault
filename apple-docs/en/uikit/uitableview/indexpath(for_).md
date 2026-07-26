---
title: 'indexPath(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableview/indexpath(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/indexpath(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/indexpath%28for%3A%29.json'
content_hash: 'sha256:57db859df44ce999'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# indexPath(for:)

<sub>Instance Method</sub>

Returns an index path that represents the row and section of a specified table-view cell.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func indexPath(for cell: UITableViewCell) -> IndexPath?
```

## Parameters

- `cell` — A cell object of the table view.

## Return Value

An index path representing the row and section of the cell, or `nil` if the index path is invalid.

## See Also

### Getting cells and section-based views

- [- cellForRowAtIndexPath:](<cellforrow(at_).md>) — Returns the table cell at the index path you specify.
- [- headerViewForSection:](<headerview(forsection_).md>) — Returns the header view for the specified section.
- [- footerViewForSection:](<footerview(forsection_).md>) — Returns the footer view for the specified section.
- [- indexPathForRowAtPoint:](<indexpathforrow(at_).md>) — Returns an index path that identifies the row and section at the specified point.
- [- indexPathsForRowsInRect:](<indexpathsforrows(in_).md>) — Returns an array of index paths, each representing a row that the specified rectangle encloses.
- [visibleCells](visiblecells.md) — The table cells that are visible in the table view.
- [indexPathsForVisibleRows](indexpathsforvisiblerows.md) — An array of index paths, each identifying a visible row in the table view.

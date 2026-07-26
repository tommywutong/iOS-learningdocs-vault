---
title: 'headerView(forSection:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableview/headerview(forsection:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/headerview(forsection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/headerview%28forsection%3A%29.json'
content_hash: 'sha256:0b7311eb4b17c837'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# headerView(forSection:)

<sub>Instance Method</sub>

Returns the header view for the specified section.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func headerView(forSection section: Int) -> UITableViewHeaderFooterView?
```

## Parameters

- `section` — An index number that identifies a section of the table. Table views in a plain style have a section index of zero.

## Return Value

The header view associated with the section, or `nil` if the section does not have a header view.

## See Also

### Getting cells and section-based views

- [- cellForRowAtIndexPath:](<cellforrow(at_).md>) — Returns the table cell at the index path you specify.
- [- footerViewForSection:](<footerview(forsection_).md>) — Returns the footer view for the specified section.
- [- indexPathForCell:](<indexpath(for_).md>) — Returns an index path that represents the row and section of a specified table-view cell.
- [- indexPathForRowAtPoint:](<indexpathforrow(at_).md>) — Returns an index path that identifies the row and section at the specified point.
- [- indexPathsForRowsInRect:](<indexpathsforrows(in_).md>) — Returns an array of index paths, each representing a row that the specified rectangle encloses.
- [visibleCells](visiblecells.md) — The table cells that are visible in the table view.
- [indexPathsForVisibleRows](indexpathsforvisiblerows.md) — An array of index paths, each identifying a visible row in the table view.

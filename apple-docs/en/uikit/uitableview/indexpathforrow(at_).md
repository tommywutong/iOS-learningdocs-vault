---
title: 'indexPathForRow(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableview/indexpathforrow(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/indexpathforrow(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/indexpathforrow%28at%3A%29.json'
content_hash: 'sha256:500c1142a52962f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# indexPathForRow(at:)

<sub>Instance Method</sub>

Returns an index path that identifies the row and section at the specified point.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func indexPathForRow(at point: CGPoint) -> IndexPath?
```

## Parameters

- `point` — A point in the local coordinate system of the table view (the table view’s bounds).

## Return Value

An index path representing the row and section associated with `point`, or `nil` if the point is out of the bounds of any row.

## See Also

### Getting cells and section-based views

- [- cellForRowAtIndexPath:](<cellforrow(at_).md>) — Returns the table cell at the index path you specify.
- [- headerViewForSection:](<headerview(forsection_).md>) — Returns the header view for the specified section.
- [- footerViewForSection:](<footerview(forsection_).md>) — Returns the footer view for the specified section.
- [- indexPathForCell:](<indexpath(for_).md>) — Returns an index path that represents the row and section of a specified table-view cell.
- [- indexPathsForRowsInRect:](<indexpathsforrows(in_).md>) — Returns an array of index paths, each representing a row that the specified rectangle encloses.
- [visibleCells](visiblecells.md) — The table cells that are visible in the table view.
- [indexPathsForVisibleRows](indexpathsforvisiblerows.md) — An array of index paths, each identifying a visible row in the table view.

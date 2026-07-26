---
title: 'indexPathsForRows(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableview/indexpathsforrows(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/indexpathsforrows(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/indexpathsforrows%28in%3A%29.json'
content_hash: 'sha256:9bc836507e30a141'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# indexPathsForRows(in:)

<sub>Instance Method</sub>

Returns an array of index paths, each representing a row that the specified rectangle encloses.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func indexPathsForRows(in rect: CGRect) -> [IndexPath]?
```

## Parameters

- `rect` — A rectangle defining an area of the table view in local coordinates.

## Return Value

An array of [NSIndexPath](../../foundation/nsindexpath.md) objects each representing a row and section index identifying a row within `rect`. Returns an empty array if there aren’t any rows to return.

## See Also

### Getting cells and section-based views

- [- cellForRowAtIndexPath:](<cellforrow(at_).md>) — Returns the table cell at the index path you specify.
- [- headerViewForSection:](<headerview(forsection_).md>) — Returns the header view for the specified section.
- [- footerViewForSection:](<footerview(forsection_).md>) — Returns the footer view for the specified section.
- [- indexPathForCell:](<indexpath(for_).md>) — Returns an index path that represents the row and section of a specified table-view cell.
- [- indexPathForRowAtPoint:](<indexpathforrow(at_).md>) — Returns an index path that identifies the row and section at the specified point.
- [visibleCells](visiblecells.md) — The table cells that are visible in the table view.
- [indexPathsForVisibleRows](indexpathsforvisiblerows.md) — An array of index paths, each identifying a visible row in the table view.

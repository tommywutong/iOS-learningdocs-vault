---
title: visibleCells
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/visiblecells
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/visiblecells'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/visiblecells.json'
content_hash: 'sha256:1976ae8db916e2a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# visibleCells

<sub>Instance Property</sub>

The table cells that are visible in the table view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var visibleCells: [UITableViewCell] { get }
```

## Discussion

The value of this property is an array containing [UITableViewCell](../uitableviewcell.md) objects, each representing a visible cell in the table view.

## See Also

### Getting cells and section-based views

- [- cellForRowAtIndexPath:](<cellforrow(at_).md>) — Returns the table cell at the index path you specify.
- [- headerViewForSection:](<headerview(forsection_).md>) — Returns the header view for the specified section.
- [- footerViewForSection:](<footerview(forsection_).md>) — Returns the footer view for the specified section.
- [- indexPathForCell:](<indexpath(for_).md>) — Returns an index path that represents the row and section of a specified table-view cell.
- [- indexPathForRowAtPoint:](<indexpathforrow(at_).md>) — Returns an index path that identifies the row and section at the specified point.
- [- indexPathsForRowsInRect:](<indexpathsforrows(in_).md>) — Returns an array of index paths, each representing a row that the specified rectangle encloses.
- [indexPathsForVisibleRows](indexpathsforvisiblerows.md) — An array of index paths, each identifying a visible row in the table view.

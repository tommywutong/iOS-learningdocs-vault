---
title: rowHeight
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/rowheight
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/rowheight'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/rowheight.json'
content_hash: 'sha256:3b33b3bb54b70635'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# rowHeight

<sub>Instance Property</sub>

The default height in points of each row in the table view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var rowHeight: CGFloat { get set }
```

## Discussion

Use this property to specify a custom height for the cells in your table view. The default value of this property is [UITableViewAutomaticDimension](automaticdimension.md), which causes the table view to choose an appropriate height based on your cell’s content.

If you create a self-sizing cell in Interface Builder, the table view changes the default row height to the value you set in Interface Builder. To get the expected self-sizing behavior for a cell that you create in Interface Builder, you must explicitly set [rowHeight](rowheight.md) to [UITableViewAutomaticDimension](automaticdimension.md) in your code.

The table view ignores the value of this property if its delegate implements the [- tableView:heightForRowAtIndexPath:](<../uitableviewdelegate/tableview(__heightforrowat_).md>) method. Prefer the use of this property over the delegate method when specifying row heights. When you implement the delegate method, the table view must call that method for every row of the table, including those that are offscreen. For tables with large numbers of rows (1000 or more), calling that method many times can negatively impact performance.

## See Also

### Configuring cell height and layout

- [estimatedRowHeight](estimatedrowheight.md) — The estimated height of rows in the table view.
- [fillerRowHeight](fillerrowheight.md) — The height for empty rows that fill the table view.
- [cellLayoutMarginsFollowReadableWidth](celllayoutmarginsfollowreadablewidth.md) — A Boolean value that indicates whether the cell margins derive from the width of the readable content guide.
- [insetsContentViewsToSafeArea](insetscontentviewstosafearea.md) — A Boolean value that indicates whether the table view adjusts the content views of its cells, headers, and footers to fit within the safe area.

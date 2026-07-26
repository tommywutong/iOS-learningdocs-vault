---
title: 'tableView(_:heightForRowAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:heightforrowat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:heightforrowat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Aheightforrowat%3A%29.json'
content_hash: 'sha256:e1e42e61ee199742'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:heightForRowAt:)

<sub>Instance Method</sub>

Asks the delegate for the height to use for a row in a specified location.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat
```

## Parameters

- `tableView` — The table view requesting this information.

- `indexPath` — An index path that locates a row in `tableView`.

## Return Value

A nonnegative floating-point value that specifies the height (in points) that `row` should be.

## Discussion

Override this method when the rows of your table are not all the same height. If your rows are the same height, do not override this method; assign a value to the [rowHeight](../uitableview/rowheight.md) property of [UITableView](../uitableview.md) instead. The value returned by this method takes precedence over the value in the [rowHeight](../uitableview/rowheight.md) property.

Before it appears onscreen, the table view calls this method for the items in the visible portion of the table. As the user scrolls, the table view calls the method for items only when they move onscreen. It calls the method each time the item appears onscreen, regardless of whether it appeared onscreen previously.

## See Also

### Related Documentation

- [- tableView:estimatedHeightForRowAtIndexPath:](<tableview(__estimatedheightforrowat_).md>) — Asks the delegate for the estimated height of a row in a specified location.

### Providing header, footer, and row heights

- [- tableView:heightForHeaderInSection:](<tableview(__heightforheaderinsection_).md>) — Asks the delegate for the height to use for the header of a particular section.
- [- tableView:heightForFooterInSection:](<tableview(__heightforfooterinsection_).md>) — Asks the delegate for the height to use for the footer of a particular section.
- [UITableViewAutomaticDimension](../uitableview/automaticdimension.md) — A constant representing the default value for a given dimension.

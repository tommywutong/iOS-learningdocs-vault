---
title: 'tableView(_:estimatedHeightForRowAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:estimatedheightforrowat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:estimatedheightforrowat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Aestimatedheightforrowat%3A%29.json'
content_hash: 'sha256:1713e12f71a9b59b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:estimatedHeightForRowAt:)

<sub>Instance Method</sub>

Asks the delegate for the estimated height of a row in a specified location.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, estimatedHeightForRowAt indexPath: IndexPath) -> CGFloat
```

## Parameters

- `tableView` — The table view requesting this information.

- `indexPath` — An index path that locates a row in `tableView`.

## Return Value

A nonnegative floating-point value that estimates the height (in points) that `row` should be. Return [UITableViewAutomaticDimension](../uitableview/automaticdimension.md) if you have no estimate.

## Discussion

Providing an estimate the height of rows can improve the user experience when loading the table view. If the table contains variable height rows, it might be expensive to calculate all their heights and so lead to a longer load time. Using estimation allows you to defer some of the cost of geometry calculation from load time to scrolling time.

## See Also

### Related Documentation

- [- tableView:heightForRowAtIndexPath:](<tableview(__heightforrowat_).md>) — Asks the delegate for the height to use for a row in a specified location.

### Estimating heights for the table’s content

- [- tableView:estimatedHeightForHeaderInSection:](<tableview(__estimatedheightforheaderinsection_).md>) — Asks the delegate for the estimated height of the header of a particular section.
- [- tableView:estimatedHeightForFooterInSection:](<tableview(__estimatedheightforfooterinsection_).md>) — Asks the delegate for the estimated height of the footer of a particular section.

---
title: 'tableView(_:estimatedHeightForFooterInSection:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:estimatedheightforfooterinsection:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:estimatedheightforfooterinsection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Aestimatedheightforfooterinsection%3A%29.json'
content_hash: 'sha256:8da28a1914355d78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:estimatedHeightForFooterInSection:)

<sub>Instance Method</sub>

Asks the delegate for the estimated height of the footer of a particular section.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, estimatedHeightForFooterInSection section: Int) -> CGFloat
```

## Parameters

- `tableView` — The table view requesting this information.

- `section` — An index number identifying a section of `tableView` .

## Return Value

A nonnegative floating-point value that estimates the height (in points) of the footer for `section`.

## Discussion

Providing an estimate the height of section footers can improve the user experience when loading the table view. If the table contains variable height section footers, it might be expensive to calculate all their heights and so lead to a longer load time. Using estimation allows you to defer some of the cost of geometry calculation from load time to scrolling time.

## See Also

### Related Documentation

- [- tableView:heightForFooterInSection:](<tableview(__heightforfooterinsection_).md>) — Asks the delegate for the height to use for the footer of a particular section.

### Estimating heights for the table’s content

- [- tableView:estimatedHeightForRowAtIndexPath:](<tableview(__estimatedheightforrowat_).md>) — Asks the delegate for the estimated height of a row in a specified location.
- [- tableView:estimatedHeightForHeaderInSection:](<tableview(__estimatedheightforheaderinsection_).md>) — Asks the delegate for the estimated height of the header of a particular section.

---
title: 'tableView(_:estimatedHeightForHeaderInSection:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:estimatedheightforheaderinsection:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:estimatedheightforheaderinsection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Aestimatedheightforheaderinsection%3A%29.json'
content_hash: 'sha256:860876907b3a3e2a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:estimatedHeightForHeaderInSection:)

<sub>Instance Method</sub>

Asks the delegate for the estimated height of the header of a particular section.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, estimatedHeightForHeaderInSection section: Int) -> CGFloat
```

## Parameters

- `tableView` — The table view requesting this information.

- `section` — An index number identifying a section of `tableView` .

## Return Value

A nonnegative floating-point value that specifies the height (in points) of the header for `section`.

## Discussion

Providing an estimate the height of section headers can improve the user experience when loading the table view. If the table contains variable height section headers, it might be expensive to calculate all their heights and so lead to a longer load time. Using estimation allows you to defer some of the cost of geometry calculation from load time to scrolling time.

## See Also

### Related Documentation

- [- tableView:heightForHeaderInSection:](<tableview(__heightforheaderinsection_).md>) — Asks the delegate for the height to use for the header of a particular section.

### Estimating heights for the table’s content

- [- tableView:estimatedHeightForRowAtIndexPath:](<tableview(__estimatedheightforrowat_).md>) — Asks the delegate for the estimated height of a row in a specified location.
- [- tableView:estimatedHeightForFooterInSection:](<tableview(__estimatedheightforfooterinsection_).md>) — Asks the delegate for the estimated height of the footer of a particular section.

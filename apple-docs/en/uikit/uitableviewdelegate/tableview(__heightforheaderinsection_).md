---
title: 'tableView(_:heightForHeaderInSection:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdelegate/tableview(_:heightforheaderinsection:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:heightforheaderinsection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate/tableview%28_%3Aheightforheaderinsection%3A%29.json'
content_hash: 'sha256:b4d36a80c43527fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDelegate](../uitableviewdelegate.md)

# tableView(_:heightForHeaderInSection:)

<sub>Instance Method</sub>

Asks the delegate for the height to use for the header of a particular section.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, heightForHeaderInSection section: Int) -> CGFloat
```

## Parameters

- `tableView` — The table view requesting this information.

- `section` — An index number identifying a section of `tableView` .

## Return Value

A nonnegative floating-point value that specifies the height (in points) of the header for `section`.

## Discussion

Use this method to specify the height of custom header views returned by your [- tableView:viewForHeaderInSection:](<tableview(__viewforheaderinsection_).md>) method.

## See Also

### Related Documentation

- [- tableView:estimatedHeightForHeaderInSection:](<tableview(__estimatedheightforheaderinsection_).md>) — Asks the delegate for the estimated height of the header of a particular section.
- [- tableView:viewForHeaderInSection:](<tableview(__viewforheaderinsection_).md>) — Asks the delegate for a view to display in the header of the specified section of the table view.

### Providing header, footer, and row heights

- [- tableView:heightForRowAtIndexPath:](<tableview(__heightforrowat_).md>) — Asks the delegate for the height to use for a row in a specified location.
- [- tableView:heightForFooterInSection:](<tableview(__heightforfooterinsection_).md>) — Asks the delegate for the height to use for the footer of a particular section.
- [UITableViewAutomaticDimension](../uitableview/automaticdimension.md) — A constant representing the default value for a given dimension.

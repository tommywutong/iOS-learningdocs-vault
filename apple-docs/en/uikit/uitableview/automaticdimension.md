---
title: automaticDimension
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/automaticdimension
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/automaticdimension'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/automaticdimension.json'
content_hash: 'sha256:ac215ca888765c5c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# automaticDimension

<sub>Type Property</sub>

A constant representing the default value for a given dimension.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class let automaticDimension: CGFloat
```

## Discussion

Return this value from your table view’s delegate methods when you want the table view to choose a default value for the given dimension. For example, if you return this constant from [- tableView:heightForHeaderInSection:](<../uitableviewdelegate/tableview(__heightforheaderinsection_).md>) or [- tableView:heightForFooterInSection:](<../uitableviewdelegate/tableview(__heightforfooterinsection_).md>), the table view uses a height that fits the value returned from [- tableView:titleForHeaderInSection:](<../uitableviewdatasource/tableview(__titleforheaderinsection_).md>) or [- tableView:titleForFooterInSection:](<../uitableviewdatasource/tableview(__titleforfooterinsection_).md>), if the title is not `nil`.

## See Also

### Providing header, footer, and row heights

- [- tableView:heightForRowAtIndexPath:](<../uitableviewdelegate/tableview(__heightforrowat_).md>) — Asks the delegate for the height to use for a row in a specified location.
- [- tableView:heightForHeaderInSection:](<../uitableviewdelegate/tableview(__heightforheaderinsection_).md>) — Asks the delegate for the height to use for the header of a particular section.
- [- tableView:heightForFooterInSection:](<../uitableviewdelegate/tableview(__heightforfooterinsection_).md>) — Asks the delegate for the height to use for the footer of a particular section.

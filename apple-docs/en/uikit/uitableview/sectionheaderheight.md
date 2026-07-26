---
title: sectionHeaderHeight
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/sectionheaderheight
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/sectionheaderheight'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/sectionheaderheight.json'
content_hash: 'sha256:0064a8b88b0bfada'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# sectionHeaderHeight

<sub>Instance Property</sub>

The height of section headers in the table view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var sectionHeaderHeight: CGFloat { get set }
```

## Discussion

The default value is [UITableViewAutomaticDimension](automaticdimension.md). If the delegate doesn’t implement [- tableView:heightForHeaderInSection:](<../uitableviewdelegate/tableview(__heightforheaderinsection_).md>), the table view calculates the height automatically. To override automatic height calculation, set this property to a positive value.

## See Also

### Related Documentation

- [tableHeaderView](tableheaderview.md) — The view that displays above the table’s content.

### Configuring header and footer appearance

- [sectionFooterHeight](sectionfooterheight.md) — The height of section footers in the table view.
- [estimatedSectionHeaderHeight](estimatedsectionheaderheight.md) — The estimated height of section headers in the table view.
- [estimatedSectionFooterHeight](estimatedsectionfooterheight.md) — The estimated height of section footers in the table view.
- [sectionHeaderTopPadding](sectionheadertoppadding.md) — The amount of padding above each section header.

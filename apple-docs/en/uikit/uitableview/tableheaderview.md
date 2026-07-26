---
title: tableHeaderView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/tableheaderview
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/tableheaderview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/tableheaderview.json'
content_hash: 'sha256:c2d8cdaaf15e1c83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# tableHeaderView

<sub>Instance Property</sub>

The view that displays above the table’s content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var tableHeaderView: UIView? { get set }
```

## Discussion

Use this property to specify a header view for your entire table. The header view is the first item to appear in the table’s view’s scrolling content, and it’s separate from the header views you add to individual sections. The default value of this property is `nil`.

When assigning a view to this property, set the height of that view to a nonzero value. The table view respects only the height of your view’s frame rectangle; it adjusts the width of your header view automatically to match the table view’s width.

## See Also

### Related Documentation

- [sectionHeaderHeight](sectionheaderheight.md) — The height of section headers in the table view.

### Configuring the table’s appearance

- [style](style-swift.property.md) — The style of the table view.
- [Style](style-swift.enum.md) — Constants for the table view styles.
- [tableFooterView](tablefooterview.md) — The view that displays below the table’s content.
- [backgroundView](backgroundview.md) — The background view of the table view.

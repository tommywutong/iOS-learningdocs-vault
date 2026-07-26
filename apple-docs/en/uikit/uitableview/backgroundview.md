---
title: backgroundView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/backgroundview
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/backgroundview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/backgroundview.json'
content_hash: 'sha256:cca0a5ef2e0aa046'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# backgroundView

<sub>Instance Property</sub>

The background view of the table view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var backgroundView: UIView? { get set }
```

## Discussion

Assign a background view to change the color behind your table’s sections and rows. The default value of this property is `nil`.

When you assign a view to this property, the table view automatically resizes that view to match its own bounds. Your background view appears behind all cells, header views, and footer views and doesn’t scroll with the rest of the table’s content.

## See Also

### Configuring the table’s appearance

- [style](style-swift.property.md) — The style of the table view.
- [Style](style-swift.enum.md) — Constants for the table view styles.
- [tableHeaderView](tableheaderview.md) — The view that displays above the table’s content.
- [tableFooterView](tablefooterview.md) — The view that displays below the table’s content.

---
title: 'tableView(_:numberOfRowsInSection:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdatasource/tableview(_:numberofrowsinsection:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdatasource/tableview(_:numberofrowsinsection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdatasource/tableview%28_%3Anumberofrowsinsection%3A%29.json'
content_hash: 'sha256:2b8636ac53320d75'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDataSource](../uitableviewdatasource.md)

# tableView(_:numberOfRowsInSection:)

<sub>Instance Method</sub>

Tells the data source to return the number of rows in a given section of a table view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int
```

## Parameters

- `tableView` — The table-view object requesting this information.

- `section` — An index number identifying a section in `tableView`.

## Return Value

The number of rows in `section`.

## See Also

### Providing the number of rows and sections

- [- numberOfSectionsInTableView:](<numberofsections(in_).md>) — Asks the data source to return the number of sections in the table view.

---
title: 'numberOfSections(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdatasource/numberofsections(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdatasource/numberofsections(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdatasource/numberofsections%28in%3A%29.json'
content_hash: 'sha256:172e745f60184854'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDataSource](../uitableviewdatasource.md)

# numberOfSections(in:)

<sub>Instance Method</sub>

Asks the data source to return the number of sections in the table view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func numberOfSections(in tableView: UITableView) -> Int
```

## Parameters

- `tableView` — An object representing the table view requesting this information.

## Return Value

The number of sections in `tableView`.

## Discussion

If you don’t implement this method, the table configures the table with one section.

## See Also

### Providing the number of rows and sections

- [- tableView:numberOfRowsInSection:](<tableview(__numberofrowsinsection_).md>) — Tells the data source to return the number of rows in a given section of a table view.

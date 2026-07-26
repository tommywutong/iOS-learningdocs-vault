---
title: 'init(tableView:cellProvider:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdiffabledatasourcereference/init(tableview:cellprovider:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdiffabledatasourcereference/init(tableview:cellprovider:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdiffabledatasourcereference/init%28tableview%3Acellprovider%3A%29.json'
content_hash: 'sha256:05d6fb8b14b32dbf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDiffableDataSourceReference](../uitableviewdiffabledatasourcereference.md)

# init(tableView:cellProvider:)

<sub>Initializer</sub>

Creates a diffable data source with the specified cell provider, and connects it to the specified table view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(tableView: UITableView, cellProvider: @escaping UITableViewDiffableDataSourceReferenceCellProvider)
```

## Parameters

- `tableView` — The initialized table view object to connect to the diffable data source.

- `cellProvider` — A closure that creates and returns each of the cells for the table view from the data the diffable data source provides.

## See Also

### Creating a diffable data source

- [UITableViewDiffableDataSourceReferenceCellProvider](../uitableviewdiffabledatasourcereferencecellprovider.md) — A closure that configures and returns a cell for a table view from its diffable data source.

---
title: UITableViewDiffableDataSource.CellProvider
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewdiffabledatasource-2euir/cellprovider
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdiffabledatasource-2euir/cellprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdiffabledatasource-2euir/cellprovider.json'
content_hash: 'sha256:ed967dae0d54fa6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDiffableDataSource](../uitableviewdiffabledatasource-2euir.md)

# UITableViewDiffableDataSource.CellProvider

<sub>Type Alias</sub>

A closure that configures and returns a cell for a table view from its diffable data source.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
typealias CellProvider = (UITableView, IndexPath, ItemIdentifierType) -> UITableViewCell?
```

## Parameters

- `tableView` — The table view to configure this cell for.

- `indexPath` — The index path that specifies the location of the cell in the table view.

- `itemIdentifier` — The identifier of the item for this cell.

## Return Value

A non-`nil` configured cell object. The cell provider must return a valid cell object to the table view.

## See Also

### Creating a diffable data source

- [init(tableView:cellProvider:)](<init(tableview_cellprovider_).md>) — Creates a diffable data source with the specified cell provider, and connects it to the specified table view.

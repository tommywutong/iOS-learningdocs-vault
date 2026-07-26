---
title: UITableViewDiffableDataSourceReferenceCellProvider
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewdiffabledatasourcereferencecellprovider
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdiffabledatasourcereferencecellprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdiffabledatasourcereferencecellprovider.json'
content_hash: 'sha256:4a3c65963de94f29'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITableViewDiffableDataSourceReferenceCellProvider

<sub>Type Alias</sub>

A closure that configures and returns a cell for a table view from its diffable data source.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
typealias UITableViewDiffableDataSourceReferenceCellProvider = (UITableView, IndexPath, Any) -> UITableViewCell?
```

## Parameters

- `tableView` — The table view to configure this cell for.

- `indexPath` — The index path that specifies the location of the cell in the table view.

- `itemIdentifier` — The identifier of the item for this cell.

## Return Value

A non-`nil` configured cell object. The cell provider must return a valid cell object to the table view.

## See Also

### Creating a diffable data source

- [- initWithTableView:cellProvider:](<uitableviewdiffabledatasourcereference/init(tableview_cellprovider_).md>) — Creates a diffable data source with the specified cell provider, and connects it to the specified table view.

---
title: dataSource
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/datasource
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/datasource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/datasource.json'
content_hash: 'sha256:a73f95b86dd3aafe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# dataSource

<sub>Instance Property</sub>

The object that acts as the data source of the table view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var dataSource: (any UITableViewDataSource)? { get set }
```

## Discussion

The data source must adopt the [UITableViewDataSource](../uitableviewdatasource.md) protocol. The data source isn’t retained.

## See Also

### Related Documentation

- [delegate](delegate.md) — The object that acts as the delegate of the table view.

### Providing the data and cells

- [prefetchDataSource](prefetchdatasource.md) — The object that acts as the prefetching data source for the table view, receiving notifications of upcoming cell data requirements.
- [prefetchingEnabled](isprefetchingenabled.md) — A Boolean value that indicates whether to allow cell and data prefetching.
- [UITableViewDataSource](../uitableviewdatasource.md) — The methods that an object adopts to manage data and provide cells for a table view.
- [UITableViewDataSourcePrefetching](../uitableviewdatasourceprefetching.md) — A protocol that provides advance warning of the data requirements for a table view, allowing you to start potentially long-running data operations early.

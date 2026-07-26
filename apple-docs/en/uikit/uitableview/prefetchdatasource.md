---
title: prefetchDataSource
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/prefetchdatasource
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/prefetchdatasource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/prefetchdatasource.json'
content_hash: 'sha256:99032ef058268700'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# prefetchDataSource

<sub>Instance Property</sub>

The object that acts as the prefetching data source for the table view, receiving notifications of upcoming cell data requirements.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var prefetchDataSource: (any UITableViewDataSourcePrefetching)? { get set }
```

## Discussion

Assign an object that conforms to the [UITableViewDataSourcePrefetching](../uitableviewdatasourceprefetching.md) protocol to facilitate prefetching of data for cells to be displayed in the near future. To disable prefetching behavior, set this property to `nil`. This object isn’t retained.

## See Also

### Providing the data and cells

- [dataSource](datasource.md) — The object that acts as the data source of the table view.
- [prefetchingEnabled](isprefetchingenabled.md) — A Boolean value that indicates whether to allow cell and data prefetching.
- [UITableViewDataSource](../uitableviewdatasource.md) — The methods that an object adopts to manage data and provide cells for a table view.
- [UITableViewDataSourcePrefetching](../uitableviewdatasourceprefetching.md) — A protocol that provides advance warning of the data requirements for a table view, allowing you to start potentially long-running data operations early.

---
title: isPrefetchingEnabled
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableview/isprefetchingenabled
source_url: 'https://developer.apple.com/documentation/uikit/uitableview/isprefetchingenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableview/isprefetchingenabled.json'
content_hash: 'sha256:49b021ad85d1b0d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableView](../uitableview.md)

# isPrefetchingEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether to allow cell and data prefetching.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isPrefetchingEnabled: Bool { get set }
```

## Discussion

When [true](../../swift/true.md), the table view may request cells in advance of displaying them. When [false](../../swift/false.md), the table view requests cells when they need to display. Setting this property to [false](../../swift/false.md) also disables data prefetching. The default value of this property is [true](../../swift/true.md).

## See Also

### Providing the data and cells

- [dataSource](datasource.md) — The object that acts as the data source of the table view.
- [prefetchDataSource](prefetchdatasource.md) — The object that acts as the prefetching data source for the table view, receiving notifications of upcoming cell data requirements.
- [UITableViewDataSource](../uitableviewdatasource.md) — The methods that an object adopts to manage data and provide cells for a table view.
- [UITableViewDataSourcePrefetching](../uitableviewdatasourceprefetching.md) — A protocol that provides advance warning of the data requirements for a table view, allowing you to start potentially long-running data operations early.

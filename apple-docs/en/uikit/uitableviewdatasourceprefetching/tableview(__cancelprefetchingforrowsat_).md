---
title: 'tableView(_:cancelPrefetchingForRowsAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdatasourceprefetching/tableview(_:cancelprefetchingforrowsat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdatasourceprefetching/tableview(_:cancelprefetchingforrowsat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdatasourceprefetching/tableview%28_%3Acancelprefetchingforrowsat%3A%29.json'
content_hash: 'sha256:0de718a43670a3e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDataSourcePrefetching](../uitableviewdatasourceprefetching.md)

# tableView(_:cancelPrefetchingForRowsAt:)

<sub>Instance Method</sub>

Cancels a previously triggered data prefetch request.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func tableView(_ tableView: UITableView, cancelPrefetchingForRowsAt indexPaths: [IndexPath])
```

## Parameters

- `tableView` — The table view issuing the cancellation of the prefetch request.

- `indexPaths` — The index paths of the items for which the data is no longer required.

## Discussion

The table view calls this method on the main queue to cancel prefetch requests for cells that are no longer needed. Use this method to cancel operations initiated by a previous call to [- tableView:prefetchRowsAtIndexPaths:](<tableview(__prefetchrowsat_).md>).

For information about how to cancel an asynchronous data loading task, see [Concurrency Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008091).

## See Also

### Fetching the row data

- [- tableView:prefetchRowsAtIndexPaths:](<tableview(__prefetchrowsat_).md>) — Instructs your prefetch data source object to begin preparing data for the cells at the supplied index paths.

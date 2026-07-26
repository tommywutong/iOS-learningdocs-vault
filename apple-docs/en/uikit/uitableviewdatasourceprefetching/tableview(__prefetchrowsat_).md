---
title: 'tableView(_:prefetchRowsAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdatasourceprefetching/tableview(_:prefetchrowsat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdatasourceprefetching/tableview(_:prefetchrowsat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdatasourceprefetching/tableview%28_%3Aprefetchrowsat%3A%29.json'
content_hash: 'sha256:c9f21e47254ef4b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDataSourcePrefetching](../uitableviewdatasourceprefetching.md)

# tableView(_:prefetchRowsAt:)

<sub>Instance Method</sub>

Instructs your prefetch data source object to begin preparing data for the cells at the supplied index paths.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func tableView(_ tableView: UITableView, prefetchRowsAt indexPaths: [IndexPath])
```

## Parameters

- `tableView` — The table view issuing the prefetch request.

- `indexPaths` — The index paths that specify the locations of the items for which the data is to be prefetched. The index paths are sorted in ascending order based on their priority. The first index path corresponds to the row closest to the visibile area, and the last index path corresponds to the row furthest from the visible area.

## Discussion

The table view calls this method on the main dispatch queue as the user scrolls, providing the index paths for cells it is likely to display in the near future. Use your implementation of this method to start any expensive data loading operations. Always load your data asynchronously and forward the results to your table’s data source object. Table views do not call this method for cells they require immediately, so your data source object must also be able to fetch the data itself.

For information about how to create an asynchronous data loading task, see [Concurrency Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008091).

## See Also

### Fetching the row data

- [- tableView:cancelPrefetchingForRowsAtIndexPaths:](<tableview(__cancelprefetchingforrowsat_).md>) — Cancels a previously triggered data prefetch request.

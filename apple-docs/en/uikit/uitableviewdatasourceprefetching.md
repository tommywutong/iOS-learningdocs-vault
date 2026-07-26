---
title: UITableViewDataSourcePrefetching
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewdatasourceprefetching
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdatasourceprefetching'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdatasourceprefetching.json'
content_hash: 'sha256:360116e7567b67cc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITableViewDataSourcePrefetching

<sub>Protocol</sub>

A protocol that provides advance warning of the data requirements for a table view, allowing you to start potentially long-running data operations early.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UITableViewDataSourcePrefetching : NSObjectProtocol
```

## Overview

You use a prefetch data source object in conjunction with your table view’s data source to begin loading data for cells before the [- tableView:cellForRowAtIndexPath:](<uitableviewdatasource/tableview(__cellforrowat_).md>) data source method is called. The following steps are required to support a prefetch data source to your table view:

- Create the table view and its regular data source.
- Create an object that adopts the [UITableViewDataSourcePrefetching](uitableviewdatasourceprefetching.md) protocol, and assign it to the [prefetchDataSource](uitableview/prefetchdatasource.md) property on the table view.
- Initiate asynchronous loading of the data required for the cells at the specified index paths in your implementation of [- tableView:prefetchRowsAtIndexPaths:](<uitableviewdatasourceprefetching/tableview(__prefetchrowsat_).md>).
- Prepare the cell for display using the prefetched data in your [- tableView:cellForRowAtIndexPath:](<uitableviewdatasource/tableview(__cellforrowat_).md>) data source method.
- Cancel pending data load operations when the table view informs you that the data is no longer required in the [- tableView:cancelPrefetchingForRowsAtIndexPaths:](<uitableviewdatasourceprefetching/tableview(__cancelprefetchingforrowsat_).md>) method.

> [!note] Note
> The prefetch method isn’t necessarily called for every cell in the table view. For details about a suggested approach to loading data, see [Load data asynchronously](uitableviewdatasourceprefetching.md#Load-data-asynchronously).

When configuring the table view object, assign your prefetch data source to its [prefetchDataSource](uitableview/prefetchdatasource.md) property. For more information about how a table view works, see [UITableView](uitableview.md).

### Load data asynchronously

The [- tableView:prefetchRowsAtIndexPaths:](<uitableviewdatasourceprefetching/tableview(__prefetchrowsat_).md>) method isn’t necessarily called for every cell in the table view. Your implementation of [- tableView:cellForRowAtIndexPath:](<uitableviewdatasource/tableview(__cellforrowat_).md>) must therefore be able to cope with the following potential situations:

- Data has been loaded via the prefetch request, and is ready to be displayed.
- Data is currently being prefetched, but isn’t yet available.
- Data hasn’t yet been requested.

One approach that handles all of these situations is to use [Operation](../foundation/operation.md) to load the data for each row. You create the [Operation](../foundation/operation.md) object and store it in the prefetch method. The data source method can then either retrieve the operation and the result, or create it if it doesn’t exist. For further information about how you can use asynchronous programming models to achieve this desired behavior, see [Concurrency Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008091).

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Fetching the row data

- [- tableView:prefetchRowsAtIndexPaths:](<uitableviewdatasourceprefetching/tableview(__prefetchrowsat_).md>) — Instructs your prefetch data source object to begin preparing data for the cells at the supplied index paths.
- [- tableView:cancelPrefetchingForRowsAtIndexPaths:](<uitableviewdatasourceprefetching/tableview(__cancelprefetchingforrowsat_).md>) — Cancels a previously triggered data prefetch request.

## See Also

### Data

- [Filling a table with data](filling-a-table-with-data.md) — Create and configure cells for your table dynamically using a data source object, or provide them statically from your storyboard.
- [Asynchronously loading images into table and collection views](asynchronously-loading-images-into-table-and-collection-views.md) — Store and fetch images asynchronously to make your app more responsive.
- [UITableViewDataSource](uitableviewdatasource.md) — The methods that an object adopts to manage data and provide cells for a table view.
- [UITableViewDiffableDataSource](uitableviewdiffabledatasource-2euir.md) — The object you use to manage data and provide cells for a table view.
- [NSDiffableDataSourceSnapshot](nsdiffabledatasourcesnapshot-swift.struct.md) — A representation of the state of the data in a view at a specific point in time.
- [UILocalizedIndexedCollation](uilocalizedindexedcollation.md) — An object that organizes, sorts, and localizes the data for a table view that has a section index.
- [UIDataSourceTranslating](uidatasourcetranslating.md) — An advanced interface for managing a data source object.
- [UIRefreshControl](uirefreshcontrol.md) — A standard control that can initiate the refreshing of a scroll view’s contents.

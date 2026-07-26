---
title: searchContentsController
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（8.0 起废弃）, iPadOS 3.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uisearchdisplaycontroller/searchcontentscontroller
source_url: 'https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller/searchcontentscontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchdisplaycontroller/searchcontentscontroller.json'
content_hash: 'sha256:6e4c641061d988ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchDisplayController](../uisearchdisplaycontroller.md)

# searchContentsController

<sub>Instance Property</sub>

The view controller that manages the contents being searched.

> [!warning] Deprecated
> For more information, see [UISearchDisplayController](../uisearchdisplaycontroller.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var searchContentsController: UIViewController { get }
```

## Discussion

This is typically an instance of [UITableViewController](../uitableviewcontroller.md).

## See Also

### Configuring a search bar

- [delegate](delegate.md) — The controller’s delegate. _(deprecated)_
- [searchBar](searchbar.md) — The search bar. _(deprecated)_
- [searchResultsTableView](searchresultstableview.md) — The table view in which the search results are displayed. _(deprecated)_
- [searchResultsDataSource](searchresultsdatasource.md) — The data source for the table view in which the search results are displayed. _(deprecated)_
- [searchResultsDelegate](searchresultsdelegate.md) — The delegate for the table view in which the search results are displayed. _(deprecated)_
- [searchResultsTitle](searchresultstitle.md) — The title for the search results view. _(deprecated)_
- [displaysSearchBarInNavigationBar](displayssearchbarinnavigationbar.md) — Specifies that the navigation bar contains a search bar. _(deprecated)_
- [navigationItem](navigationitem.md) — Represents the search display controller in a navigation controller’s navigation bar. _(deprecated)_

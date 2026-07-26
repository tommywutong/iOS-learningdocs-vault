---
title: searchResultsDataSource
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（8.0 起废弃）, iPadOS 3.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uisearchdisplaycontroller/searchresultsdatasource
source_url: 'https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller/searchresultsdatasource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchdisplaycontroller/searchresultsdatasource.json'
content_hash: 'sha256:f93f7fedbef3a9ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchDisplayController](../uisearchdisplaycontroller.md)

# searchResultsDataSource

<sub>Instance Property</sub>

The data source for the table view in which the search results are displayed.

> [!warning] Deprecated
> For more information, see [UISearchDisplayController](../uisearchdisplaycontroller.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
weak var searchResultsDataSource: (any UITableViewDataSource)? { get set }
```

## Discussion

The default is `nil`.

## See Also

### Configuring a search bar

- [delegate](delegate.md) — The controller’s delegate. _(deprecated)_
- [searchBar](searchbar.md) — The search bar. _(deprecated)_
- [searchContentsController](searchcontentscontroller.md) — The view controller that manages the contents being searched. _(deprecated)_
- [searchResultsTableView](searchresultstableview.md) — The table view in which the search results are displayed. _(deprecated)_
- [searchResultsDelegate](searchresultsdelegate.md) — The delegate for the table view in which the search results are displayed. _(deprecated)_
- [searchResultsTitle](searchresultstitle.md) — The title for the search results view. _(deprecated)_
- [displaysSearchBarInNavigationBar](displayssearchbarinnavigationbar.md) — Specifies that the navigation bar contains a search bar. _(deprecated)_
- [navigationItem](navigationitem.md) — Represents the search display controller in a navigation controller’s navigation bar. _(deprecated)_

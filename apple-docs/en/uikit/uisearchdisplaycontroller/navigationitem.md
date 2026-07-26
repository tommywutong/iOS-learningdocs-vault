---
title: navigationItem
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+（8.0 起废弃）, iPadOS 7.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uisearchdisplaycontroller/navigationitem
source_url: 'https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller/navigationitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchdisplaycontroller/navigationitem.json'
content_hash: 'sha256:c07f2c60f2be05e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchDisplayController](../uisearchdisplaycontroller.md)

# navigationItem

<sub>Instance Property</sub>

Represents the search display controller in a navigation controller’s navigation bar.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var navigationItem: UINavigationItem? { get }
```

## Discussion

You can configure the navigation item as described in the [UINavigationItem](../uinavigationitem.md), with the exception of configuring the title view.

> [!important] Important
> The system raises an exception if you attempt to set the [titleView](../uinavigationitem/titleview.md) property for a search display controller’s navigation item.

## See Also

### Configuring a search bar

- [delegate](delegate.md) — The controller’s delegate. _(deprecated)_
- [searchBar](searchbar.md) — The search bar. _(deprecated)_
- [searchContentsController](searchcontentscontroller.md) — The view controller that manages the contents being searched. _(deprecated)_
- [searchResultsTableView](searchresultstableview.md) — The table view in which the search results are displayed. _(deprecated)_
- [searchResultsDataSource](searchresultsdatasource.md) — The data source for the table view in which the search results are displayed. _(deprecated)_
- [searchResultsDelegate](searchresultsdelegate.md) — The delegate for the table view in which the search results are displayed. _(deprecated)_
- [searchResultsTitle](searchresultstitle.md) — The title for the search results view. _(deprecated)_
- [displaysSearchBarInNavigationBar](displayssearchbarinnavigationbar.md) — Specifies that the navigation bar contains a search bar. _(deprecated)_

---
title: displaysSearchBarInNavigationBar
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+（8.0 起废弃）, iPadOS 7.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uisearchdisplaycontroller/displayssearchbarinnavigationbar
source_url: 'https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller/displayssearchbarinnavigationbar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchdisplaycontroller/displayssearchbarinnavigationbar.json'
content_hash: 'sha256:bf20422e9b293e33'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchDisplayController](../uisearchdisplaycontroller.md)

# displaysSearchBarInNavigationBar

<sub>Instance Property</sub>

Specifies that the navigation bar contains a search bar.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var displaysSearchBarInNavigationBar: Bool { get set }
```

## Discussion

When you return [true](../../swift/true.md) to display the search bar in a navigation bar, the system uses the search display controller’s [navigationItem](navigationitem.md) property and ignores the navigation item, if set, of the [searchContentsController](searchcontentscontroller.md) view controller. The displayed search field occupies as much width in the navigation bar as possible.

A search bar displayed in a navigation bar cannot have a scope bar.

> [!important] Important
> The system raises an exception if you set the [showsScopeBar](../uisearchbar/showsscopebar.md) property to [true](../../swift/true.md) in a search bar that is displayed in a navigation bar.

## See Also

### Configuring a search bar

- [delegate](delegate.md) — The controller’s delegate. _(deprecated)_
- [searchBar](searchbar.md) — The search bar. _(deprecated)_
- [searchContentsController](searchcontentscontroller.md) — The view controller that manages the contents being searched. _(deprecated)_
- [searchResultsTableView](searchresultstableview.md) — The table view in which the search results are displayed. _(deprecated)_
- [searchResultsDataSource](searchresultsdatasource.md) — The data source for the table view in which the search results are displayed. _(deprecated)_
- [searchResultsDelegate](searchresultsdelegate.md) — The delegate for the table view in which the search results are displayed. _(deprecated)_
- [searchResultsTitle](searchresultstitle.md) — The title for the search results view. _(deprecated)_
- [navigationItem](navigationitem.md) — Represents the search display controller in a navigation controller’s navigation bar. _(deprecated)_

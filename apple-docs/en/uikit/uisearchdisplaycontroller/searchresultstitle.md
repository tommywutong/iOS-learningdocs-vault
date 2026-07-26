---
title: searchResultsTitle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+（8.0 起废弃）, iPadOS 5.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uisearchdisplaycontroller/searchresultstitle
source_url: 'https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller/searchresultstitle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchdisplaycontroller/searchresultstitle.json'
content_hash: 'sha256:b10c9c4cea6d01fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchDisplayController](../uisearchdisplaycontroller.md)

# searchResultsTitle

<sub>Instance Property</sub>

The title for the search results view.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var searchResultsTitle: String? { get set }
```

## Discussion

The default value is `nil`.

If the value is `nil`, the controller uses the default title string.

## See Also

### Configuring a search bar

- [delegate](delegate.md) — The controller’s delegate. _(deprecated)_
- [searchBar](searchbar.md) — The search bar. _(deprecated)_
- [searchContentsController](searchcontentscontroller.md) — The view controller that manages the contents being searched. _(deprecated)_
- [searchResultsTableView](searchresultstableview.md) — The table view in which the search results are displayed. _(deprecated)_
- [searchResultsDataSource](searchresultsdatasource.md) — The data source for the table view in which the search results are displayed. _(deprecated)_
- [searchResultsDelegate](searchresultsdelegate.md) — The delegate for the table view in which the search results are displayed. _(deprecated)_
- [displaysSearchBarInNavigationBar](displayssearchbarinnavigationbar.md) — Specifies that the navigation bar contains a search bar. _(deprecated)_
- [navigationItem](navigationitem.md) — Represents the search display controller in a navigation controller’s navigation bar. _(deprecated)_

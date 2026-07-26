---
title: 'searchDisplayController(_:willHideSearchResultsTableView:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（8.0 起废弃）, iPadOS 3.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uisearchdisplaydelegate/searchdisplaycontroller(_:willhidesearchresultstableview:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchdisplaydelegate/searchdisplaycontroller(_:willhidesearchresultstableview:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchdisplaydelegate/searchdisplaycontroller%28_%3Awillhidesearchresultstableview%3A%29.json'
content_hash: 'sha256:29e469cc053fa531'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchDisplayDelegate](../uisearchdisplaydelegate.md)

# searchDisplayController(_:willHideSearchResultsTableView:)

<sub>Instance Method</sub>

Tells the delegate that the controller is about to hide its table view.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func searchDisplayController(_ controller: UISearchDisplayController, willHideSearchResultsTableView tableView: UITableView)
```

## Parameters

- `controller` — The search display controller for which the receiver is the delegate.

- `tableView` — The search display controller’s table view.

## See Also

### Showing and hiding the table view

- [- searchDisplayController:willShowSearchResultsTableView:](<searchdisplaycontroller(__willshowsearchresultstableview_).md>) — Tells the delegate that the controller is about to display its table view. _(deprecated)_
- [- searchDisplayController:didShowSearchResultsTableView:](<searchdisplaycontroller(__didshowsearchresultstableview_).md>) — Tells the delegate that the controller just displayed its table view. _(deprecated)_
- [- searchDisplayController:didHideSearchResultsTableView:](<searchdisplaycontroller(__didhidesearchresultstableview_).md>) — Tells the delegate that the controller just hid its table view. _(deprecated)_

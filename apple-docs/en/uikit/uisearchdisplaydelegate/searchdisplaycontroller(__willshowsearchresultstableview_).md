---
title: 'searchDisplayController(_:willShowSearchResultsTableView:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（8.0 起废弃）, iPadOS 3.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uisearchdisplaydelegate/searchdisplaycontroller(_:willshowsearchresultstableview:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchdisplaydelegate/searchdisplaycontroller(_:willshowsearchresultstableview:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchdisplaydelegate/searchdisplaycontroller%28_%3Awillshowsearchresultstableview%3A%29.json'
content_hash: 'sha256:718a105cdc249721'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchDisplayDelegate](../uisearchdisplaydelegate.md)

# searchDisplayController(_:willShowSearchResultsTableView:)

<sub>Instance Method</sub>

Tells the delegate that the controller is about to display its table view.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func searchDisplayController(_ controller: UISearchDisplayController, willShowSearchResultsTableView tableView: UITableView)
```

## Parameters

- `controller` — The search display controller for which the receiver is the delegate.

- `tableView` — The search display controller’s table view.

## See Also

### Showing and hiding the table view

- [- searchDisplayController:didShowSearchResultsTableView:](<searchdisplaycontroller(__didshowsearchresultstableview_).md>) — Tells the delegate that the controller just displayed its table view. _(deprecated)_
- [- searchDisplayController:willHideSearchResultsTableView:](<searchdisplaycontroller(__willhidesearchresultstableview_).md>) — Tells the delegate that the controller is about to hide its table view. _(deprecated)_
- [- searchDisplayController:didHideSearchResultsTableView:](<searchdisplaycontroller(__didhidesearchresultstableview_).md>) — Tells the delegate that the controller just hid its table view. _(deprecated)_

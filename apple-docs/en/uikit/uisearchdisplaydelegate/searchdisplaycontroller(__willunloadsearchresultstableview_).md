---
title: 'searchDisplayController(_:willUnloadSearchResultsTableView:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（8.0 起废弃）, iPadOS 3.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uisearchdisplaydelegate/searchdisplaycontroller(_:willunloadsearchresultstableview:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchdisplaydelegate/searchdisplaycontroller(_:willunloadsearchresultstableview:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchdisplaydelegate/searchdisplaycontroller%28_%3Awillunloadsearchresultstableview%3A%29.json'
content_hash: 'sha256:569eaeb6487072cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchDisplayDelegate](../uisearchdisplaydelegate.md)

# searchDisplayController(_:willUnloadSearchResultsTableView:)

<sub>Instance Method</sub>

Tells the delegate that the controller is about to unload its table view.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func searchDisplayController(_ controller: UISearchDisplayController, willUnloadSearchResultsTableView tableView: UITableView)
```

## Parameters

- `controller` — The search display controller for which the receiver is the delegate.

- `tableView` — The search display controller’s table view.

## See Also

### Loading and unloading the table view

- [- searchDisplayController:didLoadSearchResultsTableView:](<searchdisplaycontroller(__didloadsearchresultstableview_).md>) — Tells the delegate that the controller has loaded its table view. _(deprecated)_

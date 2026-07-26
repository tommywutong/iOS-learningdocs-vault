---
title: 'searchDisplayController(_:shouldReloadTableForSearch:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（8.0 起废弃）, iPadOS 3.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uisearchdisplaydelegate/searchdisplaycontroller(_:shouldreloadtableforsearch:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchdisplaydelegate/searchdisplaycontroller(_:shouldreloadtableforsearch:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchdisplaydelegate/searchdisplaycontroller%28_%3Ashouldreloadtableforsearch%3A%29.json'
content_hash: 'sha256:f38333a92278dd13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchDisplayDelegate](../uisearchdisplaydelegate.md)

# searchDisplayController(_:shouldReloadTableForSearch:)

<sub>Instance Method</sub>

Asks the delegate if the table view should be reloaded for a given search string.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func searchDisplayController(_ controller: UISearchDisplayController, shouldReloadTableForSearch searchString: String?) -> Bool
```

## Parameters

- `controller` — The search display controller for which the receiver is the delegate.

- `searchString` — The string in the search bar.

## Return Value

[true](../../swift/true.md) if the display controller should reload the data in its table view, otherwise [false](../../swift/false.md).

## Discussion

If you don’t implement this method, then the results table is reloaded as soon as the search string changes.

You might implement this method if you want to perform an asynchronous search. You would initiate the search in this method, then return [false](../../swift/false.md). You would reload the table when you have results.

## See Also

### Responding to changes in search criteria

- [- searchDisplayController:shouldReloadTableForSearchScope:](<searchdisplaycontroller(__shouldreloadtableforsearchscope_).md>) — Asks the delegate if the table view should be reloaded for a given scope. _(deprecated)_

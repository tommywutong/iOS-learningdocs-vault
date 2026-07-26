---
title: 'searchDisplayController(_:shouldReloadTableForSearchScope:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（8.0 起废弃）, iPadOS 3.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uisearchdisplaydelegate/searchdisplaycontroller(_:shouldreloadtableforsearchscope:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchdisplaydelegate/searchdisplaycontroller(_:shouldreloadtableforsearchscope:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchdisplaydelegate/searchdisplaycontroller%28_%3Ashouldreloadtableforsearchscope%3A%29.json'
content_hash: 'sha256:c259d594fd136985'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchDisplayDelegate](../uisearchdisplaydelegate.md)

# searchDisplayController(_:shouldReloadTableForSearchScope:)

<sub>Instance Method</sub>

Asks the delegate if the table view should be reloaded for a given scope.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func searchDisplayController(_ controller: UISearchDisplayController, shouldReloadTableForSearchScope searchOption: Int) -> Bool
```

## Parameters

- `controller` — The search display controller for which the receiver is the delegate.

- `searchOption` — The index of the selected scope button in the search bar.

## Return Value

[true](../../swift/true.md) if the display controller should reload the data in its table view, otherwise [false](../../swift/false.md).

## Discussion

If you don’t implement this method, then the results table is reloaded as soon as the scope button selection changes.

You might implement this method if you want to perform an asynchronous search: you would initiate the search in this method, then return [false](../../swift/false.md), and reload the table when you have results.

## See Also

### Related Documentation

- [selectedScopeButtonIndex](../uisearchbar/selectedscopebuttonindex.md) — The index of the selected scope button.

### Responding to changes in search criteria

- [- searchDisplayController:shouldReloadTableForSearchString:](<searchdisplaycontroller(__shouldreloadtableforsearch_).md>) — Asks the delegate if the table view should be reloaded for a given search string. _(deprecated)_

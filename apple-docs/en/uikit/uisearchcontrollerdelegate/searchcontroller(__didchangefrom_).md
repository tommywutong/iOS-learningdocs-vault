---
title: 'searchController(_:didChangeFrom:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchcontrollerdelegate/searchcontroller(_:didchangefrom:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchcontrollerdelegate/searchcontroller(_:didchangefrom:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchcontrollerdelegate/searchcontroller%28_%3Adidchangefrom%3A%29.json'
content_hash: 'sha256:6d8186b375dc9114'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchControllerDelegate](../uisearchcontrollerdelegate.md)

# searchController(_:didChangeFrom:)

<sub>Instance Method</sub>

Notifies the delegate after the search bar placement changes.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func searchController(_ searchController: UISearchController, didChangeFrom previousPlacement: UINavigationItem.SearchBarPlacement)
```

## Parameters

- `searchController` — The search controller associated with the search bar.

- `previousPlacement` — The previous search bar placement.

## Discussion

The system calls this method after a search bar placement change occurs. Implement this method if you need to make any custom changes to your search suggestions UI according to the previous search bar placement.

The system calls this method after [- searchController:willChangeToSearchBarPlacement:](<searchcontroller(__willchangeto_).md>).

## See Also

### Responding to search bar placement updates

- [- searchController:willChangeToSearchBarPlacement:](<searchcontroller(__willchangeto_).md>) — Notifies the delegate before the search bar placement changes.

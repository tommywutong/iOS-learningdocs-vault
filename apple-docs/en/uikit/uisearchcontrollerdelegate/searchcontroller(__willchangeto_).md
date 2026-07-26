---
title: 'searchController(_:willChangeTo:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchcontrollerdelegate/searchcontroller(_:willchangeto:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchcontrollerdelegate/searchcontroller(_:willchangeto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchcontrollerdelegate/searchcontroller%28_%3Awillchangeto%3A%29.json'
content_hash: 'sha256:1a0266b5608c8159'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchControllerDelegate](../uisearchcontrollerdelegate.md)

# searchController(_:willChangeTo:)

<sub>Instance Method</sub>

Notifies the delegate before the search bar placement changes.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func searchController(_ searchController: UISearchController, willChangeTo newPlacement: UINavigationItem.SearchBarPlacement)
```

## Parameters

- `searchController` — The search controller associated with the search bar.

- `newPlacement` — The new search bar placement.

## Discussion

The system calls this method before a search bar placement change occurs, such as in response to a layout change that alters the amount of available space in the navigation bar. Implement this method if you need to make any custom changes to your search suggestions UI according to the new search bar placement.

The system calls this method before [- searchController:didChangeFromSearchBarPlacement:](<searchcontroller(__didchangefrom_).md>).

## See Also

### Responding to search bar placement updates

- [- searchController:didChangeFromSearchBarPlacement:](<searchcontroller(__didchangefrom_).md>) — Notifies the delegate after the search bar placement changes.

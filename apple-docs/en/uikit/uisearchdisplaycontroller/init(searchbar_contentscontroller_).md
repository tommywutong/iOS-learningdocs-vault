---
title: 'init(searchBar:contentsController:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+（8.0 起废弃）, iPadOS 3.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uisearchdisplaycontroller/init(searchbar:contentscontroller:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller/init(searchbar:contentscontroller:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchdisplaycontroller/init%28searchbar%3Acontentscontroller%3A%29.json'
content_hash: 'sha256:ab8337217b971f6a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchDisplayController](../uisearchdisplaycontroller.md)

# init(searchBar:contentsController:)

<sub>Initializer</sub>

Returns a display controller initialized with the given search bar and contents controller.

> [!warning] Deprecated
> For more information, see [UISearchDisplayController](../uisearchdisplaycontroller.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
init(searchBar: UISearchBar, contentsController viewController: UIViewController)
```

## Parameters

- `searchBar` — A search bar. The search bar must not currently be associated with another search display controller.

- `viewController` — The view controller that manages display of the original contents that are to be searched. The view controller must not currently be associated with another search display controller.

## Return Value

A search display controller initialized with the given search bar and contents controller.

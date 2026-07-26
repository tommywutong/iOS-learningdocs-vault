---
title: 'init(searchController:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchcontainerviewcontroller/init(searchcontroller:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchcontainerviewcontroller/init(searchcontroller:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchcontainerviewcontroller/init%28searchcontroller%3A%29.json'
content_hash: 'sha256:f81f5156444c33c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchContainerViewController](../uisearchcontainerviewcontroller.md)

# init(searchController:)

<sub>Initializer</sub>

Initializes and returns a search container view controller with the specified search controller object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(searchController: UISearchController)
```

## Parameters

- `searchController` — The search controller managing the search results. This parameter must not be `nil`.

## Return Value

An initialized search container view controller.

## Discussion

After initializing the search container view controller, embed it in your container view controller normally.

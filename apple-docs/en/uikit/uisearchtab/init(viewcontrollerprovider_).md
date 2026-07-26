---
title: 'init(viewControllerProvider:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchtab/init(viewcontrollerprovider:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchtab/init(viewcontrollerprovider:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchtab/init%28viewcontrollerprovider%3A%29.json'
content_hash: 'sha256:260bd7a664be77e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchTab](../uisearchtab.md)

# init(viewControllerProvider:)

<sub>Initializer</sub>

Creates a search tab with a system localized title and image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(viewControllerProvider: ((UITab) -> UIViewController)? = nil)
```

## Parameters

- `viewControllerProvider` — The view controller that the system presents when someone selects the tab.

---
title: 'init(title:image:identifier:viewControllerProvider:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitab/init(title:image:identifier:viewcontrollerprovider:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitab/init(title:image:identifier:viewcontrollerprovider:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitab/init%28title%3Aimage%3Aidentifier%3Aviewcontrollerprovider%3A%29.json'
content_hash: 'sha256:3738b77dd662e080'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITab](../uitab.md)

# init(title:image:identifier:viewControllerProvider:)

<sub>Initializer</sub>

Creates a tab object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(title: String, image: UIImage?, identifier: String, viewControllerProvider: ((UITab) -> UIViewController)? = nil)
```

## Parameters

- `title` — The tab’s title.

- `image` — The tab’s image.

- `identifier` — An identifier string for the tab. Each identifier must be unique across all the tabs managed by a [UITabBarController](../uitabbarcontroller.md).

- `viewControllerProvider` — The view controller that the system presents when someone selects the tab.

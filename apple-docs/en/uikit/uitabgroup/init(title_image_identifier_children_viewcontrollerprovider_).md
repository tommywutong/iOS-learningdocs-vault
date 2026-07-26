---
title: 'init(title:image:identifier:children:viewControllerProvider:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitabgroup/init(title:image:identifier:children:viewcontrollerprovider:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabgroup/init(title:image:identifier:children:viewcontrollerprovider:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabgroup/init%28title%3Aimage%3Aidentifier%3Achildren%3Aviewcontrollerprovider%3A%29.json'
content_hash: 'sha256:134281029d599948'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabGroup](../uitabgroup.md)

# init(title:image:identifier:children:viewControllerProvider:)

<sub>Initializer</sub>

Creates a tab group.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(title: String, image: UIImage?, identifier: String, children: [UITab], viewControllerProvider: ((UITab) -> UIViewController)? = nil)
```

## Parameters

- `title` — The group’s title.

- `image` — The group’s image.

- `identifier` — An identifier string for the tab.

- `children` — The contained tab items.

- `viewControllerProvider` — The view controller that the system presents when someone selects the group from the tab bar.

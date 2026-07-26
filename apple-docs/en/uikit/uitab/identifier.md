---
title: identifier
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitab/identifier
source_url: 'https://developer.apple.com/documentation/uikit/uitab/identifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitab/identifier.json'
content_hash: 'sha256:9aa82cb4743dfaaa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITab](../uitab.md)

# identifier

<sub>Instance Property</sub>

A string identifier for a tab.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var identifier: String { get }
```

## Discussion

Each identifier must be unique across all the tabs managed by a [UITabBarController](../uitabbarcontroller.md).

## See Also

### Accessing a tab’s appearance

- [title](title.md) — A tab’s title.
- [subtitle](subtitle.md) — A tab’s subtitle.
- [image](image.md) — A tab’s image.
- [badgeValue](badgevalue.md) — A tab’s badge value.
- [viewController](viewcontroller.md) — The view controller that the system presents when someone selects a tab.

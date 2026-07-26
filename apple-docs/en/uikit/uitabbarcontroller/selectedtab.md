---
title: selectedTab
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbarcontroller/selectedtab
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontroller/selectedtab'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontroller/selectedtab.json'
content_hash: 'sha256:80c6ffffe0b12509'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarController](../uitabbarcontroller.md)

# selectedTab

<sub>Instance Property</sub>

The currently selected tab, which can be a root tab or any of their descendants.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var selectedTab: UITab? { get set }
```

## Discussion

The default value for this property is `nil`.

## See Also

### Managing the selected tab

- [selectedViewController](selectedviewcontroller.md) — The view controller associated with the currently selected tab item.
- [selectedIndex](selectedindex.md) — The index of the view controller associated with the currently selected tab item.

---
title: 'tab(forIdentifier:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitabbarcontroller/tab(foridentifier:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontroller/tab(foridentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontroller/tab%28foridentifier%3A%29.json'
content_hash: 'sha256:f1043497870a99e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarController](../uitabbarcontroller.md)

# tab(forIdentifier:)

<sub>Instance Method</sub>

Returns the `tab` matching the specified `identifier` in the tab bar controller’s tabs. Returns nil if no tab is found matching the `identifier`.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func tab(forIdentifier identifier: String) -> UITab?
```

## See Also

### Accessing the tab bar controller properties

- [tabBar](tabbar.md) — The tab bar view associated with this controller.

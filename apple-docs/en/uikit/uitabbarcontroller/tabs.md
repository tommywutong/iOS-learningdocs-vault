---
title: tabs
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbarcontroller/tabs
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontroller/tabs'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontroller/tabs.json'
content_hash: 'sha256:ffc7218387bdd47f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarController](../uitabbarcontroller.md)

# tabs

<sub>Instance Property</sub>

An array of tabs that the tab bar displays.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var tabs: [UITab] { get set }
```

## Discussion

To set the tab bar’s content, assign an array of [UITab](../uitab.md) objects to this property. For more information, see [Elevating your iPad app with a tab bar and sidebar](../elevating-your-ipad-app-with-a-tab-bar-and-sidebar.md).

## See Also

### Assigning tabs

- [- setTabs:animated:](<settabs(__animated_).md>) — Sets the root tabs of the tab bar controller, with an option to animate the change.
- [- performBatchUpdates:](<performbatchupdates(__).md>) — Animates multiple tab changes as a single update. _(beta)_

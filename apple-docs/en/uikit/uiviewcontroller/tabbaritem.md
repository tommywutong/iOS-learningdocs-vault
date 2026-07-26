---
title: tabBarItem
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/tabbaritem
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/tabbaritem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/tabbaritem.json'
content_hash: 'sha256:7e7387e711858d06'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# tabBarItem

<sub>Instance Property</sub>

The tab bar item that represents the view controller when added to a tab bar controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var tabBarItem: UITabBarItem! { get set }
```

## Discussion

This is a unique instance of [UITabBarItem](../uitabbaritem.md) created to represent the view controller when it is a child of a tab bar controller. The first time the property is accessed, the [UITabBarItem](../uitabbaritem.md) is created. Therefore, you should not access this property if you are not using a tab bar controller to display the view controller. To ensure the tab bar item is configured, you can either override this property and add code to create the bar button items when first accessed or create the items in your view controller’s initialization code.

The default value is a tab bar item that displays the view controller’s title.

## See Also

### Configuring tab bar content

- [tab](tab.md) — The `UITab` instance that was used to create the receiver, and represents the view controller. Default is nil.
- [tabBarObservedScrollView](tabbarobservedscrollview.md) — The full-screen scroll view to synchronize with a scrolling tab bar. _(deprecated)_

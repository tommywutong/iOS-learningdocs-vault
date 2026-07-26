---
title: tabBar
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbarcontroller/tabbar
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontroller/tabbar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontroller/tabbar.json'
content_hash: 'sha256:81b987ed7f806c6d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarController](../uitabbarcontroller.md)

# tabBar

<sub>Instance Property</sub>

The tab bar view associated with this controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var tabBar: UITabBar { get }
```

## Discussion

You should never attempt to manipulate the [UITabBar](../uitabbar.md) object itself stored in this property. If you attempt to do so, the tab bar view throws an exception. To configure the items for your tab bar interface, you should instead assign one or more custom view controllers to the [viewControllers](viewcontrollers.md) property. The tab bar collects the needed tab bar items from the view controllers you specify.

The tab bar view provided by this property is only for situations where you want to display an action sheet using the [- showFromTabBar:](<../uiactionsheet/show(from_)-9i3tw.md>) method of the [UIActionSheet](../uiactionsheet.md) class.

## See Also

### Accessing the tab bar controller properties

- [- tabForIdentifier:](<tab(foridentifier_).md>) — Returns the `tab` matching the specified `identifier` in the tab bar controller’s tabs. Returns nil if no tab is found matching the `identifier`.

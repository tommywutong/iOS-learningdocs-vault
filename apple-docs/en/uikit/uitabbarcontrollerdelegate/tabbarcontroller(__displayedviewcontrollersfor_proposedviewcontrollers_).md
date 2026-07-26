---
title: 'tabBarController(_:displayedViewControllersFor:proposedViewControllers:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller(_:displayedviewcontrollersfor:proposedviewcontrollers:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller(_:displayedviewcontrollersfor:proposedviewcontrollers:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller%28_%3Adisplayedviewcontrollersfor%3Aproposedviewcontrollers%3A%29.json'
content_hash: 'sha256:71888c8ee9a874c9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBarControllerDelegate](../uitabbarcontrollerdelegate.md)

# tabBarController(_:displayedViewControllersFor:proposedViewControllers:)

<sub>Instance Method</sub>

Used with `UITabGroup.managingNavigationController`, this method allows the delegate to customize the displayed view controllers within the navigation stack for each level of selected tab. This method is called by the system if the selected tab in the `UITabBarController` belongs to or is in the hierarchy of a managing tab group (i.e. a `UITabGroup` with a non-nil `managingNavigationController`). By default, if this method is not implemented, the system will build the navigation stack by adding each tab’s `viewController` into the hierarchy, if one exists. This is especially useful to hide certain view controllers when transitioning between compact and regular size classes.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func tabBarController(_ tabBarController: UITabBarController, displayedViewControllersFor tab: UITab, proposedViewControllers: [UIViewController]) -> [UIViewController]
```

## Parameters

- `tabBarController` — The tab bar controller managed by the delegate.

- `tab` — The tab for which the displayed view controllers is being requested for by its `managingTabGroup`. Each tab in the selection hierarchy will be called once.

- `proposedViewControllers` — The proposed view controllers for the given tab. In general, the proposed view controller is a single-item array of the tab’s viewController. If other view controllers are pushed onto the navigation stack, they will be part of the last (leaf-most) tab’s `proposedViewControllers` such that they are preserved between updates.

## Return Value

A list of view controllers represented by the tab in the navigation stack.

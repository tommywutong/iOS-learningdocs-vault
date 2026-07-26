---
title: toolbar
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationcontroller/toolbar
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationcontroller/toolbar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationcontroller/toolbar.json'
content_hash: 'sha256:cc4c030e265a0dd6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationController](../uinavigationcontroller.md)

# toolbar

<sub>Instance Property</sub>

The custom toolbar associated with the navigation controller.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var toolbar: UIToolbar! { get }
```

## Discussion

This property contains a reference to the built-in toolbar managed by the navigation controller. Access to this toolbar is provided solely for clients that want to present an action sheet from the toolbar. You should not modify the [UIToolbar](../uitoolbar.md) object directly.

Management of this toolbar’s contents is done through the custom view controllers associated with this navigation controller. For each view controller on the navigation stack, you can assign a custom set of toolbar items using the [- setToolbarItems:animated:](<../uiviewcontroller/settoolbaritems(__animated_).md>) method of [UIViewController](../uiviewcontroller.md).

The visibility of this toolbar is controlled by the [toolbarHidden](istoolbarhidden.md) property. The toolbar also obeys the [hidesBottomBarWhenPushed](../uiviewcontroller/hidesbottombarwhenpushed.md) property of the currently visible view controller and hides and shows itself automatically as needed.

## See Also

### Configuring custom toolbars

- [- setToolbarHidden:animated:](<settoolbarhidden(__animated_).md>) — Changes the visibility of the navigation controller’s built-in toolbar.
- [toolbarHidden](istoolbarhidden.md) — A Boolean indicating whether the navigation controller’s built-in toolbar is visible.
- [UINavigationControllerHideShowBarDuration](hideshowbarduration.md) — A variable that specifies the duration when animating the navigation bar.

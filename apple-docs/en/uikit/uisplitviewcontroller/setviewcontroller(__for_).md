---
title: 'setViewController(_:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisplitviewcontroller/setviewcontroller(_:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontroller/setviewcontroller(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontroller/setviewcontroller%28_%3Afor%3A%29.json'
content_hash: 'sha256:be72780d78ebd4e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewController](../uisplitviewcontroller.md)

# setViewController(_:for:)

<sub>Instance Method</sub>

Presents the provided view controller in the specified column of the split view interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setViewController(_ vc: UIViewController?, for column: UISplitViewController.Column)
```

## Parameters

- `vc` — The child view controller to associate with the provided column of the split view interface.

- `column` — The corresponding column of the split view interface. See [Column](column.md) for values.

## Discussion

This method doesn’t apply to classic split view controllers with a [style](style-swift.property.md) of [UISplitViewControllerStyleUnspecified](style-swift.enum/unspecified.md). For a classic split view controller, instead use the [viewControllers](viewcontrollers.md) property to assign the primary and secondary view controllers that you want to display initially. After the split view controller is onscreen, set the child view controllers using the [- showViewController:sender:](<show(__sender_).md>) and [- showDetailViewController:sender:](<showdetailviewcontroller(__sender_).md>) methods.

For a column-style split view controller, you use this method to assign child view controllers to a specific column of the split view interface. In general, unless your view controller is a navigation controller, the split view creates its own navigation controller to wrap the view controller you assign to the primary, supplementary, and secondary columns. There are some exceptions to this behavior:

- For the primary column, if you assign a [UIViewController](../uiviewcontroller.md) (or custom subclass) whose first child view controller is a [UINavigationController](../uinavigationcontroller.md), the split view controller uses that navigation controller as the primary view controller for collapsing the interface and for placing the button to change the display mode.
- For the secondary column, if you assign a [UIViewController](../uiviewcontroller.md) (or custom subclass) whose first child view controller is a [UINavigationController](../uinavigationcontroller.md), the split view controller uses that navigation controller as the secondary view controller for placing the button to change the display mode.

| Column | Assigned As-Is |
|---|---|
| Primary | [UINavigationController](../uinavigationcontroller.md) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [UIViewController](../uiviewcontroller.md) with [UINavigationController](../uinavigationcontroller.md) as its first child |
| Supplementary | [UINavigationController](../uinavigationcontroller.md) |
| Secondary | [UITabBarController](../uitabbarcontroller.md) with [UINavigationController](../uinavigationcontroller.md)s in its tabs ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [UINavigationController](../uinavigationcontroller.md) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [UIViewController](../uiviewcontroller.md) with [UINavigationController](../uinavigationcontroller.md) as its first child |
| Compact | Any [UIViewController](../uiviewcontroller.md) |

You can’t assign a [UITabBarController](../uitabbarcontroller.md) to the primary or supplementary columns.

## See Also

### Managing the child view controllers

- [Column](column.md) — Constants that describe the columns within the split view interface.
- [- viewControllerForColumn:](<viewcontroller(for_).md>) — Returns the view controller associated with the specified column of the split view interface.
- [viewControllers](viewcontrollers.md) — The array of view controllers the split view controller manages.

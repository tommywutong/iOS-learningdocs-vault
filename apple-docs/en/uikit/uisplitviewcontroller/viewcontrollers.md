---
title: viewControllers
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisplitviewcontroller/viewcontrollers
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontroller/viewcontrollers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontroller/viewcontrollers.json'
content_hash: 'sha256:de7c2983b9dfff6e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewController](../uisplitviewcontroller.md)

# viewControllers

<sub>Instance Property</sub>

The array of view controllers the split view controller manages.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var viewControllers: [UIViewController] { get set }
```

## Discussion

When the split view interface is expanded, this property contains two or three view controllers depending on the interface’s [style](style-swift.property.md). The first view controller in the array is the primary view controller. It’s followed by the supplementary (if present) and then the secondary view controller.

When the split view interface is collapsed, this property contains only one view controller. If a view controller is set for the [UISplitViewControllerColumnCompact](column/compact.md) column, this property contains that view controller. Otherwise, this property contains the primary view controller.

In a column-style split view controller, it’s recommended that you set the child view controllers using the [- setViewController:forColumn:](<setviewcontroller(__for_).md>) method and get them using the [- viewControllerForColumn:](<viewcontroller(for_).md>) method.

In a classic split view controller, you can use this property to assign the primary and secondary view controllers that you want to display initially. After the split view controller is onscreen, you can use this property to get the view controllers in the split view interface. After you assign the initial view controllers, it’s better to set the child view controllers using the [- showViewController:sender:](<show(__sender_).md>) and [- showDetailViewController:sender:](<showdetailviewcontroller(__sender_).md>) methods. Although you can still change the view controllers in this property directly, you should do so only if you manually manage your app’s view controller transitions.

## See Also

### Related Documentation

- [- showDetailViewController:sender:](<showdetailviewcontroller(__sender_).md>) — Presents the specified view controller as the secondary view controller of the split view interface.
- [- showViewController:sender:](<show(__sender_).md>) — Presents the specified view controller as the primary view controller in the split view interface.

### Managing the child view controllers

- [Column](column.md) — Constants that describe the columns within the split view interface.
- [- setViewController:forColumn:](<setviewcontroller(__for_).md>) — Presents the provided view controller in the specified column of the split view interface.
- [- viewControllerForColumn:](<viewcontroller(for_).md>) — Returns the view controller associated with the specified column of the split view interface.

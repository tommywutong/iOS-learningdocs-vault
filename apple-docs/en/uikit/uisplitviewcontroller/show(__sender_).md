---
title: 'show(_:sender:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisplitviewcontroller/show(_:sender:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontroller/show(_:sender:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontroller/show%28_%3Asender%3A%29.json'
content_hash: 'sha256:81cc367039aa7e78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewController](../uisplitviewcontroller.md)

# show(_:sender:)

<sub>Instance Method</sub>

Presents the specified view controller as the primary view controller in the split view interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func show(_ vc: UIViewController, sender: Any?)
```

## Parameters

- `vc` — The view controller to display in the primary location of the split view interface.

- `sender` — The object that made the request to show the view controller.

## Discussion

Whenever possible, use this method (instead of modifying the contents of the [viewControllers](viewcontrollers.md) property directly) to replace the primary view controller of your split view interface. This method displays the specified view controller in a way that’s optimal for the current size class in effect.

Typically, you call this method from an action method when you want to replace the primary view controller with the one specified in `vc`. This method calls the split view controller delegate’s [- splitViewController:showViewController:sender:](<../uisplitviewcontrollerdelegate/splitviewcontroller(__show_sender_).md>) method to give the delegate an opportunity to show the view controller. If the delegate does not show the view controller, the split view controller shows it using the following heuristics:

- In a horizontally regular environment, the split view controller installs `vc` as the primary view controller unless `vc` is already a child of the primary view controller. In that case, it installs `vc` as the secondary view controller.
- In a horizontally compact environment, the split view controller presents `vc` modally.

## See Also

### Displaying the child view controllers

- [- showColumn:](<show(__).md>) — Presents the view controller in the specified column of the split view interface.
- [- hideColumn:](<hide(__).md>) — Dismisses the view controller in the specified column of the split view interface.
- [- isShowingColumn:](<isshowing(__).md>) — A Boolean value that indicates whether the split view interface is showing the specified column.
- [- showDetailViewController:sender:](<showdetailviewcontroller(__sender_).md>) — Presents the specified view controller as the secondary view controller of the split view interface.

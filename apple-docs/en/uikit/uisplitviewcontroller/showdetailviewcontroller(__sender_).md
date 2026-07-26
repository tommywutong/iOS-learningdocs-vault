---
title: 'showDetailViewController(_:sender:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisplitviewcontroller/showdetailviewcontroller(_:sender:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontroller/showdetailviewcontroller(_:sender:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontroller/showdetailviewcontroller%28_%3Asender%3A%29.json'
content_hash: 'sha256:abfd585493c059d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewController](../uisplitviewcontroller.md)

# showDetailViewController(_:sender:)

<sub>Instance Method</sub>

Presents the specified view controller as the secondary view controller of the split view interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func showDetailViewController(_ vc: UIViewController, sender: Any?)
```

## Parameters

- `vc` — The view controller to display in the secondary location of the split view interface. If you specify `nil` for this parameter or if this view controller is the same as the one it would replace, this method does nothing.

- `sender` — The view or view controller that made the request.

## Discussion

Whenever possible, use this method (instead of modifying the contents of the [viewControllers](viewcontrollers.md) property directly) to replace the secondary view controller of your split view interface. This method displays the specified view controller in a way that’s optimal for the current size class in effect. It also takes advantage of existing navigation controller behaviors whenever possible to minimize changes to the split view interface.

This method calls the delegate’s [- splitViewController:showDetailViewController:sender:](<../uisplitviewcontrollerdelegate/splitviewcontroller(__showdetail_sender_).md>) method to give the delegate an opportunity to show the view controller. If the delegate doesn’t show the view controller, the split view controller forwards the message to the view controller being replaced. For example, a navigation controller responds by pushing `vc` onto its navigation stack. If no other object shows the view controller, the split view controller shows it using the following heuristics:

- In a horizontally regular environment, the split view controller installs `vc` as the secondary view controller.
- In a horizontally compact environment, the split view controller presents `vc` modally.

All view controllers implement this method. If they do not show the view controller themselves, they forward the message to the parent split view controller (if any) and let it show the view controller. As a result, a child view controller can call this method on itself to achieve the same results as calling this method on the split view controller object.

## See Also

### Displaying the child view controllers

- [- showColumn:](<show(__).md>) — Presents the view controller in the specified column of the split view interface.
- [- hideColumn:](<hide(__).md>) — Dismisses the view controller in the specified column of the split view interface.
- [- isShowingColumn:](<isshowing(__).md>) — A Boolean value that indicates whether the split view interface is showing the specified column.
- [- showViewController:sender:](<show(__sender_).md>) — Presents the specified view controller as the primary view controller in the split view interface.

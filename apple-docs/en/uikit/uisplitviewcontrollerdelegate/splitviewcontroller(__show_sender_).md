---
title: 'splitViewController(_:show:sender:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:show:sender:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:show:sender:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller%28_%3Ashow%3Asender%3A%29.json'
content_hash: 'sha256:1bffb4fdeb67c7c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewControllerDelegate](../uisplitviewcontrollerdelegate.md)

# splitViewController(_:show:sender:)

<sub>Instance Method</sub>

Asks the delegate if it will do the work of displaying a view controller in the primary position of the split view interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func splitViewController(_ splitViewController: UISplitViewController, show vc: UIViewController, sender: Any?) -> Bool
```

## Parameters

- `splitViewController` — The split view controller whose primary view controller is being updated.

- `vc` — The view controller being displayed in the primary position.

- `sender` — The object that made the request.

## Return Value

[true](../../swift/true.md) if you handled the presentation of the view controller, or [false](../../swift/false.md) if you want the split view controller to do it.

## Discussion

This delegate method only applies to classic split view interfaces. For more information, see [Split view styles](../uisplitviewcontroller.md#Split-view-styles).

When its [- showViewController:sender:](<../uisplitviewcontroller/show(__sender_).md>) method is called, the split view controller calls this method to see if your delegate will handle the presentation of the specified view controller. If you implement this method and your implementation returns [true](../../swift/true.md), you are responsible for presenting the specified view controller in the primary position of the split view interface. The split view controller does nothing more to try to show the view controller.

If you don’t implement this method or if your implementation returns [false](../../swift/false.md), the split view controller presents the view controller.

## See Also

### Overriding the presentation behavior

- [- splitViewController:showDetailViewController:sender:](<splitviewcontroller(__showdetail_sender_).md>) — Asks the delegate if it will do the work of displaying a view controller in the secondary position of the split view interface.

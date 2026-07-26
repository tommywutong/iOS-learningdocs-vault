---
title: 'viewWillAppear(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontroller/viewwillappear(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/viewwillappear(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/viewwillappear%28_%3A%29.json'
content_hash: 'sha256:ccb0887fbff859d7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# viewWillAppear(_:)

<sub>Instance Method</sub>

Notifies the view controller that its view is about to be added to a view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func viewWillAppear(_ animated: Bool)
```

## Parameters

- `animated` — If [true](../../swift/true.md), the view is being added to the window using an animation.

## Discussion

This method is called before the view controller’s view is about to be added to a view hierarchy and before any animations are configured for showing the view. You can override this method to perform custom tasks associated with displaying the view. For example, you might use this method to change the orientation or style of the status bar to coordinate with the orientation or style of the view being presented. If you override this method, you must call `super` at some point in your implementation.

For more information about the how views are added to view hierarchies by a view controller, and the sequence of messages that occur, see [Supporting Accessibility](https://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/SupportingAccessibility.html#//apple_ref/doc/uid/TP40007457-CH12).

> [!note] Note
> If a view controller is presented by a view controller inside of a popover, this method is not invoked on the presenting view controller after the presented controller is dismissed.

## See Also

### Responding to view-related events

- [- viewIsAppearing:](<viewisappearing(__).md>) — Notifies the view controller that the system is adding the view controller’s view to a view hierarchy.
- [- viewDidAppear:](<viewdidappear(__).md>) — Notifies the view controller that its view was added to a view hierarchy.
- [- viewWillDisappear:](<viewwilldisappear(__).md>) — Notifies the view controller that its view is about to be removed from a view hierarchy.
- [- viewDidDisappear:](<viewdiddisappear(__).md>) — Notifies the view controller that its view was removed from a view hierarchy.
- [beingDismissed](isbeingdismissed.md) — A Boolean value indicating whether the view controller is in the process of being dismissed by one of its ancestors.
- [beingPresented](isbeingpresented.md) — A Boolean value indicating whether the view controller in the process of being presented by one of its ancestors.
- [movingFromParentViewController](ismovingfromparent.md) — A Boolean value indicating whether the view controller is moving from a parent view controller.
- [movingToParentViewController](ismovingtoparent.md) — A Boolean value indicating whether the view controller is moving to a parent view controller.

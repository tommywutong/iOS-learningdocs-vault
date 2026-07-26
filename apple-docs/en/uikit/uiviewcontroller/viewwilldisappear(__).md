---
title: 'viewWillDisappear(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontroller/viewwilldisappear(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/viewwilldisappear(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/viewwilldisappear%28_%3A%29.json'
content_hash: 'sha256:452de84e2fe99b70'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# viewWillDisappear(_:)

<sub>Instance Method</sub>

Notifies the view controller that its view is about to be removed from a view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func viewWillDisappear(_ animated: Bool)
```

## Parameters

- `animated` — If [true](../../swift/true.md), the disappearance of the view is being animated.

## Discussion

This method is called in response to a view being removed from a view hierarchy. This method is called before the view is actually removed and before any animations are configured.

Subclasses can override this method and use it to commit editing changes, resign the first responder status of the view, or perform other relevant tasks. For example, you might use this method to revert changes to the orientation or style of the status bar that were made in the [- viewDidAppear:](<viewdidappear(__).md>) method when the view was first presented. If you override this method, you must call `super` at some point in your implementation.

## See Also

### Responding to view-related events

- [- viewWillAppear:](<viewwillappear(__).md>) — Notifies the view controller that its view is about to be added to a view hierarchy.
- [- viewIsAppearing:](<viewisappearing(__).md>) — Notifies the view controller that the system is adding the view controller’s view to a view hierarchy.
- [- viewDidAppear:](<viewdidappear(__).md>) — Notifies the view controller that its view was added to a view hierarchy.
- [- viewDidDisappear:](<viewdiddisappear(__).md>) — Notifies the view controller that its view was removed from a view hierarchy.
- [beingDismissed](isbeingdismissed.md) — A Boolean value indicating whether the view controller is in the process of being dismissed by one of its ancestors.
- [beingPresented](isbeingpresented.md) — A Boolean value indicating whether the view controller in the process of being presented by one of its ancestors.
- [movingFromParentViewController](ismovingfromparent.md) — A Boolean value indicating whether the view controller is moving from a parent view controller.
- [movingToParentViewController](ismovingtoparent.md) — A Boolean value indicating whether the view controller is moving to a parent view controller.

---
title: 'viewDidDisappear(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontroller/viewdiddisappear(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/viewdiddisappear(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/viewdiddisappear%28_%3A%29.json'
content_hash: 'sha256:339c5ea7ca5594a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# viewDidDisappear(_:)

<sub>Instance Method</sub>

Notifies the view controller that its view was removed from a view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func viewDidDisappear(_ animated: Bool)
```

## Parameters

- `animated` — If [true](../../swift/true.md), the disappearance of the view was animated.

## Discussion

You can override this method to perform additional tasks associated with dismissing or hiding the view. If you override this method, you must call `super` at some point in your implementation.

## See Also

### Responding to view-related events

- [- viewWillAppear:](<viewwillappear(__).md>) — Notifies the view controller that its view is about to be added to a view hierarchy.
- [- viewIsAppearing:](<viewisappearing(__).md>) — Notifies the view controller that the system is adding the view controller’s view to a view hierarchy.
- [- viewDidAppear:](<viewdidappear(__).md>) — Notifies the view controller that its view was added to a view hierarchy.
- [- viewWillDisappear:](<viewwilldisappear(__).md>) — Notifies the view controller that its view is about to be removed from a view hierarchy.
- [beingDismissed](isbeingdismissed.md) — A Boolean value indicating whether the view controller is in the process of being dismissed by one of its ancestors.
- [beingPresented](isbeingpresented.md) — A Boolean value indicating whether the view controller in the process of being presented by one of its ancestors.
- [movingFromParentViewController](ismovingfromparent.md) — A Boolean value indicating whether the view controller is moving from a parent view controller.
- [movingToParentViewController](ismovingtoparent.md) — A Boolean value indicating whether the view controller is moving to a parent view controller.

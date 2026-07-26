---
title: isMovingFromParent
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/ismovingfromparent
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/ismovingfromparent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/ismovingfromparent.json'
content_hash: 'sha256:3f89d0f0b8eadd0d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# isMovingFromParent

<sub>Instance Property</sub>

A Boolean value indicating whether the view controller is moving from a parent view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isMovingFromParent: Bool { get }
```

## See Also

### Responding to view-related events

- [- viewWillAppear:](<viewwillappear(__).md>) — Notifies the view controller that its view is about to be added to a view hierarchy.
- [- viewIsAppearing:](<viewisappearing(__).md>) — Notifies the view controller that the system is adding the view controller’s view to a view hierarchy.
- [- viewDidAppear:](<viewdidappear(__).md>) — Notifies the view controller that its view was added to a view hierarchy.
- [- viewWillDisappear:](<viewwilldisappear(__).md>) — Notifies the view controller that its view is about to be removed from a view hierarchy.
- [- viewDidDisappear:](<viewdiddisappear(__).md>) — Notifies the view controller that its view was removed from a view hierarchy.
- [beingDismissed](isbeingdismissed.md) — A Boolean value indicating whether the view controller is in the process of being dismissed by one of its ancestors.
- [beingPresented](isbeingpresented.md) — A Boolean value indicating whether the view controller in the process of being presented by one of its ancestors.
- [movingToParentViewController](ismovingtoparent.md) — A Boolean value indicating whether the view controller is moving to a parent view controller.

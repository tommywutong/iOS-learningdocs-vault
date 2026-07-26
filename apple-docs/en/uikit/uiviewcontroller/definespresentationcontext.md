---
title: definesPresentationContext
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/definespresentationcontext
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/definespresentationcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/definespresentationcontext.json'
content_hash: 'sha256:b95e5199637564d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# definesPresentationContext

<sub>Instance Property</sub>

A Boolean value that indicates whether this view controller’s view is covered when the view controller or one of its descendants presents a view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var definesPresentationContext: Bool { get set }
```

## Discussion

When using the [UIModalPresentationCurrentContext](../uimodalpresentationstyle/currentcontext.md) or [UIModalPresentationOverCurrentContext](../uimodalpresentationstyle/overcurrentcontext.md) style to present a view controller, this property controls which existing view controller in your view controller hierarchy is actually covered by the new content. When a context-based presentation occurs, UIKit starts at the presenting view controller and walks up the view controller hierarchy. If it finds a view controller whose value for this property is [true](../../swift/true.md), it asks that view controller to present the new view controller. If no view controller defines the presentation context, UIKit asks the window’s root view controller to handle the presentation.

The default value for this property is [false](../../swift/false.md). Some system-provided view controllers, such as [UINavigationController](../uinavigationcontroller.md), change the default value to [true](../../swift/true.md).

## See Also

### Presenting a view controller

- [- showViewController:sender:](<show(__sender_).md>) — Presents a view controller in a primary context.
- [- showDetailViewController:sender:](<showdetailviewcontroller(__sender_).md>) — Presents a view controller in a secondary (or detail) context.
- [ShowDetailTargetDidChangeMessage](showdetailtargetdidchangemessage.md)
- [- presentViewController:animated:completion:](<present(__animated_completion_).md>) — Presents a view controller modally.
- [- dismissViewControllerAnimated:completion:](<dismiss(animated_completion_).md>) — Dismisses the view controller that was presented modally by the view controller.
- [modalPresentationStyle](modalpresentationstyle.md) — The presentation style for modal view controllers.
- [UIModalPresentationStyle](../uimodalpresentationstyle.md) — Modal presentation styles available when presenting view controllers.
- [modalTransitionStyle](modaltransitionstyle.md) — The transition style to use when presenting the view controller.
- [UIModalTransitionStyle](../uimodaltransitionstyle.md) — Transition styles available when presenting view controllers.
- [modalInPresentation](ismodalinpresentation.md) — A Boolean value indicating whether the view controller enforces a modal behavior.
- [providesPresentationContextTransitionStyle](providespresentationcontexttransitionstyle.md) — A Boolean value that indicates whether the view controller specifies the transition style for view controllers it presents.
- [disablesAutomaticKeyboardDismissal](disablesautomatickeyboarddismissal.md) — Returns a Boolean indicating whether the current input view is dismissed automatically when changing controls.
- [UIViewControllerShowDetailTargetDidChangeNotification](showdetailtargetdidchangenotification.md) — Posted when a split view controller is expanded or collapsed.

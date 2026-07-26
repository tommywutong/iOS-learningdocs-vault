---
title: isModalInPresentation
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/ismodalinpresentation
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/ismodalinpresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/ismodalinpresentation.json'
content_hash: 'sha256:3bf70588dbcae1fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# isModalInPresentation

<sub>Instance Property</sub>

A Boolean value indicating whether the view controller enforces a modal behavior.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isModalInPresentation: Bool { get set }
```

## Discussion

The default value of this property is [false](../../swift/false.md). When you set it to [true](../../swift/true.md), UIKit ignores events outside the view controller’s bounds and prevents the interactive dismissal of the view controller while it is onscreen.

## See Also

### Related Documentation

- [Disabling the pull-down gesture for a sheet](../disabling-the-pull-down-gesture-for-a-sheet.md) — Ensure a positive user experience when presenting a view controller as a sheet.

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
- [definesPresentationContext](definespresentationcontext.md) — A Boolean value that indicates whether this view controller’s view is covered when the view controller or one of its descendants presents a view controller.
- [providesPresentationContextTransitionStyle](providespresentationcontexttransitionstyle.md) — A Boolean value that indicates whether the view controller specifies the transition style for view controllers it presents.
- [disablesAutomaticKeyboardDismissal](disablesautomatickeyboarddismissal.md) — Returns a Boolean indicating whether the current input view is dismissed automatically when changing controls.
- [UIViewControllerShowDetailTargetDidChangeNotification](showdetailtargetdidchangenotification.md) — Posted when a split view controller is expanded or collapsed.

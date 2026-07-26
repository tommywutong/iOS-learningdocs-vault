---
title: showDetailTargetDidChangeNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/showdetailtargetdidchangenotification
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/showdetailtargetdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/showdetailtargetdidchangenotification.json'
content_hash: 'sha256:b748029e7d9860ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# showDetailTargetDidChangeNotification

<sub>Type Property</sub>

Posted when a split view controller is expanded or collapsed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated class let showDetailTargetDidChangeNotification: NSNotification.Name
```

## Discussion

When a view controller is using [- showViewController:sender:](<show(__sender_).md>) or [- showDetailViewController:sender:](<showdetailviewcontroller(__sender_).md>), it may need to know when a split view controller higher in the view hierarchy has changed. This notification is sent when a split view controller expands or collapses. The object of this notification is the view controller that caused the change.

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
- [definesPresentationContext](definespresentationcontext.md) — A Boolean value that indicates whether this view controller’s view is covered when the view controller or one of its descendants presents a view controller.
- [providesPresentationContextTransitionStyle](providespresentationcontexttransitionstyle.md) — A Boolean value that indicates whether the view controller specifies the transition style for view controllers it presents.
- [disablesAutomaticKeyboardDismissal](disablesautomatickeyboarddismissal.md) — Returns a Boolean indicating whether the current input view is dismissed automatically when changing controls.

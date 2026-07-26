---
title: disablesAutomaticKeyboardDismissal
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/disablesautomatickeyboarddismissal
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/disablesautomatickeyboarddismissal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/disablesautomatickeyboarddismissal.json'
content_hash: 'sha256:4fe35609cc17a1b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# disablesAutomaticKeyboardDismissal

<sub>Instance Property</sub>

Returns a Boolean indicating whether the current input view is dismissed automatically when changing controls.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var disablesAutomaticKeyboardDismissal: Bool { get }
```

## Return Value

[true](../../swift/true.md) to prevent the dismissal of the input view or [false](../../swift/false.md) if the input view may be dismissed.

## Discussion

Override this method in a subclass to allow or disallow the dismissal of the current input view (usually the system keyboard) when changing from a control that wants the input view to one that does not. Under normal circumstances, when the user taps a control that requires an input view, the system automatically displays that view. Tapping in a control that does not want an input view subsequently causes the current input view to be dismissed but may not in all cases. You can override this method in those outstanding cases to allow the input view to be dismissed or use this method to prevent the view from being dismissed in other cases.

The default implementation of this method returns [true](../../swift/true.md) when the modal presentation style of the view controller is set to [UIModalPresentationFormSheet](../uimodalpresentationstyle/formsheet.md) and returns [false](../../swift/false.md) for other presentation styles. Thus, the system normally does not allow the keyboard to be dismissed for modal forms.

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
- [UIViewControllerShowDetailTargetDidChangeNotification](showdetailtargetdidchangenotification.md) — Posted when a split view controller is expanded or collapsed.

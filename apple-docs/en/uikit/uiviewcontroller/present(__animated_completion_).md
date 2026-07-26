---
title: 'present(_:animated:completion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontroller/present(_:animated:completion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/present(_:animated:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/present%28_%3Aanimated%3Acompletion%3A%29.json'
content_hash: 'sha256:e3ad407375d496fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# present(_:animated:completion:)

<sub>Instance Method</sub>

Presents a view controller modally.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func present(_ viewControllerToPresent: UIViewController, animated flag: Bool, completion: (() -> Void)? = nil)
```

## Parameters

- `viewControllerToPresent` — The view controller to display over the current view controller’s content.

- `flag` — Pass [true](../../swift/true.md) to animate the presentation; otherwise, pass [false](../../swift/false.md).

- `completion` — The block to execute after the presentation finishes. This block has no return value and takes no parameters. You may specify `nil` for this parameter.

## Discussion

In a horizontally regular environment, the view controller is presented in the style specified by the [modalPresentationStyle](modalpresentationstyle.md) property. In a horizontally compact environment, the view controller is presented full screen by default. If you associate an adaptive delegate with the presentation controller associated with the object in `viewControllerToPresent`, you can modify the presentation style dynamically.

The object on which you call this method may not always be the one that handles the presentation. Each presentation style has different rules governing its behavior. For example, a full-screen presentation must be made by a view controller that itself covers the entire screen. If the current view controller is unable to fulfill a request, it forwards the request up the view controller hierarchy to its nearest parent, which can then handle or forward the request.

Before displaying the view controller, this method resizes the presented view controller’s view based on the presentation style. For most presentation styles, the resulting view is then animated onscreen using the transition style in the [modalTransitionStyle](modaltransitionstyle.md) property of the presented view controller. For custom presentations, the view is animated onscreen using the presented view controller’s transitioning delegate. For current context presentations, the view may be animated onscreen using the current view controller’s transition style.

The completion handler is called after the [- viewDidAppear:](<viewdidappear(__).md>) method is called on the presented view controller.

## See Also

### Related Documentation

- [presentedViewController](presentedviewcontroller.md) — The view controller that is presented by this view controller, or one of its ancestors in the view controller hierarchy.
- [presentingViewController](presentingviewcontroller.md) — The view controller that presented this view controller.

### Presenting a view controller

- [- showViewController:sender:](<show(__sender_).md>) — Presents a view controller in a primary context.
- [- showDetailViewController:sender:](<showdetailviewcontroller(__sender_).md>) — Presents a view controller in a secondary (or detail) context.
- [ShowDetailTargetDidChangeMessage](showdetailtargetdidchangemessage.md)
- [- dismissViewControllerAnimated:completion:](<dismiss(animated_completion_).md>) — Dismisses the view controller that was presented modally by the view controller.
- [modalPresentationStyle](modalpresentationstyle.md) — The presentation style for modal view controllers.
- [UIModalPresentationStyle](../uimodalpresentationstyle.md) — Modal presentation styles available when presenting view controllers.
- [modalTransitionStyle](modaltransitionstyle.md) — The transition style to use when presenting the view controller.
- [UIModalTransitionStyle](../uimodaltransitionstyle.md) — Transition styles available when presenting view controllers.
- [modalInPresentation](ismodalinpresentation.md) — A Boolean value indicating whether the view controller enforces a modal behavior.
- [definesPresentationContext](definespresentationcontext.md) — A Boolean value that indicates whether this view controller’s view is covered when the view controller or one of its descendants presents a view controller.
- [providesPresentationContextTransitionStyle](providespresentationcontexttransitionstyle.md) — A Boolean value that indicates whether the view controller specifies the transition style for view controllers it presents.
- [disablesAutomaticKeyboardDismissal](disablesautomatickeyboarddismissal.md) — Returns a Boolean indicating whether the current input view is dismissed automatically when changing controls.
- [UIViewControllerShowDetailTargetDidChangeNotification](showdetailtargetdidchangenotification.md) — Posted when a split view controller is expanded or collapsed.

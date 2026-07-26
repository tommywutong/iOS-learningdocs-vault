---
title: 'show(_:sender:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontroller/show(_:sender:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/show(_:sender:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/show%28_%3Asender%3A%29.json'
content_hash: 'sha256:09de0998a961b947'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# show(_:sender:)

<sub>Instance Method</sub>

Presents a view controller in a primary context.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func show(_ vc: UIViewController, sender: Any?)
```

## Parameters

- `vc` — The view controller to display.

- `sender` — The object that initiated the request.

## Discussion

You use this method to decouple the need to display a view controller from the process of actually presenting that view controller onscreen. Using this method, a view controller does not need to know whether it is embedded inside a navigation controller or split-view controller. It calls the same method for both. The [UISplitViewController](../uisplitviewcontroller.md) and [UINavigationController](../uinavigationcontroller.md) classes override this method and handle the presentation according to their design. For example, a navigation controller overrides this method and uses it to push `vc` onto its navigation stack.

The default implementation of this method calls the [- targetViewControllerForAction:sender:](<targetviewcontroller(foraction_sender_).md>) method to locate an object in the view controller hierarchy that overrides this method. It then calls the method on that target object, which displays the view controller in an appropriate way. If the [- targetViewControllerForAction:sender:](<targetviewcontroller(foraction_sender_).md>) method returns `nil`, this method uses the window’s root view controller to present `vc` modally.

You can override this method in custom view controllers to display `vc` yourself. Use this method to display `vc` in a primary context. For example, a container view controller might use this method to replace its primary child. Your implementation should adapt its behavior for both regular and compact environments.

## See Also

### Presenting a view controller

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
- [UIViewControllerShowDetailTargetDidChangeNotification](showdetailtargetdidchangenotification.md) — Posted when a split view controller is expanded or collapsed.

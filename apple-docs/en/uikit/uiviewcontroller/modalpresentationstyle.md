---
title: modalPresentationStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/modalpresentationstyle
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/modalpresentationstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/modalpresentationstyle.json'
content_hash: 'sha256:d2e0986084c7d9db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# modalPresentationStyle

<sub>Instance Property</sub>

The presentation style for modal view controllers.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var modalPresentationStyle: UIModalPresentationStyle { get set }
```

## Discussion

Presentation style defines how the system presents a modal view controller. The system uses this value only in regular-width size classes. In compact-width size classes, some styles take on the behavior of other styles. You can influence this behavior by implementing the [- adaptivePresentationStyleForPresentationController:traitCollection:](<../uiadaptivepresentationcontrollerdelegate/adaptivepresentationstyle(for_traitcollection_).md>) method.

Presentation style also impacts the content size of a modal view controller. For example, [UIModalPresentationPageSheet](../uimodalpresentationstyle/pagesheet.md) uses an explicit size that the system provides. By contrast, [UIModalPresentationFormSheet](../uimodalpresentationstyle/formsheet.md) uses the view controller’s [preferredContentSize](preferredcontentsize.md) property, which you can set.

The default value is [UIModalPresentationAutomatic](../uimodalpresentationstyle/automatic.md). For a list of presentation styles and their compatibility with the various transition styles, see [UIModalPresentationStyle](../uimodalpresentationstyle.md).

## See Also

### Presenting a view controller

- [- showViewController:sender:](<show(__sender_).md>) — Presents a view controller in a primary context.
- [- showDetailViewController:sender:](<showdetailviewcontroller(__sender_).md>) — Presents a view controller in a secondary (or detail) context.
- [ShowDetailTargetDidChangeMessage](showdetailtargetdidchangemessage.md)
- [- presentViewController:animated:completion:](<present(__animated_completion_).md>) — Presents a view controller modally.
- [- dismissViewControllerAnimated:completion:](<dismiss(animated_completion_).md>) — Dismisses the view controller that was presented modally by the view controller.
- [UIModalPresentationStyle](../uimodalpresentationstyle.md) — Modal presentation styles available when presenting view controllers.
- [modalTransitionStyle](modaltransitionstyle.md) — The transition style to use when presenting the view controller.
- [UIModalTransitionStyle](../uimodaltransitionstyle.md) — Transition styles available when presenting view controllers.
- [modalInPresentation](ismodalinpresentation.md) — A Boolean value indicating whether the view controller enforces a modal behavior.
- [definesPresentationContext](definespresentationcontext.md) — A Boolean value that indicates whether this view controller’s view is covered when the view controller or one of its descendants presents a view controller.
- [providesPresentationContextTransitionStyle](providespresentationcontexttransitionstyle.md) — A Boolean value that indicates whether the view controller specifies the transition style for view controllers it presents.
- [disablesAutomaticKeyboardDismissal](disablesautomatickeyboarddismissal.md) — Returns a Boolean indicating whether the current input view is dismissed automatically when changing controls.
- [UIViewControllerShowDetailTargetDidChangeNotification](showdetailtargetdidchangenotification.md) — Posted when a split view controller is expanded or collapsed.

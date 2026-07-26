---
title: UIModalPresentationStyle
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimodalpresentationstyle
source_url: 'https://developer.apple.com/documentation/uikit/uimodalpresentationstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimodalpresentationstyle.json'
content_hash: 'sha256:868193789c43fdab'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIModalPresentationStyle

<sub>Enumeration</sub>

Modal presentation styles available when presenting view controllers.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum UIModalPresentationStyle
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Presentations

- [UIModalPresentationAutomatic](uimodalpresentationstyle/automatic.md) — The default presentation style chosen by the system.
- [UIModalPresentationNone](uimodalpresentationstyle/none.md) — A presentation style that indicates no adaptations should be made.
- [UIModalPresentationFullScreen](uimodalpresentationstyle/fullscreen.md) — A presentation style in which the presented view covers the screen.
- [UIModalPresentationPageSheet](uimodalpresentationstyle/pagesheet.md) — A presentation style that partially covers the underlying content.
- [UIModalPresentationFormSheet](uimodalpresentationstyle/formsheet.md) — A presentation style that displays the content centered in the screen.
- [UIModalPresentationCurrentContext](uimodalpresentationstyle/currentcontext.md) — A presentation style where the content is displayed over another view controller’s content.
- [UIModalPresentationCustom](uimodalpresentationstyle/custom.md) — A custom view presentation style that is managed by a custom presentation controller and one or more custom animator objects.
- [UIModalPresentationOverFullScreen](uimodalpresentationstyle/overfullscreen.md) — A view presentation style in which the presented view covers the screen.
- [UIModalPresentationOverCurrentContext](uimodalpresentationstyle/overcurrentcontext.md) — A presentation style where the content is displayed over another view controller’s content.
- [UIModalPresentationPopover](uimodalpresentationstyle/popover.md) — A presentation style where the content is displayed in a popover view.
- [UIModalPresentationBlurOverFullScreen](uimodalpresentationstyle/bluroverfullscreen.md) — A presentation style that blurs the underlying content before displaying new content in a full-screen presentation.

### Initializers

- [init(rawValue:)](<uimodalpresentationstyle/init(rawvalue_).md>)

## See Also

### Presenting a view controller

- [- showViewController:sender:](<uiviewcontroller/show(__sender_).md>) — Presents a view controller in a primary context.
- [- showDetailViewController:sender:](<uiviewcontroller/showdetailviewcontroller(__sender_).md>) — Presents a view controller in a secondary (or detail) context.
- [ShowDetailTargetDidChangeMessage](uiviewcontroller/showdetailtargetdidchangemessage.md)
- [- presentViewController:animated:completion:](<uiviewcontroller/present(__animated_completion_).md>) — Presents a view controller modally.
- [- dismissViewControllerAnimated:completion:](<uiviewcontroller/dismiss(animated_completion_).md>) — Dismisses the view controller that was presented modally by the view controller.
- [modalPresentationStyle](uiviewcontroller/modalpresentationstyle.md) — The presentation style for modal view controllers.
- [modalTransitionStyle](uiviewcontroller/modaltransitionstyle.md) — The transition style to use when presenting the view controller.
- [UIModalTransitionStyle](uimodaltransitionstyle.md) — Transition styles available when presenting view controllers.
- [modalInPresentation](uiviewcontroller/ismodalinpresentation.md) — A Boolean value indicating whether the view controller enforces a modal behavior.
- [definesPresentationContext](uiviewcontroller/definespresentationcontext.md) — A Boolean value that indicates whether this view controller’s view is covered when the view controller or one of its descendants presents a view controller.
- [providesPresentationContextTransitionStyle](uiviewcontroller/providespresentationcontexttransitionstyle.md) — A Boolean value that indicates whether the view controller specifies the transition style for view controllers it presents.
- [disablesAutomaticKeyboardDismissal](uiviewcontroller/disablesautomatickeyboarddismissal.md) — Returns a Boolean indicating whether the current input view is dismissed automatically when changing controls.
- [UIViewControllerShowDetailTargetDidChangeNotification](uiviewcontroller/showdetailtargetdidchangenotification.md) — Posted when a split view controller is expanded or collapsed.

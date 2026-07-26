---
title: UIModalTransitionStyle
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimodaltransitionstyle
source_url: 'https://developer.apple.com/documentation/uikit/uimodaltransitionstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimodaltransitionstyle.json'
content_hash: 'sha256:73c73c1ab0c4cda1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIModalTransitionStyle

<sub>Enumeration</sub>

Transition styles available when presenting view controllers.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum UIModalTransitionStyle
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [UIModalTransitionStyleCoverVertical](uimodaltransitionstyle/coververtical.md)
- [UIModalTransitionStyleFlipHorizontal](uimodaltransitionstyle/fliphorizontal.md)
- [UIModalTransitionStyleCrossDissolve](uimodaltransitionstyle/crossdissolve.md)
- [UIModalTransitionStylePartialCurl](uimodaltransitionstyle/partialcurl.md)

### Initializers

- [init(rawValue:)](<uimodaltransitionstyle/init(rawvalue_).md>)

## See Also

### Presenting a view controller

- [- showViewController:sender:](<uiviewcontroller/show(__sender_).md>) — Presents a view controller in a primary context.
- [- showDetailViewController:sender:](<uiviewcontroller/showdetailviewcontroller(__sender_).md>) — Presents a view controller in a secondary (or detail) context.
- [ShowDetailTargetDidChangeMessage](uiviewcontroller/showdetailtargetdidchangemessage.md)
- [- presentViewController:animated:completion:](<uiviewcontroller/present(__animated_completion_).md>) — Presents a view controller modally.
- [- dismissViewControllerAnimated:completion:](<uiviewcontroller/dismiss(animated_completion_).md>) — Dismisses the view controller that was presented modally by the view controller.
- [modalPresentationStyle](uiviewcontroller/modalpresentationstyle.md) — The presentation style for modal view controllers.
- [UIModalPresentationStyle](uimodalpresentationstyle.md) — Modal presentation styles available when presenting view controllers.
- [modalTransitionStyle](uiviewcontroller/modaltransitionstyle.md) — The transition style to use when presenting the view controller.
- [modalInPresentation](uiviewcontroller/ismodalinpresentation.md) — A Boolean value indicating whether the view controller enforces a modal behavior.
- [definesPresentationContext](uiviewcontroller/definespresentationcontext.md) — A Boolean value that indicates whether this view controller’s view is covered when the view controller or one of its descendants presents a view controller.
- [providesPresentationContextTransitionStyle](uiviewcontroller/providespresentationcontexttransitionstyle.md) — A Boolean value that indicates whether the view controller specifies the transition style for view controllers it presents.
- [disablesAutomaticKeyboardDismissal](uiviewcontroller/disablesautomatickeyboarddismissal.md) — Returns a Boolean indicating whether the current input view is dismissed automatically when changing controls.
- [UIViewControllerShowDetailTargetDidChangeNotification](uiviewcontroller/showdetailtargetdidchangenotification.md) — Posted when a split view controller is expanded or collapsed.

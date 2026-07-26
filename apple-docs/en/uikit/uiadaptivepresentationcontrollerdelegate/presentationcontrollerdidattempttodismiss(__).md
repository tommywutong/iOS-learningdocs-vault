---
title: 'presentationControllerDidAttemptToDismiss(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiadaptivepresentationcontrollerdelegate/presentationcontrollerdidattempttodismiss(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiadaptivepresentationcontrollerdelegate/presentationcontrollerdidattempttodismiss(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiadaptivepresentationcontrollerdelegate/presentationcontrollerdidattempttodismiss%28_%3A%29.json'
content_hash: 'sha256:c5ecf4c34ccb09c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAdaptivePresentationControllerDelegate](../uiadaptivepresentationcontrollerdelegate.md)

# presentationControllerDidAttemptToDismiss(_:)

<sub>Instance Method</sub>

Notifies the delegate that a user-initiated attempt to dismiss a view was prevented.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func presentationControllerDidAttemptToDismiss(_ presentationController: UIPresentationController)
```

## Parameters

- `presentationController` — The presentation controller managing the adaptivity change.

## Discussion

UIKit supports refusing to dismiss a presentation when the `presentationController`.[modalInPresentation](../uiviewcontroller/ismodalinpresentation.md) returns `true` or [- presentationControllerShouldDismiss:](<presentationcontrollershoulddismiss(__).md>) returns `false`.

Use this method to inform the user why the presentation can’t be dismissed, for example, by presenting an instance of [UIAlertController](../uialertcontroller.md).

## See Also

### Responding to adaptive transitions

- [- presentationController:willPresentWithAdaptiveStyle:transitionCoordinator:](<presentationcontroller(__willpresentwithadaptivestyle_transitioncoordinator_).md>) — Notifies the delegate that an adaptivity-related transition is about to occur.
- [- presentationControllerShouldDismiss:](<presentationcontrollershoulddismiss(__).md>) — Asks the delegate for permission to dismiss the presentation.
- [- presentationControllerDidDismiss:](<presentationcontrollerdiddismiss(__).md>) — Notifies the delegate after a presentation is dismissed.
- [- presentationControllerWillDismiss:](<presentationcontrollerwilldismiss(__).md>) — Notifies the delegate before a presentation is dismissed.

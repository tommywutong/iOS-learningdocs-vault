---
title: 'presentationControllerShouldDismiss(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiadaptivepresentationcontrollerdelegate/presentationcontrollershoulddismiss(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiadaptivepresentationcontrollerdelegate/presentationcontrollershoulddismiss(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiadaptivepresentationcontrollerdelegate/presentationcontrollershoulddismiss%28_%3A%29.json'
content_hash: 'sha256:0a8e64dcac514a11'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAdaptivePresentationControllerDelegate](../uiadaptivepresentationcontrollerdelegate.md)

# presentationControllerShouldDismiss(_:)

<sub>Instance Method</sub>

Asks the delegate for permission to dismiss the presentation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func presentationControllerShouldDismiss(_ presentationController: UIPresentationController) -> Bool
```

## Parameters

- `presentationController` — The presentation controller that manages the adaptivity change.

## Return Value

[true](../../swift/true.md) to allow the system to dismiss the presentation, [false](../../swift/false.md) to refuse the dismissal.

## Discussion

The system may call this method at any time. This method isn’t guaranteed to be followed by a call to [- presentationControllerWillDismiss:](<presentationcontrollerwilldismiss(__).md>) or [- presentationControllerDidDismiss:](<presentationcontrollerdiddismiss(__).md>). Make sure that your implementation of this method returns quickly.

## See Also

### Related Documentation

- [Disabling the pull-down gesture for a sheet](../disabling-the-pull-down-gesture-for-a-sheet.md) — Ensure a positive user experience when presenting a view controller as a sheet.

### Responding to adaptive transitions

- [- presentationController:willPresentWithAdaptiveStyle:transitionCoordinator:](<presentationcontroller(__willpresentwithadaptivestyle_transitioncoordinator_).md>) — Notifies the delegate that an adaptivity-related transition is about to occur.
- [- presentationControllerDidAttemptToDismiss:](<presentationcontrollerdidattempttodismiss(__).md>) — Notifies the delegate that a user-initiated attempt to dismiss a view was prevented.
- [- presentationControllerDidDismiss:](<presentationcontrollerdiddismiss(__).md>) — Notifies the delegate after a presentation is dismissed.
- [- presentationControllerWillDismiss:](<presentationcontrollerwilldismiss(__).md>) — Notifies the delegate before a presentation is dismissed.

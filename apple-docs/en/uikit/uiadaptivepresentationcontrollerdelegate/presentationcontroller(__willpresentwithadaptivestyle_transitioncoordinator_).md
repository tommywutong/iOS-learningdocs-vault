---
title: 'presentationController(_:willPresentWithAdaptiveStyle:transitionCoordinator:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.3+, iPadOS 8.3+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiadaptivepresentationcontrollerdelegate/presentationcontroller(_:willpresentwithadaptivestyle:transitioncoordinator:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiadaptivepresentationcontrollerdelegate/presentationcontroller(_:willpresentwithadaptivestyle:transitioncoordinator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiadaptivepresentationcontrollerdelegate/presentationcontroller%28_%3Awillpresentwithadaptivestyle%3Atransitioncoordinator%3A%29.json'
content_hash: 'sha256:513ffae6a10794b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAdaptivePresentationControllerDelegate](../uiadaptivepresentationcontrollerdelegate.md)

# presentationController(_:willPresentWithAdaptiveStyle:transitionCoordinator:)

<sub>Instance Method</sub>

Notifies the delegate that an adaptivity-related transition is about to occur.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func presentationController(_ presentationController: UIPresentationController, willPresentWithAdaptiveStyle style: UIModalPresentationStyle, transitionCoordinator: (any UIViewControllerTransitionCoordinator)?)
```

## Parameters

- `presentationController` — The presentation controller that is managing the adaptivity change.

- `style` — The new presentation style. If the presentation style is not changing, this parameter is set to [UIModalPresentationNone](../uimodalpresentationstyle/none.md).

- `transitionCoordinator` — The transition coordinator that is managing the transition.

## Discussion

When a size class change occurs, UIKit calls this method to let you know how the presentation controller will adapt. Use this method to make any additional changes. For example, you might use the transition coordinator object to create additional animations for the transition.

## See Also

### Responding to adaptive transitions

- [- presentationControllerDidAttemptToDismiss:](<presentationcontrollerdidattempttodismiss(__).md>) — Notifies the delegate that a user-initiated attempt to dismiss a view was prevented.
- [- presentationControllerShouldDismiss:](<presentationcontrollershoulddismiss(__).md>) — Asks the delegate for permission to dismiss the presentation.
- [- presentationControllerDidDismiss:](<presentationcontrollerdiddismiss(__).md>) — Notifies the delegate after a presentation is dismissed.
- [- presentationControllerWillDismiss:](<presentationcontrollerwilldismiss(__).md>) — Notifies the delegate before a presentation is dismissed.

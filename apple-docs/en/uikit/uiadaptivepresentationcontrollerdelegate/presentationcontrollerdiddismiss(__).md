---
title: 'presentationControllerDidDismiss(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiadaptivepresentationcontrollerdelegate/presentationcontrollerdiddismiss(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiadaptivepresentationcontrollerdelegate/presentationcontrollerdiddismiss(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiadaptivepresentationcontrollerdelegate/presentationcontrollerdiddismiss%28_%3A%29.json'
content_hash: 'sha256:d2e7b267918298f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAdaptivePresentationControllerDelegate](../uiadaptivepresentationcontrollerdelegate.md)

# presentationControllerDidDismiss(_:)

<sub>Instance Method</sub>

Notifies the delegate after a presentation is dismissed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func presentationControllerDidDismiss(_ presentationController: UIPresentationController)
```

## Parameters

- `presentationController` — The presentation controller managing the adaptivity change.

## Discussion

This method is not called if the presentation is dismissed programmatically.

## See Also

### Responding to adaptive transitions

- [- presentationController:willPresentWithAdaptiveStyle:transitionCoordinator:](<presentationcontroller(__willpresentwithadaptivestyle_transitioncoordinator_).md>) — Notifies the delegate that an adaptivity-related transition is about to occur.
- [- presentationControllerDidAttemptToDismiss:](<presentationcontrollerdidattempttodismiss(__).md>) — Notifies the delegate that a user-initiated attempt to dismiss a view was prevented.
- [- presentationControllerShouldDismiss:](<presentationcontrollershoulddismiss(__).md>) — Asks the delegate for permission to dismiss the presentation.
- [- presentationControllerWillDismiss:](<presentationcontrollerwilldismiss(__).md>) — Notifies the delegate before a presentation is dismissed.

---
title: 'presentationControllerWillDismiss(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiadaptivepresentationcontrollerdelegate/presentationcontrollerwilldismiss(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiadaptivepresentationcontrollerdelegate/presentationcontrollerwilldismiss(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiadaptivepresentationcontrollerdelegate/presentationcontrollerwilldismiss%28_%3A%29.json'
content_hash: 'sha256:db2b7da13459ae71'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAdaptivePresentationControllerDelegate](../uiadaptivepresentationcontrollerdelegate.md)

# presentationControllerWillDismiss(_:)

<sub>Instance Method</sub>

Notifies the delegate before a presentation is dismissed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func presentationControllerWillDismiss(_ presentationController: UIPresentationController)
```

## Parameters

- `presentationController` — The presentation controller managing the trait changes from your app.

## Discussion

You can use this method to set up animations or interaction notifications with the presentationController’s transitionCoordinator.

This method is not called if the presentation is dismissed programmatically.

## See Also

### Responding to adaptive transitions

- [- presentationController:willPresentWithAdaptiveStyle:transitionCoordinator:](<presentationcontroller(__willpresentwithadaptivestyle_transitioncoordinator_).md>) — Notifies the delegate that an adaptivity-related transition is about to occur.
- [- presentationControllerDidAttemptToDismiss:](<presentationcontrollerdidattempttodismiss(__).md>) — Notifies the delegate that a user-initiated attempt to dismiss a view was prevented.
- [- presentationControllerShouldDismiss:](<presentationcontrollershoulddismiss(__).md>) — Asks the delegate for permission to dismiss the presentation.
- [- presentationControllerDidDismiss:](<presentationcontrollerdiddismiss(__).md>) — Notifies the delegate after a presentation is dismissed.

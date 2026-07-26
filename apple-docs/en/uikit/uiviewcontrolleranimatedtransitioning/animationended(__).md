---
title: 'animationEnded(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontrolleranimatedtransitioning/animationended(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrolleranimatedtransitioning/animationended(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrolleranimatedtransitioning/animationended%28_%3A%29.json'
content_hash: 'sha256:3940af21ebdf30df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerAnimatedTransitioning](../uiviewcontrolleranimatedtransitioning.md)

# animationEnded(_:)

<sub>Instance Method</sub>

Tells your animator object that the transition animations have finished.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func animationEnded(_ transitionCompleted: Bool)
```

## Parameters

- `transitionCompleted` — Contains the value [true](../../swift/true.md) if the transition completed successfully and the new view controller is now displayed or [false](../../swift/false.md) if the transition was canceled and the original view controller is still visible.

## Discussion

UIKit calls this method at the end of a transition to let you know the results. Use this method to perform any final cleanup operations required by your transition animator when the transition finishes.

## See Also

### Performing a transition

- [- animateTransition:](<animatetransition(using_).md>) — Tells your animator object to perform the transition animations.

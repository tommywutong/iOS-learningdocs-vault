---
title: isAnimated
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/isanimated
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/isanimated'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/isanimated.json'
content_hash: 'sha256:1313cf5235d815af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerTransitionCoordinatorContext](../uiviewcontrollertransitioncoordinatorcontext.md)

# isAnimated

<sub>Instance Property</sub>

A Boolean value indicating whether the transition is explicitly animated.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isAnimated: Bool { get }
```

## Discussion

The value of this property is [false](../../swift/false.md) for custom transitions — transitions where the view controller’s [modalPresentationStyle](../uiviewcontroller/modalpresentationstyle.md) property is set to [UIModalPresentationCustom](../uimodalpresentationstyle/custom.md) — even when the transition is started by a call to the [- animateTransition:](<../uiviewcontrolleranimatedtransitioning/animatetransition(using_).md>) method. In nearly all other cases, the value of this property is [true](../../swift/true.md).

## See Also

### Getting the transition state

- [initiallyInteractive](initiallyinteractive.md) — A Boolean value indicating whether the transition started as an interactive transition.
- [interactive](isinteractive.md) — A Boolean value indicating whether the transition is currently interactive.
- [cancelled](iscancelled.md) — A Boolean value indicating whether an interactive transition was canceled.
- [isInterruptible](isinterruptible.md) — A Boolean value indicating whether the transition animations can be interrupted.

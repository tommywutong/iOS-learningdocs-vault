---
title: initiallyInteractive
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/initiallyinteractive
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/initiallyinteractive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/initiallyinteractive.json'
content_hash: 'sha256:b4ee8967d7d60101'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerTransitionCoordinatorContext](../uiviewcontrollertransitioncoordinatorcontext.md)

# initiallyInteractive

<sub>Instance Property</sub>

A Boolean value indicating whether the transition started as an interactive transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var initiallyInteractive: Bool { get }
```

## Discussion

The value of this property is [true](../../swift/true.md) when the transition was initiated interactively and the [animated](isanimated.md) property is also set to [true](../../swift/true.md); otherwise, the value is [false](../../swift/false.md). The value of this property doesn’t change during the course of a transition. To determine whether the transition is currently interactive, use the [interactive](isinteractive.md) method instead.

## See Also

### Getting the transition state

- [interactive](isinteractive.md) — A Boolean value indicating whether the transition is currently interactive.
- [animated](isanimated.md) — A Boolean value indicating whether the transition is explicitly animated.
- [cancelled](iscancelled.md) — A Boolean value indicating whether an interactive transition was canceled.
- [isInterruptible](isinterruptible.md) — A Boolean value indicating whether the transition animations can be interrupted.

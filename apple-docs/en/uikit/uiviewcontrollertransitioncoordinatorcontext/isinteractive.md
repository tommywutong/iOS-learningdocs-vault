---
title: isInteractive
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/isinteractive
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/isinteractive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/isinteractive.json'
content_hash: 'sha256:b98606124c28ab4c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerTransitionCoordinatorContext](../uiviewcontrollertransitioncoordinatorcontext.md)

# isInteractive

<sub>Instance Property</sub>

A Boolean value indicating whether the transition is currently interactive.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isInteractive: Bool { get }
```

## Discussion

Every interactive transition has at least one noninteractive segment — namely, when it’s completing. In addition, you can design an interactive transition to have intermediate segments that are noninteractive.

If the [initiallyInteractive](initiallyinteractive.md) property is set to [false](../../swift/false.md), the value of this property can be [true](../../swift/true.md) only when the [isInterruptible](isinterruptible.md) property is also [true](../../swift/true.md).

## See Also

### Getting the transition state

- [initiallyInteractive](initiallyinteractive.md) — A Boolean value indicating whether the transition started as an interactive transition.
- [animated](isanimated.md) — A Boolean value indicating whether the transition is explicitly animated.
- [cancelled](iscancelled.md) — A Boolean value indicating whether an interactive transition was canceled.
- [isInterruptible](isinterruptible.md) — A Boolean value indicating whether the transition animations can be interrupted.

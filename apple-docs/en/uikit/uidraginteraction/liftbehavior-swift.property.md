---
title: liftBehavior
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/uikit/uidraginteraction/liftbehavior-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uidraginteraction/liftbehavior-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidraginteraction/liftbehavior-swift.property.json'
content_hash: 'sha256:6ff8baf78873626a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDragInteraction](../uidraginteraction.md)

# liftBehavior

<sub>Instance Property</sub>

A value that controls the timing behavior for initiating a drag gesture from a touch.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var liftBehavior: UIDragInteraction.LiftBehavior { get set }
```

## Discussion

The default value is [UIDragLiftBehaviorDefault](liftbehavior-swift.enum/default.md), which uses the standard lift timing parameters.

Set this property to [UIDragLiftBehaviorExtended](liftbehavior-swift.enum/extended.md) in gesture-rich views where recognizers compete for the same touches. The extended behavior increases the lift delay and cancels the drag when a second touch is detected, allowing other long-press gestures on the same view to activate before the drag begins.

For pointer-initiated drags, use [allowsPointerDragBeforeLiftDelay](allowspointerdragbeforeliftdelay.md) to control whether pointer drags respect the lift delay independently of this property.

## See Also

### Configuring lift behavior

- [LiftBehavior](liftbehavior-swift.enum.md) — Constants that determine the lift behavior for a drag interaction. _(beta)_
- [allowsPointerDragBeforeLiftDelay](allowspointerdragbeforeliftdelay.md) — A Boolean value that controls whether pointer-initiated drags begin before the lift delay elapses. _(beta)_

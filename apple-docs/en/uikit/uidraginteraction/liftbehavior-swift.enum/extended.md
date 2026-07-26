---
title: UIDragInteraction.LiftBehavior.extended
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/uikit/uidraginteraction/liftbehavior-swift.enum/extended
source_url: 'https://developer.apple.com/documentation/uikit/uidraginteraction/liftbehavior-swift.enum/extended'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidraginteraction/liftbehavior-swift.enum/extended.json'
content_hash: 'sha256:05716f428f5d3b8e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIDragInteraction](../../uidraginteraction.md) · [LiftBehavior](../liftbehavior-swift.enum.md)

# UIDragInteraction.LiftBehavior.extended

<sub>Case</sub>

An extended lift behavior, which has a longer lift delay for the `UIDragInteraction`, allowing better disambiguation of gestures in the same view. This is useful for ‘canvas’ like views where they can be many gestures involved in the manipulation of objects on screen. For extended lifts, when a second touch is recognized in the view, the gesture will be cancelled.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case extended
```

## See Also

### Lift behaviors

- [UIDragLiftBehaviorDefault](default.md) — The default lift behavior, which configures the `UIDragInteraction` with the default timing parameters. _(beta)_

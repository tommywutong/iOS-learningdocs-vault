---
title: UIDragInteraction.LiftBehavior.default
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/uikit/uidraginteraction/liftbehavior-swift.enum/default
source_url: 'https://developer.apple.com/documentation/uikit/uidraginteraction/liftbehavior-swift.enum/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidraginteraction/liftbehavior-swift.enum/default.json'
content_hash: 'sha256:6098528761967abc'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIDragInteraction](../../uidraginteraction.md) · [LiftBehavior](../liftbehavior-swift.enum.md)

# UIDragInteraction.LiftBehavior.default

<sub>Case</sub>

The default lift behavior, which configures the `UIDragInteraction` with the default timing parameters.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case `default`
```

## See Also

### Lift behaviors

- [UIDragLiftBehaviorExtended](extended.md) — An extended lift behavior, which has a longer lift delay for the `UIDragInteraction`, allowing better disambiguation of gestures in the same view. This is useful for ‘canvas’ like views where they can be many gestures involved in the manipulation of objects on screen. For extended lifts, when a second touch is recognized in the view, the gesture will be cancelled. _(beta)_

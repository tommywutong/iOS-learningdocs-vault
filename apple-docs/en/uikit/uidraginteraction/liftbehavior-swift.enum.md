---
title: UIDragInteraction.LiftBehavior
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/uikit/uidraginteraction/liftbehavior-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uidraginteraction/liftbehavior-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidraginteraction/liftbehavior-swift.enum.json'
content_hash: 'sha256:d79234898b16b324'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDragInteraction](../uidraginteraction.md)

# UIDragInteraction.LiftBehavior

<sub>Enumeration</sub>

Constants that determine the lift behavior for a drag interaction.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum LiftBehavior
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Lift behaviors

- [UIDragLiftBehaviorDefault](liftbehavior-swift.enum/default.md) — The default lift behavior, which configures the `UIDragInteraction` with the default timing parameters. _(beta)_
- [UIDragLiftBehaviorExtended](liftbehavior-swift.enum/extended.md) — An extended lift behavior, which has a longer lift delay for the `UIDragInteraction`, allowing better disambiguation of gestures in the same view. This is useful for ‘canvas’ like views where they can be many gestures involved in the manipulation of objects on screen. For extended lifts, when a second touch is recognized in the view, the gesture will be cancelled. _(beta)_

### Initializers

- [init(rawValue:)](<liftbehavior-swift.enum/init(rawvalue_).md>) _(beta)_

## See Also

### Configuring lift behavior

- [liftBehavior](liftbehavior-swift.property.md) — A value that controls the timing behavior for initiating a drag gesture from a touch. _(beta)_
- [allowsPointerDragBeforeLiftDelay](allowspointerdragbeforeliftdelay.md) — A Boolean value that controls whether pointer-initiated drags begin before the lift delay elapses. _(beta)_

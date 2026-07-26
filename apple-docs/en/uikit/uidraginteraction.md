---
title: UIDragInteraction
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidraginteraction
source_url: 'https://developer.apple.com/documentation/uikit/uidraginteraction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidraginteraction.json'
content_hash: 'sha256:24c7afa5b0911dd8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDragInteraction

<sub>Class</sub>

An interaction to enable dragging of items from a view, employing a delegate to provide drag items and to respond to calls from the drag session.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIDragInteraction
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [UIInteraction](uiinteraction.md)

## Topics

### Initializing the drag interaction

- [- initWithDelegate:](<uidraginteraction/init(delegate_).md>) — Initializes a drag interaction object with a custom delegate object.

### Configuring lift behavior

- [liftBehavior](uidraginteraction/liftbehavior-swift.property.md) — A value that controls the timing behavior for initiating a drag gesture from a touch. _(beta)_
- [LiftBehavior](uidraginteraction/liftbehavior-swift.enum.md) — Constants that determine the lift behavior for a drag interaction. _(beta)_
- [allowsPointerDragBeforeLiftDelay](uidraginteraction/allowspointerdragbeforeliftdelay.md) — A Boolean value that controls whether pointer-initiated drags begin before the lift delay elapses. _(beta)_

### Managing drag interactions

- [allowsSimultaneousRecognitionDuringLift](uidraginteraction/allowssimultaneousrecognitionduringlift.md) — A Boolean value that determines whether the interaction allows recognition of other gestures during the lift activity.
- [delegate](uidraginteraction/delegate.md) — An object that configures and controls a drag interaction.
- [UIDragInteractionDelegate](uidraginteractiondelegate.md) — The interface for configuring and controlling a drag interaction.

### Enabling the interactions

- [enabled](uidraginteraction/isenabled.md) — A Boolean value that specifies whether the drag interaction responds to touches and is allowed to participate in a drag activity.
- [enabledByDefault](uidraginteraction/isenabledbydefault.md) — A device-dependent Boolean value that indicates whether a newly-instantiated drag interaction is allowed to participate in a drag activity.

## See Also

### Drag and drop interactions

- [UIDragInteractionDelegate](uidraginteractiondelegate.md) — The interface for configuring and controlling a drag interaction.
- [UIDropInteractionDelegate](uidropinteractiondelegate.md) — The interface for configuring and controlling a drop interaction.
- [UIDropInteraction](uidropinteraction.md) — An interaction to enable dropping of items onto a view, employing a delegate to instantiate objects and respond to calls from the drop session.

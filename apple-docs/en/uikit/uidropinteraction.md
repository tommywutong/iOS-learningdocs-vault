---
title: UIDropInteraction
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidropinteraction
source_url: 'https://developer.apple.com/documentation/uikit/uidropinteraction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidropinteraction.json'
content_hash: 'sha256:ea711d021a720c38'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDropInteraction

<sub>Class</sub>

An interaction to enable dropping of items onto a view, employing a delegate to instantiate objects and respond to calls from the drop session.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIDropInteraction
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [UIInteraction](uiinteraction.md)

## Topics

### Initializing drop interactions

- [- initWithDelegate:](<uidropinteraction/init(delegate_).md>) — Initializes a drop interaction object with a custom delegate object.

### Managing drop interactions

- [delegate](uidropinteraction/delegate.md) — An object that configures and controls a drop interaction.
- [UIDropInteractionDelegate](uidropinteractiondelegate.md) — The interface for configuring and controlling a drop interaction.

### Allowing simultaneous drops

- [allowsSimultaneousDropSessions](uidropinteraction/allowssimultaneousdropsessions.md) — A Boolean value that specifies whether the drop interaction handles more than one simultaneous drop session.

## See Also

### Drag and drop interactions

- [UIDragInteractionDelegate](uidraginteractiondelegate.md) — The interface for configuring and controlling a drag interaction.
- [UIDropInteractionDelegate](uidropinteractiondelegate.md) — The interface for configuring and controlling a drop interaction.
- [UIDragInteraction](uidraginteraction.md) — An interaction to enable dragging of items from a view, employing a delegate to provide drag items and to respond to calls from the drag session.

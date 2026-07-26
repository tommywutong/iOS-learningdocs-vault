---
title: UIPencilInteraction.Tap
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.5+, iPadOS 17.5+, Mac Catalyst 17.5+, visionOS 26.2+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipencilinteraction/tap
source_url: 'https://developer.apple.com/documentation/uikit/uipencilinteraction/tap'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipencilinteraction/tap.json'
content_hash: 'sha256:13c7d5f0f307ecac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPencilInteraction](../uipencilinteraction.md)

# UIPencilInteraction.Tap

<sub>Class</sub>

An interaction that represents a double tap on Apple Pencil.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class Tap
```

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md), [Sendable](../../swift/sendable.md)

## Topics

### Getting information about a double-tap interaction

- [timestamp](tap/timestamp.md) — The timestamp of the double-tap interaction.
- [hoverPose](tap/hoverpose.md) — The hover pose of Apple Pencil during a double-tap interaction.
- [UIPencilHoverPose](../uipencilhoverpose.md) — An object that describes the hover pose of Apple Pencil during an interaction like double tap or squeeze.

## See Also

### Apple Pencil interactions in UIKit

- [UIPencilInteraction](../uipencilinteraction.md) — An interaction that tells your app when a person double-taps or squeezes Apple Pencil.
- [UIPencilInteractionDelegate](../uipencilinteractiondelegate.md) — The interface an object implements to handle double taps or squeezes a person makes on Apple Pencil.
- [Squeeze](squeeze.md) — An interaction that represents a squeeze on Apple Pencil.
- [Phase](phase.md) — Constants that describe the phases of an interaction on Apple Pencil.
- [UIPencilHoverPose](../uipencilhoverpose.md) — An object that describes the hover pose of Apple Pencil during an interaction like double tap or squeeze.

---
title: UIPencilInteraction.Squeeze
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.5+, iPadOS 17.5+, Mac Catalyst 17.5+, visionOS 26.2+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipencilinteraction/squeeze
source_url: 'https://developer.apple.com/documentation/uikit/uipencilinteraction/squeeze'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipencilinteraction/squeeze.json'
content_hash: 'sha256:f87e47405006725a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPencilInteraction](../uipencilinteraction.md)

# UIPencilInteraction.Squeeze

<sub>Class</sub>

An interaction that represents a squeeze on Apple Pencil.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class Squeeze
```

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md), [Sendable](../../swift/sendable.md)

## Topics

### Getting information about a squeeze interaction

- [timestamp](squeeze/timestamp.md) — The timestamp of the squeeze interaction.
- [phase](squeeze/phase.md) — The phase of a squeeze interaction on Apple Pencil.
- [Phase](phase.md) — Constants that describe the phases of an interaction on Apple Pencil.
- [hoverPose](squeeze/hoverpose.md) — The hover pose of Apple Pencil during a squeeze interaction.
- [UIPencilHoverPose](../uipencilhoverpose.md) — An object that describes the hover pose of Apple Pencil during an interaction like double tap or squeeze.

## See Also

### Apple Pencil interactions in UIKit

- [UIPencilInteraction](../uipencilinteraction.md) — An interaction that tells your app when a person double-taps or squeezes Apple Pencil.
- [UIPencilInteractionDelegate](../uipencilinteractiondelegate.md) — The interface an object implements to handle double taps or squeezes a person makes on Apple Pencil.
- [Tap](tap.md) — An interaction that represents a double tap on Apple Pencil.
- [Phase](phase.md) — Constants that describe the phases of an interaction on Apple Pencil.
- [UIPencilHoverPose](../uipencilhoverpose.md) — An object that describes the hover pose of Apple Pencil during an interaction like double tap or squeeze.

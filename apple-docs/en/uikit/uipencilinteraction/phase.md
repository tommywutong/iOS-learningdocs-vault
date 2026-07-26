---
title: UIPencilInteraction.Phase
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 17.5+, iPadOS 17.5+, Mac Catalyst 17.5+, visionOS 26.2+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipencilinteraction/phase
source_url: 'https://developer.apple.com/documentation/uikit/uipencilinteraction/phase'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipencilinteraction/phase.json'
content_hash: 'sha256:cd25d2e2a7be4636'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPencilInteraction](../uipencilinteraction.md)

# UIPencilInteraction.Phase

<sub>Enumeration</sub>

Constants that describe the phases of an interaction on Apple Pencil.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum Phase
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Phases

- [UIPencilInteractionPhaseBegan](phase/began.md) — A continuous gesture on the pencil began
- [UIPencilInteractionPhaseCancelled](phase/cancelled.md) — A continuous gesture on the pencil was cancelled
- [UIPencilInteractionPhaseChanged](phase/changed.md) — A continuous gesture on the pencil changed
- [UIPencilInteractionPhaseEnded](phase/ended.md) — A continuous gesture on the pencil ended, or a discrete gesture on the pencil recognized

### Initializers

- [init(rawValue:)](<phase/init(rawvalue_).md>)

## See Also

### Apple Pencil interactions in UIKit

- [UIPencilInteraction](../uipencilinteraction.md) — An interaction that tells your app when a person double-taps or squeezes Apple Pencil.
- [UIPencilInteractionDelegate](../uipencilinteractiondelegate.md) — The interface an object implements to handle double taps or squeezes a person makes on Apple Pencil.
- [Tap](tap.md) — An interaction that represents a double tap on Apple Pencil.
- [Squeeze](squeeze.md) — An interaction that represents a squeeze on Apple Pencil.
- [UIPencilHoverPose](../uipencilhoverpose.md) — An object that describes the hover pose of Apple Pencil during an interaction like double tap or squeeze.

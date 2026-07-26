---
title: BreakthroughEffect
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/breakthrougheffect
source_url: 'https://developer.apple.com/documentation/swiftui/breakthrougheffect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/breakthrougheffect.json'
content_hash: 'sha256:3afdbcf35c5113dc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# BreakthroughEffect

<sub>Structure</sub>

<sub>visionOS</sub>

```swift
struct BreakthroughEffect
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [automatic](breakthrougheffect/automatic.md) — The system will choose the best effect for the type of element and its position within the scene. This might result in no breakthrough effect.
- [none](breakthrougheffect/none.md) — The element is clipped by occluding content. This is not supported when used to customize a sheet breakthrough effect.
- [prominent](breakthrougheffect/prominent.md) — The element is prominently revealed through occluding content.
- [subtle](breakthrougheffect/subtle.md) — The element is subtly blended over occluding content.

## See Also

### Configuring passthrough

- [preferredSurroundingsEffect(_:)](<view/preferredsurroundingseffect(__).md>) — Applies an effect to passthrough video.
- [SurroundingsEffect](surroundingseffect.md) — Effects that the system can apply to passthrough video.
- [breakthroughEffect(_:)](<view/breakthrougheffect(__).md>) — Ensures that the view is always visible to the user, even when other content is occluding it, like 3D models.

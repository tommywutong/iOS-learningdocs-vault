---
title: UICollisionBehavior.Mode
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollisionbehavior/mode
source_url: 'https://developer.apple.com/documentation/uikit/uicollisionbehavior/mode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollisionbehavior/mode.json'
content_hash: 'sha256:75a2c2f633a9201e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollisionBehavior](../uicollisionbehavior.md)

# UICollisionBehavior.Mode

<sub>Structure</sub>

The types of edges that participate in collisions for a collision behavior.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct Mode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [UICollisionBehaviorModeItems](mode/items.md) — Specifies that the dynamic items, associated with the collision behavior, collide only with each other and not with specified collision boundaries.
- [UICollisionBehaviorModeBoundaries](mode/boundaries.md) — Specifies that the dynamic items, associated with the collision behavior, collide only with specified collision boundaries and don’t collide with each other.
- [UICollisionBehaviorModeEverything](mode/everything.md) — Specifies that the dynamic items, associated with the collision behavior, collide with each other _and_ with specified collision boundaries.

### Initializers

- [init(rawValue:)](<mode/init(rawvalue_).md>) — Creates a collision behavior mode structure with the specified raw value.

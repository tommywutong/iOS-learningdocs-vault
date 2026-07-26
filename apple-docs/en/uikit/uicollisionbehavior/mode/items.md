---
title: items
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollisionbehavior/mode/items
source_url: 'https://developer.apple.com/documentation/uikit/uicollisionbehavior/mode/items'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollisionbehavior/mode/items.json'
content_hash: 'sha256:87c2d08d420fc01d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UICollisionBehavior](../../uicollisionbehavior.md) · [Mode](../mode.md)

# items

<sub>Type Property</sub>

Specifies that the dynamic items, associated with the collision behavior, collide only with each other and not with specified collision boundaries.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var items: UICollisionBehavior.Mode { get }
```

## See Also

### Constants

- [UICollisionBehaviorModeBoundaries](boundaries.md) — Specifies that the dynamic items, associated with the collision behavior, collide only with specified collision boundaries and don’t collide with each other.
- [UICollisionBehaviorModeEverything](everything.md) — Specifies that the dynamic items, associated with the collision behavior, collide with each other _and_ with specified collision boundaries.

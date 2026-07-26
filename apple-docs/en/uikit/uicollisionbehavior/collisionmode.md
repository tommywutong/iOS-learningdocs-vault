---
title: collisionMode
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollisionbehavior/collisionmode
source_url: 'https://developer.apple.com/documentation/uikit/uicollisionbehavior/collisionmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollisionbehavior/collisionmode.json'
content_hash: 'sha256:adedef8fcba39c1e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollisionBehavior](../uicollisionbehavior.md)

# collisionMode

<sub>Instance Property</sub>

The type of edges that participate in collisions for the collision behavior.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var collisionMode: UICollisionBehavior.Mode { get set }
```

## Discussion

To specify `collisionMode`, use one of the values in the [Mode](mode.md) enum. The default value is [UICollisionBehaviorModeEverything](mode/everything.md).

## See Also

### Configuring a collision behavior

- [- addBoundaryWithIdentifier:forPath:](<addboundary(withidentifier_for_).md>) — Adds a collision boundary, specified as a Bezier path, to the collision behavior.
- [- addBoundaryWithIdentifier:fromPoint:toPoint:](<addboundary(withidentifier_from_to_).md>) — Adds a collision boundary, specified as a line segment, to the collision behavior.
- [boundaryIdentifiers](boundaryidentifiers.md) — The set of boundary identifiers that you’ve added to the collision behavior.
- [- boundaryWithIdentifier:](<boundary(withidentifier_).md>) — Returns a specified Bezier-path boundary.
- [- removeAllBoundaries](<removeallboundaries().md>) — Removes all previously-specified collision boundaries from the collision behavior.
- [- removeBoundaryWithIdentifier:](<removeboundary(withidentifier_).md>) — Removes a specific collision boundary from the collision behavior.
- [- setTranslatesReferenceBoundsIntoBoundaryWithInsets:](<settranslatesreferenceboundsintoboundary(with_).md>) — Specifies a collision boundary based on the bounds of the animation reference system, with optional insets.
- [translatesReferenceBoundsIntoBoundary](translatesreferenceboundsintoboundary.md) — Specifies whether a boundary based on the reference system is active.

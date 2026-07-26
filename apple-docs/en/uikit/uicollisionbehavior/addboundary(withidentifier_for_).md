---
title: 'addBoundary(withIdentifier:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollisionbehavior/addboundary(withidentifier:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollisionbehavior/addboundary(withidentifier:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollisionbehavior/addboundary%28withidentifier%3Afor%3A%29.json'
content_hash: 'sha256:a0e00210aeb9f0d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollisionBehavior](../uicollisionbehavior.md)

# addBoundary(withIdentifier:for:)

<sub>Instance Method</sub>

Adds a collision boundary, specified as a Bezier path, to the collision behavior.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func addBoundary(withIdentifier identifier: any NSCopying, for bezierPath: UIBezierPath)
```

## Parameters

- `identifier` — An arbitrary identifier for the boundary you are adding.

- `bezierPath` — An arbitrary Bezier path that specifies the collision boundary you are adding. The coordinate system and origin point for the path depend on how you’ve initialized the dynamic animator (that you’re adding the behavior to). See the overview in [UIDynamicAnimator](../uidynamicanimator.md) for more information.

## See Also

### Configuring a collision behavior

- [- addBoundaryWithIdentifier:fromPoint:toPoint:](<addboundary(withidentifier_from_to_).md>) — Adds a collision boundary, specified as a line segment, to the collision behavior.
- [boundaryIdentifiers](boundaryidentifiers.md) — The set of boundary identifiers that you’ve added to the collision behavior.
- [- boundaryWithIdentifier:](<boundary(withidentifier_).md>) — Returns a specified Bezier-path boundary.
- [collisionMode](collisionmode.md) — The type of edges that participate in collisions for the collision behavior.
- [- removeAllBoundaries](<removeallboundaries().md>) — Removes all previously-specified collision boundaries from the collision behavior.
- [- removeBoundaryWithIdentifier:](<removeboundary(withidentifier_).md>) — Removes a specific collision boundary from the collision behavior.
- [- setTranslatesReferenceBoundsIntoBoundaryWithInsets:](<settranslatesreferenceboundsintoboundary(with_).md>) — Specifies a collision boundary based on the bounds of the animation reference system, with optional insets.
- [translatesReferenceBoundsIntoBoundary](translatesreferenceboundsintoboundary.md) — Specifies whether a boundary based on the reference system is active.

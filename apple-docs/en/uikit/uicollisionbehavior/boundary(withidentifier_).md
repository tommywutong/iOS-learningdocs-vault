---
title: 'boundary(withIdentifier:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollisionbehavior/boundary(withidentifier:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollisionbehavior/boundary(withidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollisionbehavior/boundary%28withidentifier%3A%29.json'
content_hash: 'sha256:13e62e64ebf61789'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollisionBehavior](../uicollisionbehavior.md)

# boundary(withIdentifier:)

<sub>Instance Method</sub>

Returns a specified Bezier-path boundary.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func boundary(withIdentifier identifier: any NSCopying) -> UIBezierPath?
```

## Parameters

- `identifier` — A boundary identifier that you’ve previously added to the collision behavior.

## Return Value

A Bezier-path boundary.

## See Also

### Configuring a collision behavior

- [- addBoundaryWithIdentifier:forPath:](<addboundary(withidentifier_for_).md>) — Adds a collision boundary, specified as a Bezier path, to the collision behavior.
- [- addBoundaryWithIdentifier:fromPoint:toPoint:](<addboundary(withidentifier_from_to_).md>) — Adds a collision boundary, specified as a line segment, to the collision behavior.
- [boundaryIdentifiers](boundaryidentifiers.md) — The set of boundary identifiers that you’ve added to the collision behavior.
- [collisionMode](collisionmode.md) — The type of edges that participate in collisions for the collision behavior.
- [- removeAllBoundaries](<removeallboundaries().md>) — Removes all previously-specified collision boundaries from the collision behavior.
- [- removeBoundaryWithIdentifier:](<removeboundary(withidentifier_).md>) — Removes a specific collision boundary from the collision behavior.
- [- setTranslatesReferenceBoundsIntoBoundaryWithInsets:](<settranslatesreferenceboundsintoboundary(with_).md>) — Specifies a collision boundary based on the bounds of the animation reference system, with optional insets.
- [translatesReferenceBoundsIntoBoundary](translatesreferenceboundsintoboundary.md) — Specifies whether a boundary based on the reference system is active.

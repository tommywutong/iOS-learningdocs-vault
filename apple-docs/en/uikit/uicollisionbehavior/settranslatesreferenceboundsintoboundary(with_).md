---
title: 'setTranslatesReferenceBoundsIntoBoundary(with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollisionbehavior/settranslatesreferenceboundsintoboundary(with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollisionbehavior/settranslatesreferenceboundsintoboundary(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollisionbehavior/settranslatesreferenceboundsintoboundary%28with%3A%29.json'
content_hash: 'sha256:bbac00830e91b8e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollisionBehavior](../uicollisionbehavior.md)

# setTranslatesReferenceBoundsIntoBoundary(with:)

<sub>Instance Method</sub>

Specifies a collision boundary based on the bounds of the animation reference system, with optional insets.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setTranslatesReferenceBoundsIntoBoundary(with insets: UIEdgeInsets)
```

## Parameters

- `insets` — Insets to apply to the reference system’s bounds when defining the collision boundary.

## Discussion

The result of using this method depends on how you’ve initialized the dynamic animator (of class [UIDynamicAnimator](../uidynamicanimator.md)) that you’ve added the collision behavior to. See the overview in [UIDynamicAnimator](../uidynamicanimator.md) for a discussion of initialization options and modes for animators.

Here is how the dynamic animator’s initialization impacts use of this method:

- For a view-only dynamic animator, the reference bounds are those of the reference view
- For a collection-view dynamic animator, the reference bounds are those of the collection view layout
- For a dynamic-item dynamic animator, there are no reference bounds.

For a collision behavior added to a view-only or collection-view dynamic animator, activate a reference-system-based collision boundary by setting the [translatesReferenceBoundsIntoBoundary](translatesreferenceboundsintoboundary.md) property to [true](../../swift/true.md).

## See Also

### Configuring a collision behavior

- [- addBoundaryWithIdentifier:forPath:](<addboundary(withidentifier_for_).md>) — Adds a collision boundary, specified as a Bezier path, to the collision behavior.
- [- addBoundaryWithIdentifier:fromPoint:toPoint:](<addboundary(withidentifier_from_to_).md>) — Adds a collision boundary, specified as a line segment, to the collision behavior.
- [boundaryIdentifiers](boundaryidentifiers.md) — The set of boundary identifiers that you’ve added to the collision behavior.
- [- boundaryWithIdentifier:](<boundary(withidentifier_).md>) — Returns a specified Bezier-path boundary.
- [collisionMode](collisionmode.md) — The type of edges that participate in collisions for the collision behavior.
- [- removeAllBoundaries](<removeallboundaries().md>) — Removes all previously-specified collision boundaries from the collision behavior.
- [- removeBoundaryWithIdentifier:](<removeboundary(withidentifier_).md>) — Removes a specific collision boundary from the collision behavior.
- [translatesReferenceBoundsIntoBoundary](translatesreferenceboundsintoboundary.md) — Specifies whether a boundary based on the reference system is active.

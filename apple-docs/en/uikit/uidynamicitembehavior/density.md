---
title: density
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidynamicitembehavior/density
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicitembehavior/density'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicitembehavior/density.json'
content_hash: 'sha256:e6c0612cd9106b74'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDynamicItemBehavior](../uidynamicitembehavior.md)

# density

<sub>Instance Property</sub>

The relative mass density of the behavior’s dynamic items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var density: CGFloat { get set }
```

## Discussion

A dynamic item’s relative density, along with its size, determines its effective mass when it participates in UIKit Dynamics behaviors—including friction, collisions, pushes, and so on. For example, say you have two dynamic items with the same density but different sizes: item one is `100 x 100` points and item two is `100 x 200` points. In this example, item two has twice the effective mass of item one. In an elastic collision, these items exhibit a natural conservation of momentum according to their relative masses.

A `100 x 100` point dynamic item with a density of `1.0`, to which you apply a force (via a push behavior) of magnitude `1.0`, accelerates at `100` points per second².

## See Also

### Configuring a dynamic item behavior

- [- addAngularVelocity:forItem:](<addangularvelocity(__for_).md>) — Adds a specified angular velocity to a dynamic item.
- [- addLinearVelocity:forItem:](<addlinearvelocity(__for_).md>) — Adds a specified linear velocity to a dynamic item.
- [allowsRotation](allowsrotation.md) — Specifies whether rotation is allowed for the behavior’s dynamic items.
- [angularResistance](angularresistance.md) — The angular resistance for the behavior’s dynamic items.
- [- angularVelocityForItem:](<angularvelocity(for_).md>) — Returns the angular velocity for a specified dynamic item.
- [- linearVelocityForItem:](<linearvelocity(for_).md>) — Returns the linear velocity for a specified dynamic item.
- [elasticity](elasticity.md) — The amount of elasticity applied to collisions for the behavior’s dynamic items.
- [friction](friction.md) — The linear resistance for the behavior’s dynamic items when two slide against each other.
- [resistance](resistance.md) — The linear resistance for the behavior’s dynamic items, which reduces their linear velocity over time.
- [charge](charge.md) — The charge associated with the item.
- [anchored](isanchored.md) — A Boolean value indicating whether the item is anchored to its current position.

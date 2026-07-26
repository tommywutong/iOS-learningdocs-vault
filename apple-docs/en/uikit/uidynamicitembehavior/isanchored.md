---
title: isAnchored
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidynamicitembehavior/isanchored
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicitembehavior/isanchored'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicitembehavior/isanchored.json'
content_hash: 'sha256:977ac65335ed2837'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDynamicItemBehavior](../uidynamicitembehavior.md)

# isAnchored

<sub>Instance Property</sub>

A Boolean value indicating whether the item is anchored to its current position.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isAnchored: Bool { get set }
```

## Discussion

An anchored item participates in collisions but is not affected by those collisions. Instead, the item behaves like a collision boundary. The default value of this property is [false](../../swift/false.md).

## See Also

### Configuring a dynamic item behavior

- [- addAngularVelocity:forItem:](<addangularvelocity(__for_).md>) — Adds a specified angular velocity to a dynamic item.
- [- addLinearVelocity:forItem:](<addlinearvelocity(__for_).md>) — Adds a specified linear velocity to a dynamic item.
- [allowsRotation](allowsrotation.md) — Specifies whether rotation is allowed for the behavior’s dynamic items.
- [angularResistance](angularresistance.md) — The angular resistance for the behavior’s dynamic items.
- [- angularVelocityForItem:](<angularvelocity(for_).md>) — Returns the angular velocity for a specified dynamic item.
- [- linearVelocityForItem:](<linearvelocity(for_).md>) — Returns the linear velocity for a specified dynamic item.
- [density](density.md) — The relative mass density of the behavior’s dynamic items.
- [elasticity](elasticity.md) — The amount of elasticity applied to collisions for the behavior’s dynamic items.
- [friction](friction.md) — The linear resistance for the behavior’s dynamic items when two slide against each other.
- [resistance](resistance.md) — The linear resistance for the behavior’s dynamic items, which reduces their linear velocity over time.
- [charge](charge.md) — The charge associated with the item.

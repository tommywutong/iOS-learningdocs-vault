---
title: angularResistance
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidynamicitembehavior/angularresistance
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicitembehavior/angularresistance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicitembehavior/angularresistance.json'
content_hash: 'sha256:96e9121241a5a069'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDynamicItemBehavior](../uidynamicitembehavior.md)

# angularResistance

<sub>Instance Property</sub>

The angular resistance for the behavior’s dynamic items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var angularResistance: CGFloat { get set }
```

## Discussion

Valid range is `0` through [CGFLOAT_MAX](../../corefoundation/cgfloat_max.md). The greater the value, the greater the angular damping and the faster rotation slows to a stop.

## See Also

### Configuring a dynamic item behavior

- [- addAngularVelocity:forItem:](<addangularvelocity(__for_).md>) — Adds a specified angular velocity to a dynamic item.
- [- addLinearVelocity:forItem:](<addlinearvelocity(__for_).md>) — Adds a specified linear velocity to a dynamic item.
- [allowsRotation](allowsrotation.md) — Specifies whether rotation is allowed for the behavior’s dynamic items.
- [- angularVelocityForItem:](<angularvelocity(for_).md>) — Returns the angular velocity for a specified dynamic item.
- [- linearVelocityForItem:](<linearvelocity(for_).md>) — Returns the linear velocity for a specified dynamic item.
- [density](density.md) — The relative mass density of the behavior’s dynamic items.
- [elasticity](elasticity.md) — The amount of elasticity applied to collisions for the behavior’s dynamic items.
- [friction](friction.md) — The linear resistance for the behavior’s dynamic items when two slide against each other.
- [resistance](resistance.md) — The linear resistance for the behavior’s dynamic items, which reduces their linear velocity over time.
- [charge](charge.md) — The charge associated with the item.
- [anchored](isanchored.md) — A Boolean value indicating whether the item is anchored to its current position.

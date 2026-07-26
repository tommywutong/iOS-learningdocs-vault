---
title: 'addLinearVelocity(_:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidynamicitembehavior/addlinearvelocity(_:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicitembehavior/addlinearvelocity(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicitembehavior/addlinearvelocity%28_%3Afor%3A%29.json'
content_hash: 'sha256:e4acc0abece91ce8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDynamicItemBehavior](../uidynamicitembehavior.md)

# addLinearVelocity(_:for:)

<sub>Instance Method</sub>

Adds a specified linear velocity to a dynamic item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func addLinearVelocity(_ velocity: CGPoint, for item: any UIDynamicItem)
```

## Parameters

- `velocity` — The linear velocity, expressed in points per second, that you want to add to the specified dynamic item. Default value is `0`. Applying a negative value reduces the linear velocity by the specified amount.

- `item` — The dynamic item whose linear velocity you want to increase (or decrease).

## See Also

### Configuring a dynamic item behavior

- [- addAngularVelocity:forItem:](<addangularvelocity(__for_).md>) — Adds a specified angular velocity to a dynamic item.
- [allowsRotation](allowsrotation.md) — Specifies whether rotation is allowed for the behavior’s dynamic items.
- [angularResistance](angularresistance.md) — The angular resistance for the behavior’s dynamic items.
- [- angularVelocityForItem:](<angularvelocity(for_).md>) — Returns the angular velocity for a specified dynamic item.
- [- linearVelocityForItem:](<linearvelocity(for_).md>) — Returns the linear velocity for a specified dynamic item.
- [density](density.md) — The relative mass density of the behavior’s dynamic items.
- [elasticity](elasticity.md) — The amount of elasticity applied to collisions for the behavior’s dynamic items.
- [friction](friction.md) — The linear resistance for the behavior’s dynamic items when two slide against each other.
- [resistance](resistance.md) — The linear resistance for the behavior’s dynamic items, which reduces their linear velocity over time.
- [charge](charge.md) — The charge associated with the item.
- [anchored](isanchored.md) — A Boolean value indicating whether the item is anchored to its current position.

---
title: 'angularVelocity(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidynamicitembehavior/angularvelocity(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicitembehavior/angularvelocity(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicitembehavior/angularvelocity%28for%3A%29.json'
content_hash: 'sha256:4bd1503ae5d136c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDynamicItemBehavior](../uidynamicitembehavior.md)

# angularVelocity(for:)

<sub>Instance Method</sub>

Returns the angular velocity for a specified dynamic item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func angularVelocity(for item: any UIDynamicItem) -> CGFloat
```

## Parameters

- `item` — The dynamic item whose angular velocity you want to get.

## Return Value

The angular velocity of the specified dynamic item, in radians per second.

## See Also

### Configuring a dynamic item behavior

- [- addAngularVelocity:forItem:](<addangularvelocity(__for_).md>) — Adds a specified angular velocity to a dynamic item.
- [- addLinearVelocity:forItem:](<addlinearvelocity(__for_).md>) — Adds a specified linear velocity to a dynamic item.
- [allowsRotation](allowsrotation.md) — Specifies whether rotation is allowed for the behavior’s dynamic items.
- [angularResistance](angularresistance.md) — The angular resistance for the behavior’s dynamic items.
- [- linearVelocityForItem:](<linearvelocity(for_).md>) — Returns the linear velocity for a specified dynamic item.
- [density](density.md) — The relative mass density of the behavior’s dynamic items.
- [elasticity](elasticity.md) — The amount of elasticity applied to collisions for the behavior’s dynamic items.
- [friction](friction.md) — The linear resistance for the behavior’s dynamic items when two slide against each other.
- [resistance](resistance.md) — The linear resistance for the behavior’s dynamic items, which reduces their linear velocity over time.
- [charge](charge.md) — The charge associated with the item.
- [anchored](isanchored.md) — A Boolean value indicating whether the item is anchored to its current position.

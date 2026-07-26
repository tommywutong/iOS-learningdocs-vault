---
title: UIDynamicItemBehavior
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidynamicitembehavior
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicitembehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicitembehavior.json'
content_hash: 'sha256:029bc380709404bc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDynamicItemBehavior

<sub>Class</sub>

A base dynamic animation configuration for one or more dynamic items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIDynamicItemBehavior
```

## Overview

A _dynamic item_ is any iOS or custom object that conforms to the [UIDynamicItem](uidynamicitem.md) protocol. The [UIView](uiview.md) and [UICollectionViewLayoutAttributes](uicollectionviewlayoutattributes.md) classes implement this protocol in iOS 7 and later. You can use a custom object as a dynamic item for such purposes as reacting to rotation or position changes computed by a dynamic animator—an instance of the [UIDynamicAnimator](uidynamicanimator.md) class.

One notable and common use of a dynamic item behavior is to confer a velocity to a dynamic item to match the ending velocity of a user gesture.

To use a dynamic item behavior with a dynamic item, perform these two steps:

1. Associate the item with the behavior using the [- addItem:](<uidynamicitembehavior/additem(__).md>) method, or initialize a new dynamic item behavior with an array of items using the [- initWithItems:](<uidynamicitembehavior/init(items_).md>) method
2. Enable the behavior by adding it to an animator using the [- addBehavior:](<uidynamicanimator/addbehavior(__).md>) method

The coordinate system that pertains to a dynamic item behavior, and the types of dynamic items you can use with the behavior, depend on how you initialized the associated animator. For details, see [UIDynamicAnimator](uidynamicanimator.md).

You can disable rotation for a dynamic item behavior’s items by returning [false](../swift/false.md) from the [allowsRotation](uidynamicitembehavior/allowsrotation.md) property. To configure interaction among the behavior’s items, use the [elasticity](uidynamicitembehavior/elasticity.md) and [friction](uidynamicitembehavior/friction.md) properties.

You can include a dynamic item behavior in a custom, composite behavior by starting with a [UIDynamicBehavior](uidynamicbehavior.md) object and adding a dynamic item behavior with the [- addChildBehavior:](<uidynamicbehavior/addchildbehavior(__).md>) method. If you want to influence a dynamic item behavior at each step of a dynamic animation, implement the inherited [action](uidynamicbehavior/action.md) method.

If you add more than one dynamic item behavior to an animator, you effectively create a behavior tree. Only one configuration of a given property applies to any given dynamic item. For a property configured in more than one dynamic item behavior, the last one in the behavior tree, starting from the dynamic animator and going depth first toward the dynamic item, wins.

In the case of an animator with exactly one dynamic item behavior, you can restore default values for all dynamic item behavior properties by removing the behavior. In the case of an animator to which you’ve applied multiple dynamic item behaviors, removing one takes its property contribution out of the behavior tree.

## Relationships

- **Inherits From**: [UIDynamicBehavior](uidynamicbehavior.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializing and managing a dynamic item behavior

- [- addItem:](<uidynamicitembehavior/additem(__).md>) — Adds a dynamic item to the dynamic item behavior’s item array.
- [- initWithItems:](<uidynamicitembehavior/init(items_).md>) — Initializes a dynamic item behavior with an array of dynamic items.
- [- removeItem:](<uidynamicitembehavior/removeitem(__).md>) — Removes a specific dynamic item from the dynamic item behavior.
- [items](uidynamicitembehavior/items.md) — Returns the set of dynamic items you’ve added to the dynamic item behavior.

### Configuring a dynamic item behavior

- [- addAngularVelocity:forItem:](<uidynamicitembehavior/addangularvelocity(__for_).md>) — Adds a specified angular velocity to a dynamic item.
- [- addLinearVelocity:forItem:](<uidynamicitembehavior/addlinearvelocity(__for_).md>) — Adds a specified linear velocity to a dynamic item.
- [allowsRotation](uidynamicitembehavior/allowsrotation.md) — Specifies whether rotation is allowed for the behavior’s dynamic items.
- [angularResistance](uidynamicitembehavior/angularresistance.md) — The angular resistance for the behavior’s dynamic items.
- [- angularVelocityForItem:](<uidynamicitembehavior/angularvelocity(for_).md>) — Returns the angular velocity for a specified dynamic item.
- [- linearVelocityForItem:](<uidynamicitembehavior/linearvelocity(for_).md>) — Returns the linear velocity for a specified dynamic item.
- [density](uidynamicitembehavior/density.md) — The relative mass density of the behavior’s dynamic items.
- [elasticity](uidynamicitembehavior/elasticity.md) — The amount of elasticity applied to collisions for the behavior’s dynamic items.
- [friction](uidynamicitembehavior/friction.md) — The linear resistance for the behavior’s dynamic items when two slide against each other.
- [resistance](uidynamicitembehavior/resistance.md) — The linear resistance for the behavior’s dynamic items, which reduces their linear velocity over time.
- [charge](uidynamicitembehavior/charge.md) — The charge associated with the item.
- [anchored](uidynamicitembehavior/isanchored.md) — A Boolean value indicating whether the item is anchored to its current position.

## See Also

### Dynamic items

- [UIDynamicItem](uidynamicitem.md) — A set of methods that can make a custom object eligible to participate in UIKit Dynamics.
- [UIDynamicItemGroup](uidynamicitemgroup.md) — A dynamic item that comprises multiple other dynamic items.

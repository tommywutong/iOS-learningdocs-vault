---
title: UICollisionBehavior
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollisionbehavior
source_url: 'https://developer.apple.com/documentation/uikit/uicollisionbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollisionbehavior.json'
content_hash: 'sha256:edc24e6e11624873'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICollisionBehavior

<sub>Class</sub>

An object that confers to a specified array of dynamic items the ability to engage in collisions with each other and with the behavior’s specified boundaries.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UICollisionBehavior
```

## Overview

A collision behavior also specifies some characteristics of its items’ collisions, with other characteristics optionally specified by a [UIDynamicItemBehavior](uidynamicitembehavior.md) object. A _dynamic item_ is any iOS or custom object that conforms to the [UIDynamicItem](uidynamicitem.md) protocol. The [UIView](uiview.md) and [UICollectionViewLayoutAttributes](uicollectionviewlayoutattributes.md) classes implement this protocol starting in iOS 7.0. You can use a custom object as a dynamic item for such purposes as reacting to rotation or position changes computed by a dynamic animator—an instance of the [UIDynamicAnimator](uidynamicanimator.md) class.

To use a collision behavior with a dynamic item, perform these two steps:

1. Associate the item with the behavior using the [- addItem:](<uicollisionbehavior/additem(__).md>) method, or initialize a new collision behavior with an array of items using the [- initWithItems:](<uicollisionbehavior/init(items_).md>) method.
2. Enable the behavior by adding it to an animator using the [- addBehavior:](<uidynamicanimator/addbehavior(__).md>) method

The coordinate system that pertains to a collision behavior, and the types of dynamic items you can use with the behavior, depend on how you initialized the associated animator. For details, read the Overview of [UIDynamicAnimator](uidynamicanimator.md).

You can add multiple collision behaviors to a dynamic animator. A dynamic item can be part of any number of collision behaviors, provided those behaviors belong to the same animator. For example, you can specify a collision behavior for a set of say, blue, items and another for, say, pink items. When you add both behaviors to a dynamic animator, blue items can collide with each other and pink items can collide with each other, but a blue item and a pink item would not collide—they would ignore each other.

By default, a collision behavior’s items can collide with each other _and_ with any boundaries you’ve specified for the behavior. If you want to specify that a behavior’s items collide only with each other, or only with boundaries, explicitly set the [collisionMode](uicollisionbehavior/collisionmode.md) property.

You can define a collision boundary with a bezier path (see the [- addBoundaryWithIdentifier:forPath:](<uicollisionbehavior/addboundary(withidentifier_for_).md>) method) or with a line segment (see the [- addBoundaryWithIdentifier:fromPoint:toPoint:](<uicollisionbehavior/addboundary(withidentifier_from_to_).md>) method). When you use a collision behavior with a dynamic animator you’ve initialized with a reference view or a collection view layout, you can also specify a collision boundary according to the bounds of the dynamic animator’s coordinate system (see the [- setTranslatesReferenceBoundsIntoBoundaryWithInsets:](<uicollisionbehavior/settranslatesreferenceboundsintoboundary(with_).md>) method).

> [!important] Important
> When setting the initial position for a dynamic item, you must ensure that its bounds do not intersect any collision boundaries. The animation behavior for such a misplaced item is undefined.

To respond to collisions, implement a delegate object that adopts the [UICollisionBehaviorDelegate](uicollisionbehaviordelegate.md) protocol. Add the delegate to the behavior using the [collisionDelegate](uicollisionbehavior/collisiondelegate.md) property.

You can include a collision behavior in a custom, composite behavior by starting with a [UIDynamicBehavior](uidynamicbehavior.md) object and adding a collision behavior with the [- addChildBehavior:](<uidynamicbehavior/addchildbehavior(__).md>) method.  If you want to influence a collision behavior at each step of a dynamic animation, implement the inherited [action](uidynamicbehavior/action.md) method.

## Relationships

- **Inherits From**: [UIDynamicBehavior](uidynamicbehavior.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializing and managing a collision behavior

- [- addItem:](<uicollisionbehavior/additem(__).md>) — Adds a dynamic item to the collision behavior’s item array.
- [- initWithItems:](<uicollisionbehavior/init(items_).md>) — Initializes a collision behavior with an array of dynamic items.
- [- removeItem:](<uicollisionbehavior/removeitem(__).md>) — Removes a specific dynamic item from the collision behavior.
- [items](uicollisionbehavior/items.md) — Returns the set of dynamic items you’ve added to the collision behavior.

### Customizing the collision behavior

- [collisionDelegate](uicollisionbehavior/collisiondelegate.md) — The delegate object that you want to respond to collisions for the collision behavior.
- [UICollisionBehaviorDelegate](uicollisionbehaviordelegate.md) — To respond to UIKit dynamic item collisions, configure a custom class to adopt the [UICollisionBehaviorDelegate](uicollisionbehaviordelegate.md) protocol. Then, in a collision behavior (an instance of the [UICollisionBehavior](uicollisionbehavior.md) class), set the delegate to be an instance of your custom class.

### Configuring a collision behavior

- [- addBoundaryWithIdentifier:forPath:](<uicollisionbehavior/addboundary(withidentifier_for_).md>) — Adds a collision boundary, specified as a Bezier path, to the collision behavior.
- [- addBoundaryWithIdentifier:fromPoint:toPoint:](<uicollisionbehavior/addboundary(withidentifier_from_to_).md>) — Adds a collision boundary, specified as a line segment, to the collision behavior.
- [boundaryIdentifiers](uicollisionbehavior/boundaryidentifiers.md) — The set of boundary identifiers that you’ve added to the collision behavior.
- [- boundaryWithIdentifier:](<uicollisionbehavior/boundary(withidentifier_).md>) — Returns a specified Bezier-path boundary.
- [collisionMode](uicollisionbehavior/collisionmode.md) — The type of edges that participate in collisions for the collision behavior.
- [- removeAllBoundaries](<uicollisionbehavior/removeallboundaries().md>) — Removes all previously-specified collision boundaries from the collision behavior.
- [- removeBoundaryWithIdentifier:](<uicollisionbehavior/removeboundary(withidentifier_).md>) — Removes a specific collision boundary from the collision behavior.
- [- setTranslatesReferenceBoundsIntoBoundaryWithInsets:](<uicollisionbehavior/settranslatesreferenceboundsintoboundary(with_).md>) — Specifies a collision boundary based on the bounds of the animation reference system, with optional insets.
- [translatesReferenceBoundsIntoBoundary](uicollisionbehavior/translatesreferenceboundsintoboundary.md) — Specifies whether a boundary based on the reference system is active.

### Constants

- [Mode](uicollisionbehavior/mode.md) — The types of edges that participate in collisions for a collision behavior.

## See Also

### Behaviors

- [UIDynamicBehavior](uidynamicbehavior.md) — An object that confers a behavioral configuration on one or more dynamic items, for their participation in 2D animation.
- [UIAttachmentBehavior](uiattachmentbehavior.md) — A relationship between two dynamic items, or between a dynamic item and an anchor point.
- [UIFieldBehavior](uifieldbehavior.md) — An object that applies field-based physics to dynamic items.
- [UIGravityBehavior](uigravitybehavior.md) — An object that applies a gravity-like force to all of its associated dynamic items.
- [UIPushBehavior](uipushbehavior.md) — A behavior that applies a continuous or instantaneous force to one or more dynamic items, causing those items to change position accordingly.
- [UISnapBehavior](uisnapbehavior.md) — A spring-like behavior whose initial motion is damped over time so that the object settles at a specific point.

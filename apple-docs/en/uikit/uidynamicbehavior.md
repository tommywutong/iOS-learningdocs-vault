---
title: UIDynamicBehavior
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidynamicbehavior
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicbehavior.json'
content_hash: 'sha256:192fc1821d967abb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDynamicBehavior

<sub>Class</sub>

An object that confers a behavioral configuration on one or more dynamic items, for their participation in 2D animation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIDynamicBehavior
```

## Overview

A _dynamic item_ is any iOS or custom object that conforms to the [UIDynamicItem](uidynamicitem.md) protocol. The [UIView](uiview.md) and [UICollectionViewLayoutAttributes](uicollectionviewlayoutattributes.md) classes implement this protocol starting in iOS 7.0. You can implement this protocol to use a dynamic animator with custom objects for such purposes as reacting to rotation or position changes computed by an animator—an instance of the [UIDynamicAnimator](uidynamicanimator.md) class.

This parent class, [UIDynamicBehavior](uidynamicbehavior.md), is inherited by the primitive dynamic behavior classes [UIAttachmentBehavior](uiattachmentbehavior.md), [UICollisionBehavior](uicollisionbehavior.md), [UIGravityBehavior](uigravitybehavior.md), [UIDynamicItemBehavior](uidynamicitembehavior.md), [UIPushBehavior](uipushbehavior.md), and [UISnapBehavior](uisnapbehavior.md).

You can subclass [UIDynamicBehavior](uidynamicbehavior.md). By using the [- addChildBehavior:](<uidynamicbehavior/addchildbehavior(__).md>) method in an instance of this class or in a custom subclass, you can create composite behaviors of your own design.

When you subclass [UIDynamicBehavior](uidynamicbehavior.md), you typically need to provide one or more initializers, along with other housekeeping methods such as those implemented in the iOS primitive dynamic behaviors.

To perform per-step logic in a dynamic animation, provide a block object using the [action](uidynamicbehavior/action.md) property.

To access the dynamic animator that a dynamic behavior is associated with, use the [dynamicAnimator](uidynamicbehavior/dynamicanimator.md) property. To respond to a dynamic behavior being added to or removed from a dynamic animator, implement the [- willMoveToAnimator:](<uidynamicbehavior/willmove(to_).md>) method.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [UIAttachmentBehavior](uiattachmentbehavior.md), [UICollisionBehavior](uicollisionbehavior.md), [UIDynamicItemBehavior](uidynamicitembehavior.md), [UIFieldBehavior](uifieldbehavior.md), [UIGravityBehavior](uigravitybehavior.md), [UIPushBehavior](uipushbehavior.md), [UISnapBehavior](uisnapbehavior.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Configuring a dynamic behavior

- [action](uidynamicbehavior/action.md) — The block you want to execute during dynamic animation.
- [- addChildBehavior:](<uidynamicbehavior/addchildbehavior(__).md>) — Adds a dynamic behavior, as a child, to a custom dynamic behavior.
- [childBehaviors](uidynamicbehavior/childbehaviors.md) — Returns the array of dynamic behaviors that are children of a custom dynamic behavior.
- [- removeChildBehavior:](<uidynamicbehavior/removechildbehavior(__).md>) — Removes a child dynamic behavior from a custom dynamic behavior.

### Responding to changes in the behavior tree

- [dynamicAnimator](uidynamicbehavior/dynamicanimator.md) — The dynamic animator that the dynamic behavior is associated with.
- [- willMoveToAnimator:](<uidynamicbehavior/willmove(to_).md>) — Called when the dynamic behavior is added to, or removed from, a dynamic animator.

## See Also

### Behaviors

- [UIAttachmentBehavior](uiattachmentbehavior.md) — A relationship between two dynamic items, or between a dynamic item and an anchor point.
- [UICollisionBehavior](uicollisionbehavior.md) — An object that confers to a specified array of dynamic items the ability to engage in collisions with each other and with the behavior’s specified boundaries.
- [UIFieldBehavior](uifieldbehavior.md) — An object that applies field-based physics to dynamic items.
- [UIGravityBehavior](uigravitybehavior.md) — An object that applies a gravity-like force to all of its associated dynamic items.
- [UIPushBehavior](uipushbehavior.md) — A behavior that applies a continuous or instantaneous force to one or more dynamic items, causing those items to change position accordingly.
- [UISnapBehavior](uisnapbehavior.md) — A spring-like behavior whose initial motion is damped over time so that the object settles at a specific point.

---
title: UISnapBehavior
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisnapbehavior
source_url: 'https://developer.apple.com/documentation/uikit/uisnapbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisnapbehavior.json'
content_hash: 'sha256:f92c1423db23d9d9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISnapBehavior

<sub>Class</sub>

A spring-like behavior whose initial motion is damped over time so that the object settles at a specific point.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UISnapBehavior
```

## Overview

A **dynamic item** is any iOS or custom object that conforms to the [UIDynamicItem](uidynamicitem.md) protocol. The [UIView](uiview.md) and [UICollectionViewLayoutAttributes](uicollectionviewlayoutattributes.md) classes implement this protocol starting in iOS 7.0. You can use a custom object as a dynamic item for such purposes as reacting to rotation or position changes computed by a dynamic animator—an instance of the [UIDynamicAnimator](uidynamicanimator.md) class.

To use a snap behavior with a dynamic item, perform these two steps:

1. Initialize a new snap behavior with the item using the [- initWithItem:snapToPoint:](<uisnapbehavior/init(item_snapto_).md>) method
2. Enable the behavior by adding it to an animator using the [- addBehavior:](<uidynamicanimator/addbehavior(__).md>) method

The coordinate system that pertains to a snap behavior, and the types of dynamic items you can use with the behavior, depend on how you initialized the associated animator. For details, read the Overview of [UIDynamicAnimator](uidynamicanimator.md).

You can include a snap behavior in a custom, composite behavior by starting with a [UIDynamicBehavior](uidynamicbehavior.md) object and adding a snap behavior with the [- addChildBehavior:](<uidynamicbehavior/addchildbehavior(__).md>) method.  If you want to influence a snap behavior at each step of a dynamic animation, implement the inherited [action](uidynamicbehavior/action.md) method.

## Relationships

- **Inherits From**: [UIDynamicBehavior](uidynamicbehavior.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializing a snap behavior

- [- initWithItem:snapToPoint:](<uisnapbehavior/init(item_snapto_).md>) — Initializes a snap behavior with a dynamic item and a snap point.

### Configuring a snap behavior

- [snapPoint](uisnapbehavior/snappoint.md) — The point to which to snap.
- [damping](uisnapbehavior/damping.md) — The amount of oscillation of a dynamic item during the conclusion of a snap.

### Initializers

- [init(item:snapToPoint:)](<uisnapbehavior/init(item_snaptopoint_).md>)

## See Also

### Behaviors

- [UIDynamicBehavior](uidynamicbehavior.md) — An object that confers a behavioral configuration on one or more dynamic items, for their participation in 2D animation.
- [UIAttachmentBehavior](uiattachmentbehavior.md) — A relationship between two dynamic items, or between a dynamic item and an anchor point.
- [UICollisionBehavior](uicollisionbehavior.md) — An object that confers to a specified array of dynamic items the ability to engage in collisions with each other and with the behavior’s specified boundaries.
- [UIFieldBehavior](uifieldbehavior.md) — An object that applies field-based physics to dynamic items.
- [UIGravityBehavior](uigravitybehavior.md) — An object that applies a gravity-like force to all of its associated dynamic items.
- [UIPushBehavior](uipushbehavior.md) — A behavior that applies a continuous or instantaneous force to one or more dynamic items, causing those items to change position accordingly.

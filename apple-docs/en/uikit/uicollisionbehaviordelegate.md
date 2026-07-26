---
title: UICollisionBehaviorDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollisionbehaviordelegate
source_url: 'https://developer.apple.com/documentation/uikit/uicollisionbehaviordelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollisionbehaviordelegate.json'
content_hash: 'sha256:1406f3d7496ea8a5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICollisionBehaviorDelegate

<sub>Protocol</sub>

To respond to UIKit dynamic item collisions, configure a custom class to adopt the [UICollisionBehaviorDelegate](uicollisionbehaviordelegate.md) protocol. Then, in a collision behavior (an instance of the [UICollisionBehavior](uicollisionbehavior.md) class), set the delegate to be an instance of your custom class.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UICollisionBehaviorDelegate : NSObjectProtocol
```

## Overview

The delegate is notified of collisions that occur between the behavior’s dynamic items, or between a dynamic item and a boundary, depending on the behavior’s mode (as set with its [collisionMode](uicollisionbehavior/collisionmode.md) property). In the case of a collision between an item and the boundary defined by a reference view, the identifier passed to the delegate method is `nil`. (For more on the reference view and the different ways to initialize a dynamic animator, read the Overview in [UIDynamicAnimator](uidynamicanimator.md).)

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Responding to UIKit Dynamics collisions

- [- collisionBehavior:beganContactForItem:withBoundaryIdentifier:atPoint:](<uicollisionbehaviordelegate/collisionbehavior(__begancontactfor_withboundaryidentifier_at_).md>) — Called when a collision, between a dynamic item and a collision boundary, has begun.
- [- collisionBehavior:beganContactForItem:withItem:atPoint:](<uicollisionbehaviordelegate/collisionbehavior(__begancontactfor_with_at_).md>) — Called when a collision between two dynamic items has begun.
- [- collisionBehavior:endedContactForItem:withBoundaryIdentifier:](<uicollisionbehaviordelegate/collisionbehavior(__endedcontactfor_withboundaryidentifier_).md>) — Called when a collision between a dynamic item and a boundary has ended.
- [- collisionBehavior:endedContactForItem:withItem:](<uicollisionbehaviordelegate/collisionbehavior(__endedcontactfor_with_).md>) — Called when a collision between two dynamic items has ended.

## See Also

### Customizing the collision behavior

- [collisionDelegate](uicollisionbehavior/collisiondelegate.md) — The delegate object that you want to respond to collisions for the collision behavior.

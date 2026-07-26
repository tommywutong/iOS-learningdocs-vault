---
title: 'collisionBehavior(_:beganContactFor:with:at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollisionbehaviordelegate/collisionbehavior(_:begancontactfor:with:at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollisionbehaviordelegate/collisionbehavior(_:begancontactfor:with:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollisionbehaviordelegate/collisionbehavior%28_%3Abegancontactfor%3Awith%3Aat%3A%29.json'
content_hash: 'sha256:0d22ce511d4244d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollisionBehaviorDelegate](../uicollisionbehaviordelegate.md)

# collisionBehavior(_:beganContactFor:with:at:)

<sub>Instance Method</sub>

Called when a collision between two dynamic items has begun.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func collisionBehavior(_ behavior: UICollisionBehavior, beganContactFor item1: any UIDynamicItem, with item2: any UIDynamicItem, at p: CGPoint)
```

## Parameters

- `behavior` — The collision behavior that owns the dynamic items that have started to contact each other.

- `item1` — The first of the two dynamic items participating in the collision.

- `item2` — The second of the two dynamic items participating in the collision.

- `p` — The contact point for the collision. The coordinate system that pertains to a collision depends on how you initialized the associated animator. For details, read the Overview of [UIDynamicAnimator](../uidynamicanimator.md).

## See Also

### Responding to UIKit Dynamics collisions

- [- collisionBehavior:beganContactForItem:withBoundaryIdentifier:atPoint:](<collisionbehavior(__begancontactfor_withboundaryidentifier_at_).md>) — Called when a collision, between a dynamic item and a collision boundary, has begun.
- [- collisionBehavior:endedContactForItem:withBoundaryIdentifier:](<collisionbehavior(__endedcontactfor_withboundaryidentifier_).md>) — Called when a collision between a dynamic item and a boundary has ended.
- [- collisionBehavior:endedContactForItem:withItem:](<collisionbehavior(__endedcontactfor_with_).md>) — Called when a collision between two dynamic items has ended.

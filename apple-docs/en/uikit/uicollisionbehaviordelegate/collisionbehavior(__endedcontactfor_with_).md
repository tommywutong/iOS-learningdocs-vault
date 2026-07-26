---
title: 'collisionBehavior(_:endedContactFor:with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollisionbehaviordelegate/collisionbehavior(_:endedcontactfor:with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollisionbehaviordelegate/collisionbehavior(_:endedcontactfor:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollisionbehaviordelegate/collisionbehavior%28_%3Aendedcontactfor%3Awith%3A%29.json'
content_hash: 'sha256:52323c9c5d0b63c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollisionBehaviorDelegate](../uicollisionbehaviordelegate.md)

# collisionBehavior(_:endedContactFor:with:)

<sub>Instance Method</sub>

Called when a collision between two dynamic items has ended.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func collisionBehavior(_ behavior: UICollisionBehavior, endedContactFor item1: any UIDynamicItem, with item2: any UIDynamicItem)
```

## Parameters

- `behavior` — The collision behavior that owns the dynamic items that collided.

- `item1` — The first of the two dynamic items participating in the collision.

- `item2` — The second of the two dynamic items participating in the collision.

## See Also

### Responding to UIKit Dynamics collisions

- [- collisionBehavior:beganContactForItem:withBoundaryIdentifier:atPoint:](<collisionbehavior(__begancontactfor_withboundaryidentifier_at_).md>) — Called when a collision, between a dynamic item and a collision boundary, has begun.
- [- collisionBehavior:beganContactForItem:withItem:atPoint:](<collisionbehavior(__begancontactfor_with_at_).md>) — Called when a collision between two dynamic items has begun.
- [- collisionBehavior:endedContactForItem:withBoundaryIdentifier:](<collisionbehavior(__endedcontactfor_withboundaryidentifier_).md>) — Called when a collision between a dynamic item and a boundary has ended.

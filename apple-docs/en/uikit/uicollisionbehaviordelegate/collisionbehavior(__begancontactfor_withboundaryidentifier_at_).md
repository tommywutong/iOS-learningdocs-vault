---
title: 'collisionBehavior(_:beganContactFor:withBoundaryIdentifier:at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollisionbehaviordelegate/collisionbehavior(_:begancontactfor:withboundaryidentifier:at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollisionbehaviordelegate/collisionbehavior(_:begancontactfor:withboundaryidentifier:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollisionbehaviordelegate/collisionbehavior%28_%3Abegancontactfor%3Awithboundaryidentifier%3Aat%3A%29.json'
content_hash: 'sha256:92f85ac9219840b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollisionBehaviorDelegate](../uicollisionbehaviordelegate.md)

# collisionBehavior(_:beganContactFor:withBoundaryIdentifier:at:)

<sub>Instance Method</sub>

Called when a collision, between a dynamic item and a collision boundary, has begun.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func collisionBehavior(_ behavior: UICollisionBehavior, beganContactFor item: any UIDynamicItem, withBoundaryIdentifier identifier: (any NSCopying)?, at p: CGPoint)
```

## Parameters

- `behavior` — The collision behavior that owns the dynamic item that has started contact with a boundary.

- `item` — The dynamic item that has started contact with a boundary.

- `identifier` — The identifier of the boundary that the dynamic item has started contact with.

- `p` — The collision point on the boundary.

## See Also

### Responding to UIKit Dynamics collisions

- [- collisionBehavior:beganContactForItem:withItem:atPoint:](<collisionbehavior(__begancontactfor_with_at_).md>) — Called when a collision between two dynamic items has begun.
- [- collisionBehavior:endedContactForItem:withBoundaryIdentifier:](<collisionbehavior(__endedcontactfor_withboundaryidentifier_).md>) — Called when a collision between a dynamic item and a boundary has ended.
- [- collisionBehavior:endedContactForItem:withItem:](<collisionbehavior(__endedcontactfor_with_).md>) — Called when a collision between two dynamic items has ended.

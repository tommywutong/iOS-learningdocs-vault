---
title: 'collisionBehavior(_:endedContactFor:withBoundaryIdentifier:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollisionbehaviordelegate/collisionbehavior(_:endedcontactfor:withboundaryidentifier:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollisionbehaviordelegate/collisionbehavior(_:endedcontactfor:withboundaryidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollisionbehaviordelegate/collisionbehavior%28_%3Aendedcontactfor%3Awithboundaryidentifier%3A%29.json'
content_hash: 'sha256:0fe11faa8337da8f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollisionBehaviorDelegate](../uicollisionbehaviordelegate.md)

# collisionBehavior(_:endedContactFor:withBoundaryIdentifier:)

<sub>Instance Method</sub>

Called when a collision between a dynamic item and a boundary has ended.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func collisionBehavior(_ behavior: UICollisionBehavior, endedContactFor item: any UIDynamicItem, withBoundaryIdentifier identifier: (any NSCopying)?)
```

## Parameters

- `behavior` — The collision behavior that owns the dynamic item that has ended contact.

- `item` — The dynamic item that collided.

- `identifier` — The identifier of the boundary that the dynamic item collided with.

## See Also

### Responding to UIKit Dynamics collisions

- [- collisionBehavior:beganContactForItem:withBoundaryIdentifier:atPoint:](<collisionbehavior(__begancontactfor_withboundaryidentifier_at_).md>) — Called when a collision, between a dynamic item and a collision boundary, has begun.
- [- collisionBehavior:beganContactForItem:withItem:atPoint:](<collisionbehavior(__begancontactfor_with_at_).md>) — Called when a collision between two dynamic items has begun.
- [- collisionBehavior:endedContactForItem:withItem:](<collisionbehavior(__endedcontactfor_with_).md>) — Called when a collision between two dynamic items has ended.

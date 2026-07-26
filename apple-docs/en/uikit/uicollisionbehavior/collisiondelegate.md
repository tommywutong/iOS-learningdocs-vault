---
title: collisionDelegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollisionbehavior/collisiondelegate
source_url: 'https://developer.apple.com/documentation/uikit/uicollisionbehavior/collisiondelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollisionbehavior/collisiondelegate.json'
content_hash: 'sha256:6307808ba30f9434'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollisionBehavior](../uicollisionbehavior.md)

# collisionDelegate

<sub>Instance Property</sub>

The delegate object that you want to respond to collisions for the collision behavior.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var collisionDelegate: (any UICollisionBehaviorDelegate)? { get set }
```

## See Also

### Customizing the collision behavior

- [UICollisionBehaviorDelegate](../uicollisionbehaviordelegate.md) — To respond to UIKit dynamic item collisions, configure a custom class to adopt the [UICollisionBehaviorDelegate](../uicollisionbehaviordelegate.md) protocol. Then, in a collision behavior (an instance of the [UICollisionBehavior](../uicollisionbehavior.md) class), set the delegate to be an instance of your custom class.

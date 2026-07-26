---
title: UIKit Dynamics
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uikit-dynamics
source_url: 'https://developer.apple.com/documentation/uikit/uikit-dynamics'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uikit-dynamics.json'
content_hash: 'sha256:d8539d0054162533'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [Animation and haptics](animation-and-haptics.md)

# UIKit Dynamics

<sub>API Collection</sub>

Apply physics-based animations to your views.

## Topics

### Dynamic animators

- [UIDynamicAnimator](uidynamicanimator.md) — An object that provides physics-related capabilities and animations for its dynamic items, and provides the context for those animations.

### Dynamic items

- [UIDynamicItem](uidynamicitem.md) — A set of methods that can make a custom object eligible to participate in UIKit Dynamics.
- [UIDynamicItemBehavior](uidynamicitembehavior.md) — A base dynamic animation configuration for one or more dynamic items.
- [UIDynamicItemGroup](uidynamicitemgroup.md) — A dynamic item that comprises multiple other dynamic items.

### Behaviors

- [UIDynamicBehavior](uidynamicbehavior.md) — An object that confers a behavioral configuration on one or more dynamic items, for their participation in 2D animation.
- [UIAttachmentBehavior](uiattachmentbehavior.md) — A relationship between two dynamic items, or between a dynamic item and an anchor point.
- [UICollisionBehavior](uicollisionbehavior.md) — An object that confers to a specified array of dynamic items the ability to engage in collisions with each other and with the behavior’s specified boundaries.
- [UIFieldBehavior](uifieldbehavior.md) — An object that applies field-based physics to dynamic items.
- [UIGravityBehavior](uigravitybehavior.md) — An object that applies a gravity-like force to all of its associated dynamic items.
- [UIPushBehavior](uipushbehavior.md) — A behavior that applies a continuous or instantaneous force to one or more dynamic items, causing those items to change position accordingly.
- [UISnapBehavior](uisnapbehavior.md) — A spring-like behavior whose initial motion is damped over time so that the object settles at a specific point.

### Animation regions

- [UIRegion](uiregion.md) — A shape for use in UIKit Dynamics.

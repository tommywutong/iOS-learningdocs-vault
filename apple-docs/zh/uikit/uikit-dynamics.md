---
title: UIKit 动力学
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
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Animation and haptics](animation-and-haptics.md)

# UIKit 动力学

<sub>API 集合</sub>

将基于物理效果的动画应用到你的视图。

## 主题

### 动态动画器

- [UIDynamicAnimator](uidynamicanimator.md) — 一个为其动态项提供物理相关能力与动画、并为这些动画提供上下文的对象。

### 动态项

- [UIDynamicItem](uidynamicitem.md) — 一组方法，可使自定义对象具备参与 UIKit Dynamics 的资格。
- [UIDynamicItemBehavior](uidynamicitembehavior.md) — 面向一个或多个动态项的基础动态动画配置。
- [UIDynamicItemGroup](uidynamicitemgroup.md) — 一个由多个其他动态项组成的动态项。

### 行为

- [UIDynamicBehavior](uidynamicbehavior.md) — 一个对象，为一个或多个动态项赋予行为配置，使其参与 2D 动画。
- [UIAttachmentBehavior](uiattachmentbehavior.md) — 两个动态项之间、或一个动态项与一个锚点之间的关系。
- [UICollisionBehavior](uicollisionbehavior.md) — 一个对象，为指定的一组动态项赋予彼此之间以及与该行为指定边界之间发生碰撞的能力。
- [UIFieldBehavior](uifieldbehavior.md) — 一个对象，将基于场的物理效果应用到动态项。
- [UIGravityBehavior](uigravitybehavior.md) — 一个对象，将类似重力的力应用到其所有关联的动态项。
- [UIPushBehavior](uipushbehavior.md) — 一种行为，将持续或瞬时的力施加到一个或多个动态项，使这些项相应地改变位置。
- [UISnapBehavior](uisnapbehavior.md) — 一种类似弹簧的行为，其初始运动会随时间衰减，使对象最终停在特定点。

### 动画区域

- [UIRegion](uiregion.md) — 一个用于 UIKit Dynamics 的形状。

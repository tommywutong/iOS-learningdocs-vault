---
title: anchorPoint
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiattachmentbehavior/anchorpoint
source_url: 'https://developer.apple.com/documentation/uikit/uiattachmentbehavior/anchorpoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiattachmentbehavior/anchorpoint.json'
content_hash: 'sha256:29701b1be9022b71'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAttachmentBehavior](../uiattachmentbehavior.md)

# anchorPoint

<sub>Instance Property</sub>

The anchor point for the attachment behavior, if any.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var anchorPoint: CGPoint { get set }
```

## Discussion

The anchor point is relative to the coordinate system for the behavior’s associated dynamic animator. For attachment types without an anchor point, the value in this property is [CGPointZero](../../coregraphics/cgpointzero.md). For more information about the coordinate system of the reference view, see [UIDynamicAnimator](../uidynamicanimator.md).

## See Also

### Configuring an attachment behavior

- [attachedBehaviorType](attachedbehaviortype.md) — The type of the attachment behavior.
- [damping](damping.md) — The amount of damping to apply to the attachment behavior.
- [frequency](frequency.md) — The frequency of oscillation for the attachment behavior.
- [length](length.md) — The distance, in points, between the two attachment points of the attachment behavior.
- [frictionTorque](frictiontorque.md) — The amount of force needed to overcome rotational forces around an anchor point.
- [attachmentRange](attachmentrange.md) — The range of motion for the attachment behavior.

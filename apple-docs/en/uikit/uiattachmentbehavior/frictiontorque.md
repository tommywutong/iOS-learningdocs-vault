---
title: frictionTorque
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiattachmentbehavior/frictiontorque
source_url: 'https://developer.apple.com/documentation/uikit/uiattachmentbehavior/frictiontorque'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiattachmentbehavior/frictiontorque.json'
content_hash: 'sha256:3dffaaf7b3a0c13c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAttachmentBehavior](../uiattachmentbehavior.md)

# frictionTorque

<sub>Instance Property</sub>

The amount of force needed to overcome rotational forces around an anchor point.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var frictionTorque: CGFloat { get set }
```

## Discussion

For attachments where each item rotates around an anchor point, use this property to specify the resistance to that rotation. The default value of this property is `0.0`, which causes items to rotate freely with even very small impulses. Higher torque values increase the amount of force needed to cause rotation.

This property has no formal units, so you need to experiment with values to get the behavior that you want.

## See Also

### Configuring an attachment behavior

- [anchorPoint](anchorpoint.md) — The anchor point for the attachment behavior, if any.
- [attachedBehaviorType](attachedbehaviortype.md) — The type of the attachment behavior.
- [damping](damping.md) — The amount of damping to apply to the attachment behavior.
- [frequency](frequency.md) — The frequency of oscillation for the attachment behavior.
- [length](length.md) — The distance, in points, between the two attachment points of the attachment behavior.
- [attachmentRange](attachmentrange.md) — The range of motion for the attachment behavior.

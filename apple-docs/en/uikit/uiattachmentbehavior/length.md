---
title: length
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiattachmentbehavior/length
source_url: 'https://developer.apple.com/documentation/uikit/uiattachmentbehavior/length'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiattachmentbehavior/length.json'
content_hash: 'sha256:d56d20fd2da45ee9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAttachmentBehavior](../uiattachmentbehavior.md)

# length

<sub>Instance Property</sub>

The distance, in points, between the two attachment points of the attachment behavior.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var length: CGFloat { get set }
```

## Discussion

Use this property to adjust the attachment length, if you want to, _after_ creating an attachment. The system sets initial length automatically based on how you initialize the attachment.

## See Also

### Configuring an attachment behavior

- [anchorPoint](anchorpoint.md) — The anchor point for the attachment behavior, if any.
- [attachedBehaviorType](attachedbehaviortype.md) — The type of the attachment behavior.
- [damping](damping.md) — The amount of damping to apply to the attachment behavior.
- [frequency](frequency.md) — The frequency of oscillation for the attachment behavior.
- [frictionTorque](frictiontorque.md) — The amount of force needed to overcome rotational forces around an anchor point.
- [attachmentRange](attachmentrange.md) — The range of motion for the attachment behavior.

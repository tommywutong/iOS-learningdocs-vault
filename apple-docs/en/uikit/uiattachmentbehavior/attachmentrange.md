---
title: attachmentRange
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiattachmentbehavior/attachmentrange
source_url: 'https://developer.apple.com/documentation/uikit/uiattachmentbehavior/attachmentrange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiattachmentbehavior/attachmentrange.json'
content_hash: 'sha256:e499f76549875f94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAttachmentBehavior](../uiattachmentbehavior.md)

# attachmentRange

<sub>Instance Property</sub>

The range of motion for the attachment behavior.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var attachmentRange: UIFloatRange { get set }
```

## Discussion

For sliding attachments, this property defines the range of motion (measured in points) supported along the given axis of translation. The specified range must always contain the value 0, which represents the starting point of movement for items. Items slide along the axis between the minimum and maximum values you specify. Setting this property to [UIFloatRangeZero](../uifloatrange/zero.md) prevents items from sliding at all along their axis of translation.

For pin attachments, this property defines the amount of rotation (measured in radians) supported in the counter-clockwise and clockwise directions. The specified range must contain the value `0`, which represents the starting angle of each item. Items rotate around the anchor point between the minimum and maximum values you specify. Setting this property to [UIFloatRangeZero](../uifloatrange/zero.md) prevents items from rotating at all.

The default value of this property is [UIFloatRangeInfinite](../uifloatrange/infinite.md).

## See Also

### Configuring an attachment behavior

- [anchorPoint](anchorpoint.md) — The anchor point for the attachment behavior, if any.
- [attachedBehaviorType](attachedbehaviortype.md) — The type of the attachment behavior.
- [damping](damping.md) — The amount of damping to apply to the attachment behavior.
- [frequency](frequency.md) — The frequency of oscillation for the attachment behavior.
- [length](length.md) — The distance, in points, between the two attachment points of the attachment behavior.
- [frictionTorque](frictiontorque.md) — The amount of force needed to overcome rotational forces around an anchor point.

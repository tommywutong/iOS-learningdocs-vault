---
title: UIAttachmentBehavior
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiattachmentbehavior
source_url: 'https://developer.apple.com/documentation/uikit/uiattachmentbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiattachmentbehavior.json'
content_hash: 'sha256:13b7d4648bfd124a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIAttachmentBehavior

<sub>Class</sub>

A relationship between two dynamic items, or between a dynamic item and an anchor point.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIAttachmentBehavior
```

## Overview

When two items are attached to each other, forces imparted on one item affect the movement of the other in a prescribed way. When an item is attached to an anchor point, the movement of that item is affected by its attachment to the specified anchor point. Some attachment behaviors support both two items and an anchor point.

You specify type of attachment behavior you want at creation time. This class offers many creation and initialization methods, each of which creates a different type of attachment behavior, which cannot be changed later. However, you may change specific attributes of the attachment behavior using the properties of this class. For example, you can change the distance between two attached items or change the damping forces applied to the items.

### Applying an Attachment Behavior to Dynamic Items

To apply an attachment behavior to your dynamic items, do the following:

1. Create the attachment behavior using one of the creation or initialization methods. The method you choose defines the relationship between the items and the anchor point (if any).
2. Enable the attachment behavior by adding it to your [UIDynamicAnimator](uidynamicanimator.md) object using the [- addBehavior:](<uidynamicanimator/addbehavior(__).md>) method. Do not add the same attachment behavior to multiple animator objects.

The attachment behavior derives its coordinate system from the reference view of its associated dynamic animator object. For more information about the dynamic animator and the reference coordinate system, see [UIDynamicAnimator](uidynamicanimator.md).

## Relationships

- **Inherits From**: [UIDynamicBehavior](uidynamicbehavior.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating and initializing attachment behavior objects

- [+ slidingAttachmentWithItem:attachmentAnchor:axisOfTranslation:](<uiattachmentbehavior/slidingattachment(with_attachmentanchor_axisoftranslation_).md>) — Creates and returns an attachment behavior where one item slides along the specified axis.
- [+ slidingAttachmentWithItem:attachedToItem:attachmentAnchor:axisOfTranslation:](<uiattachmentbehavior/slidingattachment(with_attachedto_attachmentanchor_axisoftranslation_).md>) — Creates and returns an attachment behavior where two items are fixed to points that slide along the specified axis.
- [+ fixedAttachmentWithItem:attachedToItem:attachmentAnchor:](<uiattachmentbehavior/fixedattachment(with_attachedto_attachmentanchor_).md>) — Creates and returns an attachment behavior where the two items are fixed together through the specified anchor point.
- [+ limitAttachmentWithItem:offsetFromCenter:attachedToItem:offsetFromCenter:](<uiattachmentbehavior/limitattachment(with_offsetfromcenter_attachedto_offsetfromcenter_).md>) — Creates and returns an attachment behavior object where two items are constrained by a maximum distance from one another.
- [+ pinAttachmentWithItem:attachedToItem:attachmentAnchor:](<uiattachmentbehavior/pinattachment(with_attachedto_attachmentanchor_).md>) — Creates and returns an attachment behavior where the two items are pinned to, and move around, an anchor point
- [- initWithItem:attachedToAnchor:](<uiattachmentbehavior/init(item_attachedtoanchor_).md>) — Initializes a behavior where the center of a dynamic item is attached to the specified anchor point.
- [- initWithItem:attachedToItem:](<uiattachmentbehavior/init(item_attachedto_).md>) — Initializes a behavior where the centers of two dynamic items are attached to each other.
- [- initWithItem:offsetFromCenter:attachedToAnchor:](<uiattachmentbehavior/init(item_offsetfromcenter_attachedtoanchor_).md>) — Initializes a behavior where the specified point in a dynamic item is attached to an anchor point.
- [- initWithItem:offsetFromCenter:attachedToItem:offsetFromCenter:](<uiattachmentbehavior/init(item_offsetfromcenter_attachedto_offsetfromcenter_).md>) — Initializes an attachment behavior that connects a specified point in one dynamic item to a specified point in another dynamic item.

### Getting the attached items

- [items](uiattachmentbehavior/items.md) — The dynamic items connected by the attachment behavior.

### Configuring an attachment behavior

- [anchorPoint](uiattachmentbehavior/anchorpoint.md) — The anchor point for the attachment behavior, if any.
- [attachedBehaviorType](uiattachmentbehavior/attachedbehaviortype.md) — The type of the attachment behavior.
- [damping](uiattachmentbehavior/damping.md) — The amount of damping to apply to the attachment behavior.
- [frequency](uiattachmentbehavior/frequency.md) — The frequency of oscillation for the attachment behavior.
- [length](uiattachmentbehavior/length.md) — The distance, in points, between the two attachment points of the attachment behavior.
- [frictionTorque](uiattachmentbehavior/frictiontorque.md) — The amount of force needed to overcome rotational forces around an anchor point.
- [attachmentRange](uiattachmentbehavior/attachmentrange.md) — The range of motion for the attachment behavior.

### Constants

- [AttachmentType](uiattachmentbehavior/attachmenttype.md) — Constants indicating the type of the attachment behavior object.
- [UIFloatRange](uifloatrange.md) — The range of motion for attached objects.
- [Float range constants](float-range-constants.md) — Constants for specifying standard ranges.
- [UIOffset](uioffset.md) — A structure that specifies an amount to offset a position.

### Initializers

- [init(item:attachedToItem:)](<uiattachmentbehavior/init(item_attachedtoitem_).md>)
- [init(item:offsetFromCenter:attachedToItem:offsetFromCenter:)](<uiattachmentbehavior/init(item_offsetfromcenter_attachedtoitem_offsetfromcenter_).md>)

## See Also

### Behaviors

- [UIDynamicBehavior](uidynamicbehavior.md) — An object that confers a behavioral configuration on one or more dynamic items, for their participation in 2D animation.
- [UICollisionBehavior](uicollisionbehavior.md) — An object that confers to a specified array of dynamic items the ability to engage in collisions with each other and with the behavior’s specified boundaries.
- [UIFieldBehavior](uifieldbehavior.md) — An object that applies field-based physics to dynamic items.
- [UIGravityBehavior](uigravitybehavior.md) — An object that applies a gravity-like force to all of its associated dynamic items.
- [UIPushBehavior](uipushbehavior.md) — A behavior that applies a continuous or instantaneous force to one or more dynamic items, causing those items to change position accordingly.
- [UISnapBehavior](uisnapbehavior.md) — A spring-like behavior whose initial motion is damped over time so that the object settles at a specific point.

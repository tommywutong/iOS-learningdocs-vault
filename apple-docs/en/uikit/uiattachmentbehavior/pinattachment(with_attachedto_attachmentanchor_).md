---
title: 'pinAttachment(with:attachedTo:attachmentAnchor:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiattachmentbehavior/pinattachment(with:attachedto:attachmentanchor:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiattachmentbehavior/pinattachment(with:attachedto:attachmentanchor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiattachmentbehavior/pinattachment%28with%3Aattachedto%3Aattachmentanchor%3A%29.json'
content_hash: 'sha256:234a482ec3c2c123'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAttachmentBehavior](../uiattachmentbehavior.md)

# pinAttachment(with:attachedTo:attachmentAnchor:)

<sub>Type Method</sub>

Creates and returns an attachment behavior where the two items are pinned to, and move around, an anchor point

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func pinAttachment(with item1: any UIDynamicItem, attachedTo item2: any UIDynamicItem, attachmentAnchor point: CGPoint) -> Self
```

## Parameters

- `item1` — The first of two dynamic items connected by the attachment behavior.

- `item2` — The second of two dynamic items connected by the attachment behavior.

- `point` — The initial anchor point for each item. Specify this point in the coordinate system of the dynamic animator’s reference view. For more information about coordinate systems, see [UIDynamicAnimator](../uidynamicanimator.md).

## Return Value

A new attachment object or `nil` if the object could not be created.

## Discussion

The behavior created by this method acts like a solid rod connecting each item to the specified anchor point. Each item is free to rotate around the anchor point, inscribing a circle whose radius is the defined at creation time by the distance between `point` and the item’s center. When forces act on one or both items, the anchor point and other item also move accordingly. The anchor point of the attachment does not interact with collision boundaries.

Use the [frictionTorque](frictiontorque.md) property to control the rotational behavior of the items. When the value of that property is `0`, items rotate freely in response to almost any impulse. Adding torque increases the amount of force that must be applied to an item before it rotates.

Use the [attachmentRange](attachmentrange.md) property to limit the amount of rotation for each item. This property lets you specify the minimum and maximum amount of rotation of the items from their starting positions.

## See Also

### Creating and initializing attachment behavior objects

- [+ slidingAttachmentWithItem:attachmentAnchor:axisOfTranslation:](<slidingattachment(with_attachmentanchor_axisoftranslation_).md>) — Creates and returns an attachment behavior where one item slides along the specified axis.
- [+ slidingAttachmentWithItem:attachedToItem:attachmentAnchor:axisOfTranslation:](<slidingattachment(with_attachedto_attachmentanchor_axisoftranslation_).md>) — Creates and returns an attachment behavior where two items are fixed to points that slide along the specified axis.
- [+ fixedAttachmentWithItem:attachedToItem:attachmentAnchor:](<fixedattachment(with_attachedto_attachmentanchor_).md>) — Creates and returns an attachment behavior where the two items are fixed together through the specified anchor point.
- [+ limitAttachmentWithItem:offsetFromCenter:attachedToItem:offsetFromCenter:](<limitattachment(with_offsetfromcenter_attachedto_offsetfromcenter_).md>) — Creates and returns an attachment behavior object where two items are constrained by a maximum distance from one another.
- [- initWithItem:attachedToAnchor:](<init(item_attachedtoanchor_).md>) — Initializes a behavior where the center of a dynamic item is attached to the specified anchor point.
- [- initWithItem:attachedToItem:](<init(item_attachedto_).md>) — Initializes a behavior where the centers of two dynamic items are attached to each other.
- [- initWithItem:offsetFromCenter:attachedToAnchor:](<init(item_offsetfromcenter_attachedtoanchor_).md>) — Initializes a behavior where the specified point in a dynamic item is attached to an anchor point.
- [- initWithItem:offsetFromCenter:attachedToItem:offsetFromCenter:](<init(item_offsetfromcenter_attachedto_offsetfromcenter_).md>) — Initializes an attachment behavior that connects a specified point in one dynamic item to a specified point in another dynamic item.

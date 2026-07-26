---
title: 'limitAttachment(with:offsetFromCenter:attachedTo:offsetFromCenter:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiattachmentbehavior/limitattachment(with:offsetfromcenter:attachedto:offsetfromcenter:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiattachmentbehavior/limitattachment(with:offsetfromcenter:attachedto:offsetfromcenter:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiattachmentbehavior/limitattachment%28with%3Aoffsetfromcenter%3Aattachedto%3Aoffsetfromcenter%3A%29.json'
content_hash: 'sha256:1fd06db80764857d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAttachmentBehavior](../uiattachmentbehavior.md)

# limitAttachment(with:offsetFromCenter:attachedTo:offsetFromCenter:)

<sub>Type Method</sub>

Creates and returns an attachment behavior object where two items are constrained by a maximum distance from one another.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func limitAttachment(with item1: any UIDynamicItem, offsetFromCenter offset1: UIOffset, attachedTo item2: any UIDynamicItem, offsetFromCenter offset2: UIOffset) -> Self
```

## Parameters

- `item1` — The first of two dynamic items connected by the attachment behavior.

- `offset1` — The offset from the center of `item1` that corresponds to the attachment point. Use an offset value to create rotational torque on the item. To pull the item from its center, specify [UIOffsetZero](../uioffset/zero.md).

- `item2` — The second of two dynamic items connected by the attachment behavior.

- `offset2` — The offset from the center of `item2` that corresponds to the attachment point. Use an offset value to create rotational torque on the item. To pull the item from its center, specify [UIOffsetZero](../uioffset/zero.md).

## Return Value

A new attachment object or `nil` if the object could not be created.

## Discussion

The behavior created by this method is like connecting two items with a rope. The only constraint between the items is the maximum distance between them, which corresponds to the moment when the rope is taut. At other times, the objects move freely relative to one another.

The initial maximum distance between the items is set using the current position of the items. You can change the maximum distance by modifying the [length](length.md) property.

## See Also

### Creating and initializing attachment behavior objects

- [+ slidingAttachmentWithItem:attachmentAnchor:axisOfTranslation:](<slidingattachment(with_attachmentanchor_axisoftranslation_).md>) — Creates and returns an attachment behavior where one item slides along the specified axis.
- [+ slidingAttachmentWithItem:attachedToItem:attachmentAnchor:axisOfTranslation:](<slidingattachment(with_attachedto_attachmentanchor_axisoftranslation_).md>) — Creates and returns an attachment behavior where two items are fixed to points that slide along the specified axis.
- [+ fixedAttachmentWithItem:attachedToItem:attachmentAnchor:](<fixedattachment(with_attachedto_attachmentanchor_).md>) — Creates and returns an attachment behavior where the two items are fixed together through the specified anchor point.
- [+ pinAttachmentWithItem:attachedToItem:attachmentAnchor:](<pinattachment(with_attachedto_attachmentanchor_).md>) — Creates and returns an attachment behavior where the two items are pinned to, and move around, an anchor point
- [- initWithItem:attachedToAnchor:](<init(item_attachedtoanchor_).md>) — Initializes a behavior where the center of a dynamic item is attached to the specified anchor point.
- [- initWithItem:attachedToItem:](<init(item_attachedto_).md>) — Initializes a behavior where the centers of two dynamic items are attached to each other.
- [- initWithItem:offsetFromCenter:attachedToAnchor:](<init(item_offsetfromcenter_attachedtoanchor_).md>) — Initializes a behavior where the specified point in a dynamic item is attached to an anchor point.
- [- initWithItem:offsetFromCenter:attachedToItem:offsetFromCenter:](<init(item_offsetfromcenter_attachedto_offsetfromcenter_).md>) — Initializes an attachment behavior that connects a specified point in one dynamic item to a specified point in another dynamic item.

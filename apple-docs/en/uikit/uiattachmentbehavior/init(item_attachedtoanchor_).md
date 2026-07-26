---
title: 'init(item:attachedToAnchor:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiattachmentbehavior/init(item:attachedtoanchor:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiattachmentbehavior/init(item:attachedtoanchor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiattachmentbehavior/init%28item%3Aattachedtoanchor%3A%29.json'
content_hash: 'sha256:095054d85a5f0609'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAttachmentBehavior](../uiattachmentbehavior.md)

# init(item:attachedToAnchor:)

<sub>Initializer</sub>

Initializes a behavior where the center of a dynamic item is attached to the specified anchor point.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(item: any UIDynamicItem, attachedToAnchor point: CGPoint)
```

## Parameters

- `item` — The dynamic item to attach to the specified `point`.

- `point` — The anchor point for the item. Specify this point in the coordinate system of the dynamic animator’s reference view. For more information about coordinate systems, see [UIDynamicAnimator](../uidynamicanimator.md).

## Return Value

The initialized attachment behavior, or `nil` if there was a problem initializing the object.

## Discussion

The behavior created by this method acts like a solid rod connecting the item to the specified anchor point. The item is free to rotate around the anchor point, but its distance to the anchor point remains fixed.

The attachment object returned by this method is of type [UIAttachmentBehaviorTypeAnchor](attachmenttype/anchor.md).

## See Also

### Creating and initializing attachment behavior objects

- [+ slidingAttachmentWithItem:attachmentAnchor:axisOfTranslation:](<slidingattachment(with_attachmentanchor_axisoftranslation_).md>) — Creates and returns an attachment behavior where one item slides along the specified axis.
- [+ slidingAttachmentWithItem:attachedToItem:attachmentAnchor:axisOfTranslation:](<slidingattachment(with_attachedto_attachmentanchor_axisoftranslation_).md>) — Creates and returns an attachment behavior where two items are fixed to points that slide along the specified axis.
- [+ fixedAttachmentWithItem:attachedToItem:attachmentAnchor:](<fixedattachment(with_attachedto_attachmentanchor_).md>) — Creates and returns an attachment behavior where the two items are fixed together through the specified anchor point.
- [+ limitAttachmentWithItem:offsetFromCenter:attachedToItem:offsetFromCenter:](<limitattachment(with_offsetfromcenter_attachedto_offsetfromcenter_).md>) — Creates and returns an attachment behavior object where two items are constrained by a maximum distance from one another.
- [+ pinAttachmentWithItem:attachedToItem:attachmentAnchor:](<pinattachment(with_attachedto_attachmentanchor_).md>) — Creates and returns an attachment behavior where the two items are pinned to, and move around, an anchor point
- [- initWithItem:attachedToItem:](<init(item_attachedto_).md>) — Initializes a behavior where the centers of two dynamic items are attached to each other.
- [- initWithItem:offsetFromCenter:attachedToAnchor:](<init(item_offsetfromcenter_attachedtoanchor_).md>) — Initializes a behavior where the specified point in a dynamic item is attached to an anchor point.
- [- initWithItem:offsetFromCenter:attachedToItem:offsetFromCenter:](<init(item_offsetfromcenter_attachedto_offsetfromcenter_).md>) — Initializes an attachment behavior that connects a specified point in one dynamic item to a specified point in another dynamic item.

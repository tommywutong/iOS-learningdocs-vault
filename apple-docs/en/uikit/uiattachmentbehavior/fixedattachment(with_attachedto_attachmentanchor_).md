---
title: 'fixedAttachment(with:attachedTo:attachmentAnchor:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiattachmentbehavior/fixedattachment(with:attachedto:attachmentanchor:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiattachmentbehavior/fixedattachment(with:attachedto:attachmentanchor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiattachmentbehavior/fixedattachment%28with%3Aattachedto%3Aattachmentanchor%3A%29.json'
content_hash: 'sha256:d3d7e359d384705f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAttachmentBehavior](../uiattachmentbehavior.md)

# fixedAttachment(with:attachedTo:attachmentAnchor:)

<sub>Type Method</sub>

Creates and returns an attachment behavior where the two items are fixed together through the specified anchor point.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func fixedAttachment(with item1: any UIDynamicItem, attachedTo item2: any UIDynamicItem, attachmentAnchor point: CGPoint) -> Self
```

## Parameters

- `item1` — The first of two dynamic items connected by the attachment behavior.

- `item2` — The second of two dynamic items connected by the attachment behavior.

- `point` — The anchor point for both items. Specify this point in the coordinate system of the dynamic animator’s reference view. For more information about coordinate systems, see [UIDynamicAnimator](../uidynamicanimator.md).

## Return Value

A new attachment object or `nil` if the object could not be created.

## Discussion

The behavior created by this method acts like a solid rod connecting each item to the specified anchor point. The position of the items relative to each other does not change. Forces acting on the items move them together as if they were a single unit.

## See Also

### Creating and initializing attachment behavior objects

- [+ slidingAttachmentWithItem:attachmentAnchor:axisOfTranslation:](<slidingattachment(with_attachmentanchor_axisoftranslation_).md>) — Creates and returns an attachment behavior where one item slides along the specified axis.
- [+ slidingAttachmentWithItem:attachedToItem:attachmentAnchor:axisOfTranslation:](<slidingattachment(with_attachedto_attachmentanchor_axisoftranslation_).md>) — Creates and returns an attachment behavior where two items are fixed to points that slide along the specified axis.
- [+ limitAttachmentWithItem:offsetFromCenter:attachedToItem:offsetFromCenter:](<limitattachment(with_offsetfromcenter_attachedto_offsetfromcenter_).md>) — Creates and returns an attachment behavior object where two items are constrained by a maximum distance from one another.
- [+ pinAttachmentWithItem:attachedToItem:attachmentAnchor:](<pinattachment(with_attachedto_attachmentanchor_).md>) — Creates and returns an attachment behavior where the two items are pinned to, and move around, an anchor point
- [- initWithItem:attachedToAnchor:](<init(item_attachedtoanchor_).md>) — Initializes a behavior where the center of a dynamic item is attached to the specified anchor point.
- [- initWithItem:attachedToItem:](<init(item_attachedto_).md>) — Initializes a behavior where the centers of two dynamic items are attached to each other.
- [- initWithItem:offsetFromCenter:attachedToAnchor:](<init(item_offsetfromcenter_attachedtoanchor_).md>) — Initializes a behavior where the specified point in a dynamic item is attached to an anchor point.
- [- initWithItem:offsetFromCenter:attachedToItem:offsetFromCenter:](<init(item_offsetfromcenter_attachedto_offsetfromcenter_).md>) — Initializes an attachment behavior that connects a specified point in one dynamic item to a specified point in another dynamic item.

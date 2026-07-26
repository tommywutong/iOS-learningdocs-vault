---
title: 'init(item:offsetFromCenter:attachedTo:offsetFromCenter:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiattachmentbehavior/init(item:offsetfromcenter:attachedto:offsetfromcenter:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiattachmentbehavior/init(item:offsetfromcenter:attachedto:offsetfromcenter:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiattachmentbehavior/init%28item%3Aoffsetfromcenter%3Aattachedto%3Aoffsetfromcenter%3A%29.json'
content_hash: 'sha256:bb3ba93c552ff37e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAttachmentBehavior](../uiattachmentbehavior.md)

# init(item:offsetFromCenter:attachedTo:offsetFromCenter:)

<sub>Initializer</sub>

Initializes an attachment behavior that connects a specified point in one dynamic item to a specified point in another dynamic item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(item item1: any UIDynamicItem, offsetFromCenter offset1: UIOffset, attachedTo item2: any UIDynamicItem, offsetFromCenter offset2: UIOffset)
```

## Parameters

- `item1` — The first of two dynamic items connected by the attachment behavior.

- `offset1` — The offset from the center of `item1` at which to create the attachment. Specifying [UIOffsetZero](../uioffset/zero.md) creates the attachment at the center of `item1`.

- `item2` — The second of two dynamic items connected by the attachment behavior.

- `offset2` — The offset from the center of `item2` at which to create the attachment. Specifying [UIOffsetZero](../uioffset/zero.md) creates the attachment at the center of `item2`.

## Return Value

The initialized attachment behavior, or `nil` if there was a problem initializing the object.

## Discussion

The behavior created by this method acts like a solid rod connecting the two items at the specified offsets from their center points. Forces applied to one item push or pull the other item accordingly. The items are free to rotate around each other but always remain the same distance apart.

The attachment object returned by this method is of type [UIAttachmentBehaviorTypeItems](attachmenttype/items.md).

## See Also

### Creating and initializing attachment behavior objects

- [+ slidingAttachmentWithItem:attachmentAnchor:axisOfTranslation:](<slidingattachment(with_attachmentanchor_axisoftranslation_).md>) — Creates and returns an attachment behavior where one item slides along the specified axis.
- [+ slidingAttachmentWithItem:attachedToItem:attachmentAnchor:axisOfTranslation:](<slidingattachment(with_attachedto_attachmentanchor_axisoftranslation_).md>) — Creates and returns an attachment behavior where two items are fixed to points that slide along the specified axis.
- [+ fixedAttachmentWithItem:attachedToItem:attachmentAnchor:](<fixedattachment(with_attachedto_attachmentanchor_).md>) — Creates and returns an attachment behavior where the two items are fixed together through the specified anchor point.
- [+ limitAttachmentWithItem:offsetFromCenter:attachedToItem:offsetFromCenter:](<limitattachment(with_offsetfromcenter_attachedto_offsetfromcenter_).md>) — Creates and returns an attachment behavior object where two items are constrained by a maximum distance from one another.
- [+ pinAttachmentWithItem:attachedToItem:attachmentAnchor:](<pinattachment(with_attachedto_attachmentanchor_).md>) — Creates and returns an attachment behavior where the two items are pinned to, and move around, an anchor point
- [- initWithItem:attachedToAnchor:](<init(item_attachedtoanchor_).md>) — Initializes a behavior where the center of a dynamic item is attached to the specified anchor point.
- [- initWithItem:attachedToItem:](<init(item_attachedto_).md>) — Initializes a behavior where the centers of two dynamic items are attached to each other.
- [- initWithItem:offsetFromCenter:attachedToAnchor:](<init(item_offsetfromcenter_attachedtoanchor_).md>) — Initializes a behavior where the specified point in a dynamic item is attached to an anchor point.

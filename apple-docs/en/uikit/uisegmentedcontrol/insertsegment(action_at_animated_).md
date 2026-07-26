---
title: 'insertSegment(action:at:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisegmentedcontrol/insertsegment(action:at:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisegmentedcontrol/insertsegment(action:at:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisegmentedcontrol/insertsegment%28action%3Aat%3Aanimated%3A%29.json'
content_hash: 'sha256:420be0127bcef7d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISegmentedControl](../uisegmentedcontrol.md)

# insertSegment(action:at:animated:)

<sub>Instance Method</sub>

Insert a segment with the action you specify at the given index.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func insertSegment(action: UIAction, at segment: Int, animated: Bool)
```

## Parameters

- `action` — A [UIAction](../uiaction.md) object to set on the segment at the index you specify.

- `segment` — An unsigned integer index of a segment.

- `animated` — [true](../../swift/true.md) if the insertion of the new segment animates; otherwise, [false](../../swift/false.md).

## Discussion

Segments prefer images over titles when the action contains both. Selecting a segment invokes the action’s [UIActionHandler](../uiactionhandler.md), as well as handlers for the [UIControlEventValueChanged](../uicontrol/event/valuechanged.md) and [UIControlEventPrimaryActionTriggered](../uicontrol/event/primaryactiontriggered.md) control events.

If a segment exists with the action’s identifier, this method updates the existing segment is if the index is the same or removes the segment if the index is different.

## See Also

### Managing segments

- [numberOfSegments](numberofsegments.md) — Returns the number of segments the segmented control has.
- [- segmentIndexForActionIdentifier:](<segmentindex(identifiedby_).md>) — The index of a segment with an action that has an identifier matching the identifier you specify.
- [- insertSegmentWithImage:atIndex:animated:](<insertsegment(with_at_animated_).md>) — Inserts a segment at the position you specify and gives it an image as content.
- [- insertSegmentWithTitle:atIndex:animated:](<insertsegment(withtitle_at_animated_).md>) — Inserts a segment at the position you specify and gives it a title as content.
- [- removeAllSegments](<removeallsegments().md>) — Removes all segments of the segmented control.
- [- removeSegmentAtIndex:animated:](<removesegment(at_animated_).md>) — Removes the segment you specify from the segmented control, optionally animating the transition.
- [selectedSegmentIndex](selectedsegmentindex.md) — The index number that identifies the selected segment that the user last touched.
- [UISegmentedControlNoSegment](nosegment.md) — A segment index value indicating that there’s no selected segment.

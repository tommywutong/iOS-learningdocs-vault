---
title: selectedSegmentIndex
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisegmentedcontrol/selectedsegmentindex
source_url: 'https://developer.apple.com/documentation/uikit/uisegmentedcontrol/selectedsegmentindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisegmentedcontrol/selectedsegmentindex.json'
content_hash: 'sha256:7b10cceeb364eadf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISegmentedControl](../uisegmentedcontrol.md)

# selectedSegmentIndex

<sub>Instance Property</sub>

The index number that identifies the selected segment that the user last touched.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var selectedSegmentIndex: Int { get set }
```

## Discussion

The default value is [UISegmentedControlNoSegment](nosegment.md) (no segment selected) until the user touches a segment. Set this property to `-1` to turn off the current selection. [UISegmentedControl](../uisegmentedcontrol.md) ignores this property when [momentary](ismomentary.md) is [true](../../swift/true.md). When the user touches a segment to change the selection, the system generates the control event [UIControlEventValueChanged](../uicontrol/event/valuechanged.md). If you set up the segmented control to respond to this control event, it sends an action message to its target.

## See Also

### Managing segments

- [numberOfSegments](numberofsegments.md) — Returns the number of segments the segmented control has.
- [- segmentIndexForActionIdentifier:](<segmentindex(identifiedby_).md>) — The index of a segment with an action that has an identifier matching the identifier you specify.
- [- insertSegmentWithAction:atIndex:animated:](<insertsegment(action_at_animated_).md>) — Insert a segment with the action you specify at the given index.
- [- insertSegmentWithImage:atIndex:animated:](<insertsegment(with_at_animated_).md>) — Inserts a segment at the position you specify and gives it an image as content.
- [- insertSegmentWithTitle:atIndex:animated:](<insertsegment(withtitle_at_animated_).md>) — Inserts a segment at the position you specify and gives it a title as content.
- [- removeAllSegments](<removeallsegments().md>) — Removes all segments of the segmented control.
- [- removeSegmentAtIndex:animated:](<removesegment(at_animated_).md>) — Removes the segment you specify from the segmented control, optionally animating the transition.
- [UISegmentedControlNoSegment](nosegment.md) — A segment index value indicating that there’s no selected segment.

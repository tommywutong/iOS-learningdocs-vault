---
title: noSegment
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisegmentedcontrol/nosegment
source_url: 'https://developer.apple.com/documentation/uikit/uisegmentedcontrol/nosegment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisegmentedcontrol/nosegment.json'
content_hash: 'sha256:5d0b8e3b752d966a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISegmentedControl](../uisegmentedcontrol.md)

# noSegment

<sub>Type Property</sub>

A segment index value indicating that there’s no selected segment.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class var noSegment: Int { get }
```

## Discussion

See [selectedSegmentIndex](selectedsegmentindex.md) for more information.

## See Also

### Managing segments

- [numberOfSegments](numberofsegments.md) — Returns the number of segments the segmented control has.
- [- segmentIndexForActionIdentifier:](<segmentindex(identifiedby_).md>) — The index of a segment with an action that has an identifier matching the identifier you specify.
- [- insertSegmentWithAction:atIndex:animated:](<insertsegment(action_at_animated_).md>) — Insert a segment with the action you specify at the given index.
- [- insertSegmentWithImage:atIndex:animated:](<insertsegment(with_at_animated_).md>) — Inserts a segment at the position you specify and gives it an image as content.
- [- insertSegmentWithTitle:atIndex:animated:](<insertsegment(withtitle_at_animated_).md>) — Inserts a segment at the position you specify and gives it a title as content.
- [- removeAllSegments](<removeallsegments().md>) — Removes all segments of the segmented control.
- [- removeSegmentAtIndex:animated:](<removesegment(at_animated_).md>) — Removes the segment you specify from the segmented control, optionally animating the transition.
- [selectedSegmentIndex](selectedsegmentindex.md) — The index number that identifies the selected segment that the user last touched.

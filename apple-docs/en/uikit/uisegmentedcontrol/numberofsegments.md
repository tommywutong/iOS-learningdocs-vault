---
title: numberOfSegments
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisegmentedcontrol/numberofsegments
source_url: 'https://developer.apple.com/documentation/uikit/uisegmentedcontrol/numberofsegments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisegmentedcontrol/numberofsegments.json'
content_hash: 'sha256:85082213f7ddd840'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISegmentedControl](../uisegmentedcontrol.md)

# numberOfSegments

<sub>Instance Property</sub>

Returns the number of segments the segmented control has.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var numberOfSegments: Int { get }
```

## See Also

### Managing segments

- [- segmentIndexForActionIdentifier:](<segmentindex(identifiedby_).md>) — The index of a segment with an action that has an identifier matching the identifier you specify.
- [- insertSegmentWithAction:atIndex:animated:](<insertsegment(action_at_animated_).md>) — Insert a segment with the action you specify at the given index.
- [- insertSegmentWithImage:atIndex:animated:](<insertsegment(with_at_animated_).md>) — Inserts a segment at the position you specify and gives it an image as content.
- [- insertSegmentWithTitle:atIndex:animated:](<insertsegment(withtitle_at_animated_).md>) — Inserts a segment at the position you specify and gives it a title as content.
- [- removeAllSegments](<removeallsegments().md>) — Removes all segments of the segmented control.
- [- removeSegmentAtIndex:animated:](<removesegment(at_animated_).md>) — Removes the segment you specify from the segmented control, optionally animating the transition.
- [selectedSegmentIndex](selectedsegmentindex.md) — The index number that identifies the selected segment that the user last touched.
- [UISegmentedControlNoSegment](nosegment.md) — A segment index value indicating that there’s no selected segment.

---
title: 'insertSegment(withTitle:at:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisegmentedcontrol/insertsegment(withtitle:at:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisegmentedcontrol/insertsegment(withtitle:at:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisegmentedcontrol/insertsegment%28withtitle%3Aat%3Aanimated%3A%29.json'
content_hash: 'sha256:9924418529947294'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISegmentedControl](../uisegmentedcontrol.md)

# insertSegment(withTitle:at:animated:)

<sub>Instance Method</sub>

Inserts a segment at the position you specify and gives it a title as content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func insertSegment(withTitle title: String?, at segment: Int, animated: Bool)
```

## Parameters

- `title` — A string to use as the segment’s title.

- `segment` — An index number identifying a segment in the control. `segment` must be a number in the range 0 to the number of segments ([numberOfSegments](numberofsegments.md)) inclusive; the segmented control pins values exceeding this upper range to the last segment. The method inserts the new segment just before the designated one.

- `animated` — [true](../../swift/true.md) if the insertion of the new segment must be animated, otherwise [false](../../swift/false.md).

## See Also

### Managing segments

- [numberOfSegments](numberofsegments.md) — Returns the number of segments the segmented control has.
- [- segmentIndexForActionIdentifier:](<segmentindex(identifiedby_).md>) — The index of a segment with an action that has an identifier matching the identifier you specify.
- [- insertSegmentWithAction:atIndex:animated:](<insertsegment(action_at_animated_).md>) — Insert a segment with the action you specify at the given index.
- [- insertSegmentWithImage:atIndex:animated:](<insertsegment(with_at_animated_).md>) — Inserts a segment at the position you specify and gives it an image as content.
- [- removeAllSegments](<removeallsegments().md>) — Removes all segments of the segmented control.
- [- removeSegmentAtIndex:animated:](<removesegment(at_animated_).md>) — Removes the segment you specify from the segmented control, optionally animating the transition.
- [selectedSegmentIndex](selectedsegmentindex.md) — The index number that identifies the selected segment that the user last touched.
- [UISegmentedControlNoSegment](nosegment.md) — A segment index value indicating that there’s no selected segment.

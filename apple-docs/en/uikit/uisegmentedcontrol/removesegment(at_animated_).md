---
title: 'removeSegment(at:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisegmentedcontrol/removesegment(at:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisegmentedcontrol/removesegment(at:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisegmentedcontrol/removesegment%28at%3Aanimated%3A%29.json'
content_hash: 'sha256:def005e95f8e0d39'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISegmentedControl](../uisegmentedcontrol.md)

# removeSegment(at:animated:)

<sub>Instance Method</sub>

Removes the segment you specify from the segmented control, optionally animating the transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func removeSegment(at segment: Int, animated: Bool)
```

## Parameters

- `segment` — An index number identifying a segment in the control. It must be a number between 0 and the number of segments ([numberOfSegments](numberofsegments.md)) minus 1; the segmented control pins values exceeding this upper range to the last segment.

- `animated` — [true](../../swift/true.md) if the removal of the new segment must animate; otherwise, [false](../../swift/false.md).

## See Also

### Managing segments

- [numberOfSegments](numberofsegments.md) — Returns the number of segments the segmented control has.
- [- segmentIndexForActionIdentifier:](<segmentindex(identifiedby_).md>) — The index of a segment with an action that has an identifier matching the identifier you specify.
- [- insertSegmentWithAction:atIndex:animated:](<insertsegment(action_at_animated_).md>) — Insert a segment with the action you specify at the given index.
- [- insertSegmentWithImage:atIndex:animated:](<insertsegment(with_at_animated_).md>) — Inserts a segment at the position you specify and gives it an image as content.
- [- insertSegmentWithTitle:atIndex:animated:](<insertsegment(withtitle_at_animated_).md>) — Inserts a segment at the position you specify and gives it a title as content.
- [- removeAllSegments](<removeallsegments().md>) — Removes all segments of the segmented control.
- [selectedSegmentIndex](selectedsegmentindex.md) — The index number that identifies the selected segment that the user last touched.
- [UISegmentedControlNoSegment](nosegment.md) — A segment index value indicating that there’s no selected segment.

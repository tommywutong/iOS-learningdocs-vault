---
title: 'segmentIndex(identifiedBy:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisegmentedcontrol/segmentindex(identifiedby:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisegmentedcontrol/segmentindex(identifiedby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisegmentedcontrol/segmentindex%28identifiedby%3A%29.json'
content_hash: 'sha256:70dd26320b2fa458'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISegmentedControl](../uisegmentedcontrol.md)

# segmentIndex(identifiedBy:)

<sub>Instance Method</sub>

The index of a segment with an action that has an identifier matching the identifier you specify.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func segmentIndex(identifiedBy actionIdentifier: UIAction.Identifier) -> Int
```

## Parameters

- `actionIdentifier` — The [Identifier](../uiaction/identifier-swift.struct.md) to match.

## Return Value

The index of the segment with an action that has a matching identifier, or [NSNotFound](../../foundation/nsnotfound-4qp9h.md) if no matching action is found.

## See Also

### Managing segments

- [numberOfSegments](numberofsegments.md) — Returns the number of segments the segmented control has.
- [- insertSegmentWithAction:atIndex:animated:](<insertsegment(action_at_animated_).md>) — Insert a segment with the action you specify at the given index.
- [- insertSegmentWithImage:atIndex:animated:](<insertsegment(with_at_animated_).md>) — Inserts a segment at the position you specify and gives it an image as content.
- [- insertSegmentWithTitle:atIndex:animated:](<insertsegment(withtitle_at_animated_).md>) — Inserts a segment at the position you specify and gives it a title as content.
- [- removeAllSegments](<removeallsegments().md>) — Removes all segments of the segmented control.
- [- removeSegmentAtIndex:animated:](<removesegment(at_animated_).md>) — Removes the segment you specify from the segmented control, optionally animating the transition.
- [selectedSegmentIndex](selectedsegmentindex.md) — The index number that identifies the selected segment that the user last touched.
- [UISegmentedControlNoSegment](nosegment.md) — A segment index value indicating that there’s no selected segment.

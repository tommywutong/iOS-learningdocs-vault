---
title: 'setContentOffset(_:forSegmentAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisegmentedcontrol/setcontentoffset(_:forsegmentat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisegmentedcontrol/setcontentoffset(_:forsegmentat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisegmentedcontrol/setcontentoffset%28_%3Aforsegmentat%3A%29.json'
content_hash: 'sha256:16a06b26572fca9a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISegmentedControl](../uisegmentedcontrol.md)

# setContentOffset(_:forSegmentAt:)

<sub>Instance Method</sub>

Adjusts the offset for drawing the content (image or text) of the specified segment.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setContentOffset(_ offset: CGSize, forSegmentAt segment: Int)
```

## Parameters

- `offset` — The offset (as a [CGSize](../../corefoundation/cgsize.md) type) from the origin of the segment at which to draw the segment’s content. The default offset is (0,0).

- `segment` — An index number identifying a segment in the control. It must be a number between 0 and the number of segments ([numberOfSegments](numberofsegments.md)) minus 1; the segmented control pins values exceeding this upper range to the last segment.

## See Also

### Managing segment behavior and appearance

- [momentary](ismomentary.md) — A Boolean value that determines whether segments in the segmented control show selected state.
- [- setEnabled:forSegmentAtIndex:](<setenabled(__forsegmentat_).md>) — Enables the segment you specify.
- [- isEnabledForSegmentAtIndex:](<isenabledforsegment(at_).md>) — Returns whether the indicated segment is enabled.
- [- contentOffsetForSegmentAtIndex:](<contentoffsetforsegment(at_).md>) — Returns the offset for drawing the content (image or text) of the segment you specify.
- [- setWidth:forSegmentAtIndex:](<setwidth(__forsegmentat_).md>) — Sets the width of the segment at the index you specify.
- [- widthForSegmentAtIndex:](<widthforsegment(at_).md>) — Returns the width of the segment at the index you specify.
- [apportionsSegmentWidthsByContent](apportionssegmentwidthsbycontent.md) — Indicates whether the control attempts to adjust segment widths based on their content widths.

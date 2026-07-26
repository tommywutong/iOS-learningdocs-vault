---
title: 'setWidth(_:forSegmentAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisegmentedcontrol/setwidth(_:forsegmentat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisegmentedcontrol/setwidth(_:forsegmentat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisegmentedcontrol/setwidth%28_%3Aforsegmentat%3A%29.json'
content_hash: 'sha256:382863eaef2d69d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISegmentedControl](../uisegmentedcontrol.md)

# setWidth(_:forSegmentAt:)

<sub>Instance Method</sub>

Sets the width of the segment at the index you specify.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setWidth(_ width: CGFloat, forSegmentAt segment: Int)
```

## Parameters

- `width` — A float value specifying the width of the segment. The default value is {0.0}, which tells `UISegmentedControl` to automatically size the segment.

- `segment` — An index number identifying a segment in the control. It must be a number between 0 and the number of segments ([numberOfSegments](numberofsegments.md)) minus 1; the segmented control pins values exceeding this upper range to the last segment.

## See Also

### Managing segment behavior and appearance

- [momentary](ismomentary.md) — A Boolean value that determines whether segments in the segmented control show selected state.
- [- setEnabled:forSegmentAtIndex:](<setenabled(__forsegmentat_).md>) — Enables the segment you specify.
- [- isEnabledForSegmentAtIndex:](<isenabledforsegment(at_).md>) — Returns whether the indicated segment is enabled.
- [- setContentOffset:forSegmentAtIndex:](<setcontentoffset(__forsegmentat_).md>) — Adjusts the offset for drawing the content (image or text) of the specified segment.
- [- contentOffsetForSegmentAtIndex:](<contentoffsetforsegment(at_).md>) — Returns the offset for drawing the content (image or text) of the segment you specify.
- [- widthForSegmentAtIndex:](<widthforsegment(at_).md>) — Returns the width of the segment at the index you specify.
- [apportionsSegmentWidthsByContent](apportionssegmentwidthsbycontent.md) — Indicates whether the control attempts to adjust segment widths based on their content widths.

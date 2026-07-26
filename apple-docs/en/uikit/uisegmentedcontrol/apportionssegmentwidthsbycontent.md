---
title: apportionsSegmentWidthsByContent
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisegmentedcontrol/apportionssegmentwidthsbycontent
source_url: 'https://developer.apple.com/documentation/uikit/uisegmentedcontrol/apportionssegmentwidthsbycontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisegmentedcontrol/apportionssegmentwidthsbycontent.json'
content_hash: 'sha256:dcd7ff88be86115f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISegmentedControl](../uisegmentedcontrol.md)

# apportionsSegmentWidthsByContent

<sub>Instance Property</sub>

Indicates whether the control attempts to adjust segment widths based on their content widths.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var apportionsSegmentWidthsByContent: Bool { get set }
```

## Discussion

If the value of this property is [true](../../swift/true.md), for segments whose width value is `0`, the control attempts to adjust segment widths based on their content widths.

The default is [false](../../swift/false.md).

## See Also

### Managing segment behavior and appearance

- [momentary](ismomentary.md) — A Boolean value that determines whether segments in the segmented control show selected state.
- [- setEnabled:forSegmentAtIndex:](<setenabled(__forsegmentat_).md>) — Enables the segment you specify.
- [- isEnabledForSegmentAtIndex:](<isenabledforsegment(at_).md>) — Returns whether the indicated segment is enabled.
- [- setContentOffset:forSegmentAtIndex:](<setcontentoffset(__forsegmentat_).md>) — Adjusts the offset for drawing the content (image or text) of the specified segment.
- [- contentOffsetForSegmentAtIndex:](<contentoffsetforsegment(at_).md>) — Returns the offset for drawing the content (image or text) of the segment you specify.
- [- setWidth:forSegmentAtIndex:](<setwidth(__forsegmentat_).md>) — Sets the width of the segment at the index you specify.
- [- widthForSegmentAtIndex:](<widthforsegment(at_).md>) — Returns the width of the segment at the index you specify.

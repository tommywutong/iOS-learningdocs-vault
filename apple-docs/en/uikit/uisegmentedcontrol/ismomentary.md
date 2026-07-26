---
title: isMomentary
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisegmentedcontrol/ismomentary
source_url: 'https://developer.apple.com/documentation/uikit/uisegmentedcontrol/ismomentary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisegmentedcontrol/ismomentary.json'
content_hash: 'sha256:797a91c1311ad792'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISegmentedControl](../uisegmentedcontrol.md)

# isMomentary

<sub>Instance Property</sub>

A Boolean value that determines whether segments in the segmented control show selected state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isMomentary: Bool { get set }
```

## Discussion

The default value of this property is [false](../../swift/false.md). If it’s set to [true](../../swift/true.md), segments in the control don’t show selected state and don’t update the value of [selectedSegmentIndex](selectedsegmentindex.md) after tracking ends.

## See Also

### Managing segment behavior and appearance

- [- setEnabled:forSegmentAtIndex:](<setenabled(__forsegmentat_).md>) — Enables the segment you specify.
- [- isEnabledForSegmentAtIndex:](<isenabledforsegment(at_).md>) — Returns whether the indicated segment is enabled.
- [- setContentOffset:forSegmentAtIndex:](<setcontentoffset(__forsegmentat_).md>) — Adjusts the offset for drawing the content (image or text) of the specified segment.
- [- contentOffsetForSegmentAtIndex:](<contentoffsetforsegment(at_).md>) — Returns the offset for drawing the content (image or text) of the segment you specify.
- [- setWidth:forSegmentAtIndex:](<setwidth(__forsegmentat_).md>) — Sets the width of the segment at the index you specify.
- [- widthForSegmentAtIndex:](<widthforsegment(at_).md>) — Returns the width of the segment at the index you specify.
- [apportionsSegmentWidthsByContent](apportionssegmentwidthsbycontent.md) — Indicates whether the control attempts to adjust segment widths based on their content widths.

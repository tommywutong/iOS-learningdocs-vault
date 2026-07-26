---
title: segmentedControlStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（7.0 起废弃）, iPadOS 2.0+（7.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uisegmentedcontrol/segmentedcontrolstyle
source_url: 'https://developer.apple.com/documentation/uikit/uisegmentedcontrol/segmentedcontrolstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisegmentedcontrol/segmentedcontrolstyle.json'
content_hash: 'sha256:f08000cb19f0c295'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISegmentedControl](../uisegmentedcontrol.md)

# segmentedControlStyle

<sub>Instance Property</sub>

The style of the segmented control.

> [!warning] Deprecated
> Segmented controls no longer support multiple styles using this functionality. Use the other appearance modification methods and properties to customize a segmented control.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic) UISegmentedControlStyle segmentedControlStyle;
```

## Discussion

The default style is [UISegmentedControlStylePlain](../uisegmentedcontrolstyle/uisegmentedcontrolstyleplain.md). See [UISegmentedControlStyle](../uisegmentedcontrolstyle.md) for descriptions of valid constants.

## See Also

### Managing segment behavior and appearance

- [momentary](ismomentary.md) — A Boolean value that determines whether segments in the segmented control show selected state.
- [- setEnabled:forSegmentAtIndex:](<setenabled(__forsegmentat_).md>) — Enables the segment you specify.
- [- isEnabledForSegmentAtIndex:](<isenabledforsegment(at_).md>) — Returns whether the indicated segment is enabled.
- [- setContentOffset:forSegmentAtIndex:](<setcontentoffset(__forsegmentat_).md>) — Adjusts the offset for drawing the content (image or text) of the specified segment.
- [- contentOffsetForSegmentAtIndex:](<contentoffsetforsegment(at_).md>) — Returns the offset for drawing the content (image or text) of the segment you specify.
- [- setWidth:forSegmentAtIndex:](<setwidth(__forsegmentat_).md>) — Sets the width of the segment at the index you specify.
- [- widthForSegmentAtIndex:](<widthforsegment(at_).md>) — Returns the width of the segment at the index you specify.
- [apportionsSegmentWidthsByContent](apportionssegmentwidthsbycontent.md) — Indicates whether the control attempts to adjust segment widths based on their content widths.
- [UISegmentedControlStyle](../uisegmentedcontrolstyle.md) — The styles of the segmented control. _(deprecated)_

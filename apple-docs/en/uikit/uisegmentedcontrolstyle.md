---
title: UISegmentedControlStyle
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+（7.0 起废弃）, iPadOS 2.0+（7.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uisegmentedcontrolstyle
source_url: 'https://developer.apple.com/documentation/uikit/uisegmentedcontrolstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisegmentedcontrolstyle.json'
content_hash: 'sha256:d49f1515b6b0cefd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISegmentedControlStyle

<sub>Enumeration</sub>

The styles of the segmented control.

> [!warning] Deprecated
> Segmented controls no longer support multiple styles using this functionality. Use the other appearance modification methods and properties to customize a segmented control.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
enum UISegmentedControlStyle : NSInteger;
```

## Overview

You use these constants as values for the [segmentedControlStyle](uisegmentedcontrol/segmentedcontrolstyle.md) property.

## Topics

### Constants

- [UISegmentedControlStylePlain](uisegmentedcontrolstyle/uisegmentedcontrolstyleplain.md) — The large plain style for segmented controls. _(deprecated)_
- [UISegmentedControlStyleBordered](uisegmentedcontrolstyle/uisegmentedcontrolstylebordered.md) — The large bordered style for segmented controls. _(deprecated)_
- [UISegmentedControlStyleBar](uisegmentedcontrolstyle/uisegmentedcontrolstylebar.md) — The small toolbar style for segmented controls. _(deprecated)_
- [UISegmentedControlStyleBezeled](uisegmentedcontrolstyle/uisegmentedcontrolstylebezeled.md) — The large bezeled style for segmented controls. _(deprecated)_

## See Also

### Managing segment behavior and appearance

- [momentary](uisegmentedcontrol/ismomentary.md) — A Boolean value that determines whether segments in the segmented control show selected state.
- [- setEnabled:forSegmentAtIndex:](<uisegmentedcontrol/setenabled(__forsegmentat_).md>) — Enables the segment you specify.
- [- isEnabledForSegmentAtIndex:](<uisegmentedcontrol/isenabledforsegment(at_).md>) — Returns whether the indicated segment is enabled.
- [- setContentOffset:forSegmentAtIndex:](<uisegmentedcontrol/setcontentoffset(__forsegmentat_).md>) — Adjusts the offset for drawing the content (image or text) of the specified segment.
- [- contentOffsetForSegmentAtIndex:](<uisegmentedcontrol/contentoffsetforsegment(at_).md>) — Returns the offset for drawing the content (image or text) of the segment you specify.
- [- setWidth:forSegmentAtIndex:](<uisegmentedcontrol/setwidth(__forsegmentat_).md>) — Sets the width of the segment at the index you specify.
- [- widthForSegmentAtIndex:](<uisegmentedcontrol/widthforsegment(at_).md>) — Returns the width of the segment at the index you specify.
- [apportionsSegmentWidthsByContent](uisegmentedcontrol/apportionssegmentwidthsbycontent.md) — Indicates whether the control attempts to adjust segment widths based on their content widths.
- [segmentedControlStyle](uisegmentedcontrol/segmentedcontrolstyle.md) — The style of the segmented control. _(deprecated)_

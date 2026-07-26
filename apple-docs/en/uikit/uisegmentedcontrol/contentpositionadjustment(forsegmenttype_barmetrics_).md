---
title: 'contentPositionAdjustment(forSegmentType:barMetrics:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisegmentedcontrol/contentpositionadjustment(forsegmenttype:barmetrics:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisegmentedcontrol/contentpositionadjustment(forsegmenttype:barmetrics:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisegmentedcontrol/contentpositionadjustment%28forsegmenttype%3Abarmetrics%3A%29.json'
content_hash: 'sha256:87597226fb186a99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISegmentedControl](../uisegmentedcontrol.md)

# contentPositionAdjustment(forSegmentType:barMetrics:)

<sub>Instance Method</sub>

Returns the positioning offset for a given segment and bar metrics.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func contentPositionAdjustment(forSegmentType leftCenterRightOrAlone: UISegmentedControl.Segment, barMetrics: UIBarMetrics) -> UIOffset
```

## Parameters

- `leftCenterRightOrAlone` — An identifier for a segment.

- `barMetrics` — Bar metrics.

## Return Value

The content positioning offset for the segment identified by `leftCenterRightOrAlone` and `barMetrics`.

## Discussion

For more details, see [- setContentPositionAdjustment:forSegmentType:barMetrics:](<setcontentpositionadjustment(__forsegmenttype_barmetrics_).md>).

## See Also

### Customizing appearance

- [selectedSegmentTintColor](selectedsegmenttintcolor.md) — The color to use for highlighting the currently selected segment.
- [- backgroundImageForState:barMetrics:](<backgroundimage(for_barmetrics_).md>) — Returns the background image for a given state and bar metrics.
- [- setBackgroundImage:forState:barMetrics:](<setbackgroundimage(__for_barmetrics_).md>) — Sets the background image for given state and bar metrics.
- [- setContentPositionAdjustment:forSegmentType:barMetrics:](<setcontentpositionadjustment(__forsegmenttype_barmetrics_).md>) — Sets the content positioning offset for a given segment and bar metrics.
- [Segment](segment.md) — Constants for specifying a segment in a control.
- [- dividerImageForLeftSegmentState:rightSegmentState:barMetrics:](<dividerimage(forleftsegmentstate_rightsegmentstate_barmetrics_).md>) — Returns the divider image used for a given combination of left and right segment states and bar metrics.
- [- setDividerImage:forLeftSegmentState:rightSegmentState:barMetrics:](<setdividerimage(__forleftsegmentstate_rightsegmentstate_barmetrics_).md>) — Sets the divider image to use for a given combination of left and right segment states and bar metrics.
- [- titleTextAttributesForState:](<titletextattributes(for_).md>) — Returns the text attributes of the title for a given control state.
- [- setTitleTextAttributes:forState:](<settitletextattributes(__for_).md>) — Sets the text attributes of the title for a given control state.

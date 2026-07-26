---
title: 'setDividerImage(_:forLeftSegmentState:rightSegmentState:barMetrics:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisegmentedcontrol/setdividerimage(_:forleftsegmentstate:rightsegmentstate:barmetrics:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisegmentedcontrol/setdividerimage(_:forleftsegmentstate:rightsegmentstate:barmetrics:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisegmentedcontrol/setdividerimage%28_%3Aforleftsegmentstate%3Arightsegmentstate%3Abarmetrics%3A%29.json'
content_hash: 'sha256:236d90dd47720bde'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISegmentedControl](../uisegmentedcontrol.md)

# setDividerImage(_:forLeftSegmentState:rightSegmentState:barMetrics:)

<sub>Instance Method</sub>

Sets the divider image to use for a given combination of left and right segment states and bar metrics.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setDividerImage(_ dividerImage: UIImage?, forLeftSegmentState leftState: UIControl.State, rightSegmentState rightState: UIControl.State, barMetrics: UIBarMetrics)
```

## Parameters

- `dividerImage` — The divider image to use.

- `leftState` — The state of the left segment.

- `rightState` — The state of the right segment.

- `barMetrics` — Bar metrics.

## Discussion

To customize the segmented control appearance, provide divider images for the following cases:

- Between two unselected segments, where `leftState` and `rightState` are both [UIControlStateNormal](../uicontrol/state-swift.struct/normal.md)
- Between a selected segment on the left and an unselected on the right, where `leftState` is [UIControlStateSelected](../uicontrol/state-swift.struct/selected.md) and `rightState` is [UIControlStateNormal](../uicontrol/state-swift.struct/normal.md)
- Between an unselected segment on the left and a selected on the right, where `leftState` is [UIControlStateNormal](../uicontrol/state-swift.struct/normal.md) and `rightState` is [UIControlStateSelected](../uicontrol/state-swift.struct/selected.md)

## See Also

### Customizing appearance

- [selectedSegmentTintColor](selectedsegmenttintcolor.md) — The color to use for highlighting the currently selected segment.
- [- backgroundImageForState:barMetrics:](<backgroundimage(for_barmetrics_).md>) — Returns the background image for a given state and bar metrics.
- [- setBackgroundImage:forState:barMetrics:](<setbackgroundimage(__for_barmetrics_).md>) — Sets the background image for given state and bar metrics.
- [- contentPositionAdjustmentForSegmentType:barMetrics:](<contentpositionadjustment(forsegmenttype_barmetrics_).md>) — Returns the positioning offset for a given segment and bar metrics.
- [- setContentPositionAdjustment:forSegmentType:barMetrics:](<setcontentpositionadjustment(__forsegmenttype_barmetrics_).md>) — Sets the content positioning offset for a given segment and bar metrics.
- [Segment](segment.md) — Constants for specifying a segment in a control.
- [- dividerImageForLeftSegmentState:rightSegmentState:barMetrics:](<dividerimage(forleftsegmentstate_rightsegmentstate_barmetrics_).md>) — Returns the divider image used for a given combination of left and right segment states and bar metrics.
- [- titleTextAttributesForState:](<titletextattributes(for_).md>) — Returns the text attributes of the title for a given control state.
- [- setTitleTextAttributes:forState:](<settitletextattributes(__for_).md>) — Sets the text attributes of the title for a given control state.

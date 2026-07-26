---
title: 'setBackgroundImage(_:for:barMetrics:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisegmentedcontrol/setbackgroundimage(_:for:barmetrics:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisegmentedcontrol/setbackgroundimage(_:for:barmetrics:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisegmentedcontrol/setbackgroundimage%28_%3Afor%3Abarmetrics%3A%29.json'
content_hash: 'sha256:5096ad4c6dcffb80'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISegmentedControl](../uisegmentedcontrol.md)

# setBackgroundImage(_:for:barMetrics:)

<sub>Instance Method</sub>

Sets the background image for given state and bar metrics.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setBackgroundImage(_ backgroundImage: UIImage?, for state: UIControl.State, barMetrics: UIBarMetrics)
```

## Parameters

- `backgroundImage` — The background image to use for `state` and `barMetrics`.

- `state` — A control state.

- `barMetrics` — Bar metrics.

## Discussion

If `backgroundImage` is an image that [- resizableImageWithCapInsets:](<../uiimage/resizableimage(withcapinsets_).md>) returns, the system calculates the cap widths from that information.

If `backgroundImage` isn’t an image that [- resizableImageWithCapInsets:](<../uiimage/resizableimage(withcapinsets_).md>) returns, the system calculates the cap width by subtracting one from the image’s width, then dividing by 2. The system uses the cap widths as the margins for text placement. To adjust the margin, use the margin adjustment methods.

Generally, specify a value for the [UIControlStateNormal](../uicontrol/state-swift.struct/normal.md) state. The segmented control uses this state for other states that don’t have a custom value set.

Similarly, when a property is dependent on the bar metrics, be sure to specify a value for [UIBarMetricsDefault](../uibarmetrics/default.md). The segmented control respects properties for [UIBarMetricsCompact](../uibarmetrics/compact.md) only when the control is in smaller navigation and toolbars.

## See Also

### Customizing appearance

- [selectedSegmentTintColor](selectedsegmenttintcolor.md) — The color to use for highlighting the currently selected segment.
- [- backgroundImageForState:barMetrics:](<backgroundimage(for_barmetrics_).md>) — Returns the background image for a given state and bar metrics.
- [- contentPositionAdjustmentForSegmentType:barMetrics:](<contentpositionadjustment(forsegmenttype_barmetrics_).md>) — Returns the positioning offset for a given segment and bar metrics.
- [- setContentPositionAdjustment:forSegmentType:barMetrics:](<setcontentpositionadjustment(__forsegmenttype_barmetrics_).md>) — Sets the content positioning offset for a given segment and bar metrics.
- [Segment](segment.md) — Constants for specifying a segment in a control.
- [- dividerImageForLeftSegmentState:rightSegmentState:barMetrics:](<dividerimage(forleftsegmentstate_rightsegmentstate_barmetrics_).md>) — Returns the divider image used for a given combination of left and right segment states and bar metrics.
- [- setDividerImage:forLeftSegmentState:rightSegmentState:barMetrics:](<setdividerimage(__forleftsegmentstate_rightsegmentstate_barmetrics_).md>) — Sets the divider image to use for a given combination of left and right segment states and bar metrics.
- [- titleTextAttributesForState:](<titletextattributes(for_).md>) — Returns the text attributes of the title for a given control state.
- [- setTitleTextAttributes:forState:](<settitletextattributes(__for_).md>) — Sets the text attributes of the title for a given control state.

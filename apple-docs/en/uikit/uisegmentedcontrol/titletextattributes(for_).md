---
title: 'titleTextAttributes(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisegmentedcontrol/titletextattributes(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisegmentedcontrol/titletextattributes(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisegmentedcontrol/titletextattributes%28for%3A%29.json'
content_hash: 'sha256:d29d4338532e22bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISegmentedControl](../uisegmentedcontrol.md)

# titleTextAttributes(for:)

<sub>Instance Method</sub>

Returns the text attributes of the title for a given control state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func titleTextAttributes(for state: UIControl.State) -> [NSAttributedString.Key : Any]?
```

## Parameters

- `state` — A control state.

## Return Value

The text attributes of the title for `state`.

## Discussion

For more details, see [- setTitleTextAttributes:forState:](<settitletextattributes(__for_).md>)

## See Also

### Customizing appearance

- [selectedSegmentTintColor](selectedsegmenttintcolor.md) — The color to use for highlighting the currently selected segment.
- [- backgroundImageForState:barMetrics:](<backgroundimage(for_barmetrics_).md>) — Returns the background image for a given state and bar metrics.
- [- setBackgroundImage:forState:barMetrics:](<setbackgroundimage(__for_barmetrics_).md>) — Sets the background image for given state and bar metrics.
- [- contentPositionAdjustmentForSegmentType:barMetrics:](<contentpositionadjustment(forsegmenttype_barmetrics_).md>) — Returns the positioning offset for a given segment and bar metrics.
- [- setContentPositionAdjustment:forSegmentType:barMetrics:](<setcontentpositionadjustment(__forsegmenttype_barmetrics_).md>) — Sets the content positioning offset for a given segment and bar metrics.
- [Segment](segment.md) — Constants for specifying a segment in a control.
- [- dividerImageForLeftSegmentState:rightSegmentState:barMetrics:](<dividerimage(forleftsegmentstate_rightsegmentstate_barmetrics_).md>) — Returns the divider image used for a given combination of left and right segment states and bar metrics.
- [- setDividerImage:forLeftSegmentState:rightSegmentState:barMetrics:](<setdividerimage(__forleftsegmentstate_rightsegmentstate_barmetrics_).md>) — Sets the divider image to use for a given combination of left and right segment states and bar metrics.
- [- setTitleTextAttributes:forState:](<settitletextattributes(__for_).md>) — Sets the text attributes of the title for a given control state.

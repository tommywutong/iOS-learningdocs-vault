---
title: UISegmentedControl.Segment
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisegmentedcontrol/segment
source_url: 'https://developer.apple.com/documentation/uikit/uisegmentedcontrol/segment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisegmentedcontrol/segment.json'
content_hash: 'sha256:d54cd6ac52da2850'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISegmentedControl](../uisegmentedcontrol.md)

# UISegmentedControl.Segment

<sub>Enumeration</sub>

Constants for specifying a segment in a control.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum Segment
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UISegmentedControlSegmentAny](segment/any.md) — Specifies any segment.
- [UISegmentedControlSegmentLeft](segment/left.md) — The capped, leftmost segment.
- [UISegmentedControlSegmentCenter](segment/center.md) — Any segment between the left and rightmost segments.
- [UISegmentedControlSegmentRight](segment/right.md) — The capped, rightmost segment.
- [UISegmentedControlSegmentAlone](segment/alone.md) — The standalone segment, capped on both ends.

### Initializers

- [init(rawValue:)](<segment/init(rawvalue_).md>)

## See Also

### Customizing appearance

- [selectedSegmentTintColor](selectedsegmenttintcolor.md) — The color to use for highlighting the currently selected segment.
- [- backgroundImageForState:barMetrics:](<backgroundimage(for_barmetrics_).md>) — Returns the background image for a given state and bar metrics.
- [- setBackgroundImage:forState:barMetrics:](<setbackgroundimage(__for_barmetrics_).md>) — Sets the background image for given state and bar metrics.
- [- contentPositionAdjustmentForSegmentType:barMetrics:](<contentpositionadjustment(forsegmenttype_barmetrics_).md>) — Returns the positioning offset for a given segment and bar metrics.
- [- setContentPositionAdjustment:forSegmentType:barMetrics:](<setcontentpositionadjustment(__forsegmenttype_barmetrics_).md>) — Sets the content positioning offset for a given segment and bar metrics.
- [- dividerImageForLeftSegmentState:rightSegmentState:barMetrics:](<dividerimage(forleftsegmentstate_rightsegmentstate_barmetrics_).md>) — Returns the divider image used for a given combination of left and right segment states and bar metrics.
- [- setDividerImage:forLeftSegmentState:rightSegmentState:barMetrics:](<setdividerimage(__forleftsegmentstate_rightsegmentstate_barmetrics_).md>) — Sets the divider image to use for a given combination of left and right segment states and bar metrics.
- [- titleTextAttributesForState:](<titletextattributes(for_).md>) — Returns the text attributes of the title for a given control state.
- [- setTitleTextAttributes:forState:](<settitletextattributes(__for_).md>) — Sets the text attributes of the title for a given control state.

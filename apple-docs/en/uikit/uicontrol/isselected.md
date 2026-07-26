---
title: isSelected
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontrol/isselected
source_url: 'https://developer.apple.com/documentation/uikit/uicontrol/isselected'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontrol/isselected.json'
content_hash: 'sha256:345e1a2e90f83781'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIControl](../uicontrol.md)

# isSelected

<sub>Instance Property</sub>

A Boolean value indicating whether the control is in the selected state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isSelected: Bool { get set }
```

## Discussion

Set the value of this property to [true](../../swift/true.md) to select it or [false](../../swift/false.md) to deselect it. Most controls don’t modify their appearance or behavior when selected, but some do. For example, the [UISegmentedControl](../uisegmentedcontrol.md) class tracks whether a segment is selected and draws it differently when it is.

The default value of this property is [false](../../swift/false.md) for a newly created control. You can set a control’s initial selected state in your storyboard file.

## See Also

### Managing state

- [state](state-swift.property.md) — The state of the control, specified as a bit mask value.
- [State](state-swift.struct.md) — Constants describing the state of a control.
- [enabled](isenabled.md) — A Boolean value indicating whether the control is in the enabled state.
- [highlighted](ishighlighted.md) — A Boolean value indicating whether the control draws a highlight.

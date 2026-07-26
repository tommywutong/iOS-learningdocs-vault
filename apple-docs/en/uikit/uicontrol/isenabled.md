---
title: isEnabled
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontrol/isenabled
source_url: 'https://developer.apple.com/documentation/uikit/uicontrol/isenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontrol/isenabled.json'
content_hash: 'sha256:aa5c3531e1af3257'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIControl](../uicontrol.md)

# isEnabled

<sub>Instance Property</sub>

A Boolean value indicating whether the control is in the enabled state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isEnabled: Bool { get set }
```

## Discussion

Set the value of this property to [true](../../swift/true.md) to enable the control or [false](../../swift/false.md) to disable it. An enabled control is capable of responding to user interactions, whereas a disabled control ignores touch events and may draw itself differently. Setting this property to [false](../../swift/false.md) adds the [UIControlStateDisabled](state-swift.struct/disabled.md) flag to the control’s [state](state-swift.property.md) bitmask; enabling the control again removes that flag.

The default value of this property is [true](../../swift/true.md) for a newly created control. You can set a control’s initial enabled state in your storyboard file.

## See Also

### Managing state

- [state](state-swift.property.md) — The state of the control, specified as a bit mask value.
- [State](state-swift.struct.md) — Constants describing the state of a control.
- [selected](isselected.md) — A Boolean value indicating whether the control is in the selected state.
- [highlighted](ishighlighted.md) — A Boolean value indicating whether the control draws a highlight.

---
title: state
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontrol/state-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uicontrol/state-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontrol/state-swift.property.json'
content_hash: 'sha256:6254e91c2fb2d9b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIControl](../uicontrol.md)

# state

<sub>Instance Property</sub>

The state of the control, specified as a bit mask value.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var state: UIControl.State { get }
```

## Discussion

The value of this property is a bitmask of the constants in the [State](state-swift.struct.md) type. A control can be in more than one state at a time. For example, it can be focused and highlighted at the same time. You can also get the values for individual states using the properties of this class.

## See Also

### Managing state

- [State](state-swift.struct.md) — Constants describing the state of a control.
- [enabled](isenabled.md) — A Boolean value indicating whether the control is in the enabled state.
- [selected](isselected.md) — A Boolean value indicating whether the control is in the selected state.
- [highlighted](ishighlighted.md) — A Boolean value indicating whether the control draws a highlight.

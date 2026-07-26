---
title: isHighlighted
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontrol/ishighlighted
source_url: 'https://developer.apple.com/documentation/uikit/uicontrol/ishighlighted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontrol/ishighlighted.json'
content_hash: 'sha256:5b11645ff893091a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIControl](../uicontrol.md)

# isHighlighted

<sub>Instance Property</sub>

A Boolean value indicating whether the control draws a highlight.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isHighlighted: Bool { get set }
```

## Discussion

When the value of this property is [true](../../swift/true.md), the control draws a highlight; otherwise, the control doesn’t draw a highlight. Controls automatically set and clear this state in response to appropriate touch events. You can change the value of this property as needed to apply or remove a highlight programmatically

The default value of this property is [false](../../swift/false.md) for a newly created control. You can set a control’s initial selected state in your storyboard file.

## See Also

### Managing state

- [state](state-swift.property.md) — The state of the control, specified as a bit mask value.
- [State](state-swift.struct.md) — Constants describing the state of a control.
- [enabled](isenabled.md) — A Boolean value indicating whether the control is in the enabled state.
- [selected](isselected.md) — A Boolean value indicating whether the control is in the selected state.

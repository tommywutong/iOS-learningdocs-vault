---
title: selected
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontrol/state-swift.struct/selected
source_url: 'https://developer.apple.com/documentation/uikit/uicontrol/state-swift.struct/selected'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontrol/state-swift.struct/selected.json'
content_hash: 'sha256:6ad73bfd3dadeaa2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIControl](../../uicontrol.md) · [State](../state-swift.struct.md)

# selected

<sub>Type Property</sub>

The selected state of a control.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var selected: UIControl.State { get }
```

## Discussion

For many controls, this state has no effect on behavior or appearance. Some subclasses, like the [UISegmentedControl](../../uisegmentedcontrol.md) class, use this state to change their appearance. You can retrieve and set this value through the [selected](../isselected.md) property.

## See Also

### Constants

- [UIControlStateNormal](normal.md) — The normal, or default, state of a control where the control is enabled but neither selected nor highlighted.
- [UIControlStateHighlighted](highlighted.md) — The highlighted state of a control.
- [UIControlStateDisabled](disabled.md) — The disabled state of a control.
- [UIControlStateFocused](focused.md) — The focused state of a control.
- [UIControlStateApplication](application.md) — Additional control-state flags available for app use.
- [UIControlStateReserved](reserved.md) — Control-state flags reserved for internal framework use.

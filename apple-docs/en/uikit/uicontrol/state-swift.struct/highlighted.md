---
title: highlighted
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontrol/state-swift.struct/highlighted
source_url: 'https://developer.apple.com/documentation/uikit/uicontrol/state-swift.struct/highlighted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontrol/state-swift.struct/highlighted.json'
content_hash: 'sha256:8590e6fb54f41b49'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIControl](../../uicontrol.md) · [State](../state-swift.struct.md)

# highlighted

<sub>Type Property</sub>

The highlighted state of a control.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var highlighted: UIControl.State { get }
```

## Discussion

A control becomes highlighted when a touch event enters the control’s bounds, and it loses that highlight when there’s a touch-up event or when the touch event exits the control’s bounds. You can retrieve and set this value through the [highlighted](../ishighlighted.md) property.

## See Also

### Constants

- [UIControlStateNormal](normal.md) — The normal, or default, state of a control where the control is enabled but neither selected nor highlighted.
- [UIControlStateDisabled](disabled.md) — The disabled state of a control.
- [UIControlStateSelected](selected.md) — The selected state of a control.
- [UIControlStateFocused](focused.md) — The focused state of a control.
- [UIControlStateApplication](application.md) — Additional control-state flags available for app use.
- [UIControlStateReserved](reserved.md) — Control-state flags reserved for internal framework use.

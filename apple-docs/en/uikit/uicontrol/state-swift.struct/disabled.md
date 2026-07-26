---
title: disabled
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontrol/state-swift.struct/disabled
source_url: 'https://developer.apple.com/documentation/uikit/uicontrol/state-swift.struct/disabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontrol/state-swift.struct/disabled.json'
content_hash: 'sha256:b7c65958d5b8431b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIControl](../../uicontrol.md) · [State](../state-swift.struct.md)

# disabled

<sub>Type Property</sub>

The disabled state of a control.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var disabled: UIControl.State { get }
```

## Discussion

User interactions with disabled control have no effect and the control draws itself with a dimmed appearance to reflect that it’s disabled. You can retrieve and set this value through the [enabled](../isenabled.md) property.

## See Also

### Constants

- [UIControlStateNormal](normal.md) — The normal, or default, state of a control where the control is enabled but neither selected nor highlighted.
- [UIControlStateHighlighted](highlighted.md) — The highlighted state of a control.
- [UIControlStateSelected](selected.md) — The selected state of a control.
- [UIControlStateFocused](focused.md) — The focused state of a control.
- [UIControlStateApplication](application.md) — Additional control-state flags available for app use.
- [UIControlStateReserved](reserved.md) — Control-state flags reserved for internal framework use.

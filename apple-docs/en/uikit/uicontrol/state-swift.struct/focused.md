---
title: focused
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontrol/state-swift.struct/focused
source_url: 'https://developer.apple.com/documentation/uikit/uicontrol/state-swift.struct/focused'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontrol/state-swift.struct/focused.json'
content_hash: 'sha256:96c9fa0ab43b9354'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIControl](../../uicontrol.md) · [State](../state-swift.struct.md)

# focused

<sub>Type Property</sub>

The focused state of a control.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var focused: UIControl.State { get }
```

## Discussion

In focus-based navigation systems, a control enters this state when it receives the focus. A focused control changes its appearance to indicate that it has focus, and this appearance differs from the appearance of the control when it’s highlighted or selected. Further interactions with the control can result in it also becoming highlighted or selected.

## See Also

### Constants

- [UIControlStateNormal](normal.md) — The normal, or default, state of a control where the control is enabled but neither selected nor highlighted.
- [UIControlStateHighlighted](highlighted.md) — The highlighted state of a control.
- [UIControlStateDisabled](disabled.md) — The disabled state of a control.
- [UIControlStateSelected](selected.md) — The selected state of a control.
- [UIControlStateApplication](application.md) — Additional control-state flags available for app use.
- [UIControlStateReserved](reserved.md) — Control-state flags reserved for internal framework use.

---
title: isEnabled
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitooltipinteraction/isenabled
source_url: 'https://developer.apple.com/documentation/uikit/uitooltipinteraction/isenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitooltipinteraction/isenabled.json'
content_hash: 'sha256:c8df62a367f54c6b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIToolTipInteraction](../uitooltipinteraction.md)

# isEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the tooltip interaction is in the enabled state.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var isEnabled: Bool { get set }
```

## Discussion

A view or control can only display a tooltip from an enabled interaction. Set the value of the [enabled](isenabled.md) property to [true](../../swift/true.md) to enable the interaction or [false](../../swift/false.md) to disable it. The default value is [true](../../swift/true.md).

## See Also

### Managing the interaction

- [defaultToolTip](defaulttooltip.md) — The text that appears in a tooltip by default.

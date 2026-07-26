---
title: defaultToolTip
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitooltipinteraction/defaulttooltip
source_url: 'https://developer.apple.com/documentation/uikit/uitooltipinteraction/defaulttooltip'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitooltipinteraction/defaulttooltip.json'
content_hash: 'sha256:d2b1145dbc886aba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIToolTipInteraction](../uitooltipinteraction.md)

# defaultToolTip

<sub>Instance Property</sub>

The text that appears in a tooltip by default.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var defaultToolTip: String? { get set }
```

## Discussion

Set this property to the default text to display in the tooltip.

If you set the [delegate](delegate.md) property to an object that conforms to the [UIToolTipInteractionDelegate](../uitooltipinteractiondelegate.md) protocol and implements the [- toolTipInteraction:configurationAtPoint:](<../uitooltipinteractiondelegate/tooltipinteraction(__configurationat_).md>) method, then the return value of the delegate method determines the text that appears in the tooltip.

## See Also

### Managing the interaction

- [enabled](isenabled.md) — A Boolean value that indicates whether the tooltip interaction is in the enabled state.

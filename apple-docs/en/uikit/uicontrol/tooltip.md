---
title: toolTip
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontrol/tooltip
source_url: 'https://developer.apple.com/documentation/uikit/uicontrol/tooltip'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontrol/tooltip.json'
content_hash: 'sha256:eabf55957d4d2b0b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIControl](../uicontrol.md)

# toolTip

<sub>Instance Property</sub>

The default text to display in the control’s tooltip.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var toolTip: String? { get set }
```

## Discussion

Set this property to the text that should appear in the tooltip. If you want your app to determine the tooltip text at a later time — for instance, to determine the text based on the current state of your app — set the [delegate](../uitooltipinteraction/delegate.md) property of [toolTipInteraction](tooltipinteraction.md) after setting [toolTip](tooltip.md) with the default text. For example, the following code listing sets the tooltip’s default text and delegate for a shopping cart button:

```swift
let button = UIButton(configuration: configuration, primaryAction: action)
button.toolTip = "Click to add the item to your cart. Your cart is empty."
button.toolTipInteraction?.delegate = self
```

If the delegate implements the method [- toolTipInteraction:configurationAtPoint:](<../uitooltipinteractiondelegate/tooltipinteraction(__configurationat_).md>), the tooltip ignores the default text set in the [toolTip](tooltip.md) property. For more information, see [toolTipInteraction](tooltipinteraction.md).

## See Also

### Showing tooltips

- [toolTipInteraction](tooltipinteraction.md) — The tooltip interaction associated with the control.

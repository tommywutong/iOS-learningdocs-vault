---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitooltipinteraction/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uitooltipinteraction/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitooltipinteraction/delegate.json'
content_hash: 'sha256:2579a9da3c46d5c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIToolTipInteraction](../uitooltipinteraction.md)

# delegate

<sub>Instance Property</sub>

An object that provides text that a tooltip displays instead of the default text.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var delegate: (any UIToolTipInteractionDelegate)? { get set }
```

## Discussion

To provide tooltip text based on the current state or unique logic of your app, set the [delegate](delegate.md) property to an object that conforms to the [UIToolTipInteractionDelegate](../uitooltipinteractiondelegate.md) protocol and implements the [- toolTipInteraction:configurationAtPoint:](<../uitooltipinteractiondelegate/tooltipinteraction(__configurationat_).md>) method. The method returns a [UIToolTipConfiguration](../uitooltipconfiguration.md) object containing the text to display in the tooltip. For example, the following code listing instructs the tooltip to show the name of the view’s background color instead of the [defaultToolTip](defaulttooltip.md) text. If the color name is unavailable, the method returns `nil`, which disables the display of the tooltip.

```swift
func toolTipInteraction(_ interaction: UIToolTipInteraction, configurationAt point: CGPoint) -> UIToolTipConfiguration? {
    let configuration: UIToolTipConfiguration?
    if let accessibilityName = backgroundColor?.accessibilityName {
        configuration = UIToolTipConfiguration(toolTip: "The color is \(accessibilityName).")
    } else {
        configuration = nil
    }
    
    return configuration
}
```

## See Also

### Providing tooltip configurations

- [UIToolTipInteractionDelegate](../uitooltipinteractiondelegate.md) — An interface that provides tooltip settings to an interaction.

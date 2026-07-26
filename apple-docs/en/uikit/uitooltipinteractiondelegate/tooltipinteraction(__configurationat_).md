---
title: 'toolTipInteraction(_:configurationAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitooltipinteractiondelegate/tooltipinteraction(_:configurationat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitooltipinteractiondelegate/tooltipinteraction(_:configurationat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitooltipinteractiondelegate/tooltipinteraction%28_%3Aconfigurationat%3A%29.json'
content_hash: 'sha256:1443fd4ce8bb2c0f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIToolTipInteractionDelegate](../uitooltipinteractiondelegate.md)

# toolTipInteraction(_:configurationAt:)

<sub>Instance Method</sub>

Asks the delegate for a tooltip configuration that describes the tooltip settings.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func toolTipInteraction(_ interaction: UIToolTipInteraction, configurationAt point: CGPoint) -> UIToolTipConfiguration?
```

## Parameters

- `interaction` — The tooltip interaction requesting a tooltip configuration.

- `point` — The current position of the pointer in the coordinate space of the view or control associated to the tooltip interaction.

## Return Value

A tooltip configuration that specifies the text that appears in the tooltip and the region of the view or control where the pointer must hover over to trigger the display of the tooltip. Return `nil` to prevent the display of the tooltip.

## Discussion

Implement this method to provide a tooltip configuration based on logic specific to your app. For example, the following code listing returns a tooltip configuration when the pointer hovers over the top or bottom regions of the view. If the pointer hovers over the middle region, the method returns `nil` to prevent the display of a tooltip.

```swift
func toolTipInteraction(_ interaction: UIToolTipInteraction, configurationAt point: CGPoint) -> UIToolTipConfiguration? {   
    var topRect = self.bounds
    var bottomRect = self.bounds

    let partHeight = self.bounds.size.height / 3
    topRect.size.height = partHeight
    bottomRect.size.height = partHeight
    bottomRect.origin.y = partHeight * 2

    // Display tooltip if the pointer within the top or bottom rects.
    if topRect.contains(point) {
        return UIToolTipConfiguration(toolTip: "Top area of the view.", in: topRect)
    } else if bottomRect.contains(point) {
        return UIToolTipConfiguration(toolTip: "Bottom area of the view.", in: bottomRect)
    }
    
    // Pointer is in the middle of the view. Don't display a tooltip.
    return nil
}
```

## See Also

### Providing a tooltip configuration

- [UIToolTipConfiguration](../uitooltipconfiguration.md) — An object that a tooltip interaction delegate uses to describe the tooltip settings.

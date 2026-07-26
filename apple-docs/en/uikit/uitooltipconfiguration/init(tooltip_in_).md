---
title: 'init(toolTip:in:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitooltipconfiguration/init(tooltip:in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitooltipconfiguration/init(tooltip:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitooltipconfiguration/init%28tooltip%3Ain%3A%29.json'
content_hash: 'sha256:f81c17cb8eac6948'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIToolTipConfiguration](../uitooltipconfiguration.md)

# init(toolTip:in:)

<sub>Initializer</sub>

Creates a tooltip configuration, and sets the tooltip text and hover region within the view or control.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
convenience init(toolTip: String, in sourceRect: CGRect)
```

## Parameters

- `toolTip` — The text that appears in the tooltip.

- `sourceRect` — The region of the view or control where the pointer must hover to trigger the display of the tooltip.

## Discussion

Create a configuration using this method to show the tooltip when the pointer hovers over the specified region of the view or control. For example, the following code listing returns a configuration that instructs the view shows the tooltip only when the pointer hovers over either top or bottom regions of a view. The tooltip does’t appear when the pointer hovers over the middle region of the view.

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

### Creating a tooltip configuration

- [+ configurationWithToolTip:](<init(tooltip_).md>) — Creates a tooltip configuration and sets the tooltip text.

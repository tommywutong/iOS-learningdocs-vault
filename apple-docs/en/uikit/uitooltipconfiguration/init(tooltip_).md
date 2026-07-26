---
title: 'init(toolTip:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitooltipconfiguration/init(tooltip:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitooltipconfiguration/init(tooltip:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitooltipconfiguration/init%28tooltip%3A%29.json'
content_hash: 'sha256:64f06bddb0673720'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIToolTipConfiguration](../uitooltipconfiguration.md)

# init(toolTip:)

<sub>Initializer</sub>

Creates a tooltip configuration and sets the tooltip text.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
convenience init(toolTip: String)
```

## Parameters

- `toolTip` — The text that appears in the tooltip.

## Discussion

Create a configuration using this method to show the tooltip when the pointer hovers over any area of the view or control. For example, the following code listing creates a configuration that instructs the view to show the tooltip when the pointer hovers over any area of the view:

```swift
let configuration = UIToolTipConfiguration(toolTip: "The color is \(colorName).")
```

## See Also

### Creating a tooltip configuration

- [+ configurationWithToolTip:inRect:](<init(tooltip_in_).md>) — Creates a tooltip configuration, and sets the tooltip text and hover region within the view or control.

---
title: 'backgroundImage(for:style:barMetrics:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitem/backgroundimage(for:style:barmetrics:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/backgroundimage(for:style:barmetrics:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/backgroundimage%28for%3Astyle%3Abarmetrics%3A%29.json'
content_hash: 'sha256:c7bab0c725ee773e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# backgroundImage(for:style:barMetrics:)

<sub>Instance Method</sub>

Returns the background image for the specified state, style, and metrics.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func backgroundImage(for state: UIControl.State, style: UIBarButtonItem.Style, barMetrics: UIBarMetrics) -> UIImage?
```

## Parameters

- `state` — The bar button state.

- `style` — The bar button style.

- `barMetrics` — The bar button metrics.

## Return Value

The background image associated with the specified state, style, and metrics.

## See Also

### Customizing the background

- [- backgroundVerticalPositionAdjustmentForBarMetrics:](<backgroundverticalpositionadjustment(for_).md>) — Returns the background vertical position offset for specified bar metrics.
- [- setBackgroundVerticalPositionAdjustment:forBarMetrics:](<setbackgroundverticalpositionadjustment(__for_).md>) — Sets the background vertical position offset for specified bar metrics.
- [- backgroundImageForState:barMetrics:](<backgroundimage(for_barmetrics_).md>) — Returns the background image for a specified state and bar metrics.
- [- setBackgroundImage:forState:barMetrics:](<setbackgroundimage(__for_barmetrics_).md>) — Sets the background image for a specified state and bar metrics.
- [- setBackgroundImage:forState:style:barMetrics:](<setbackgroundimage(__for_style_barmetrics_).md>) — Sets the background image for the specified state, style, and metrics.

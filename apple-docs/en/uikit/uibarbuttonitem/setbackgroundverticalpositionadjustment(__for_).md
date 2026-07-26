---
title: 'setBackgroundVerticalPositionAdjustment(_:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitem/setbackgroundverticalpositionadjustment(_:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/setbackgroundverticalpositionadjustment(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/setbackgroundverticalpositionadjustment%28_%3Afor%3A%29.json'
content_hash: 'sha256:13e75ea8ece471e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# setBackgroundVerticalPositionAdjustment(_:for:)

<sub>Instance Method</sub>

Sets the background vertical position offset for specified bar metrics.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setBackgroundVerticalPositionAdjustment(_ adjustment: CGFloat, for barMetrics: UIBarMetrics)
```

## Parameters

- `adjustment` — The background vertical position offset for `barMetrics`.

- `barMetrics` — Bar metrics.

## Discussion

This offset is used to adjust the vertical centering of bordered bar buttons within the bar.

## See Also

### Customizing the background

- [- backgroundVerticalPositionAdjustmentForBarMetrics:](<backgroundverticalpositionadjustment(for_).md>) — Returns the background vertical position offset for specified bar metrics.
- [- backgroundImageForState:barMetrics:](<backgroundimage(for_barmetrics_).md>) — Returns the background image for a specified state and bar metrics.
- [- setBackgroundImage:forState:barMetrics:](<setbackgroundimage(__for_barmetrics_).md>) — Sets the background image for a specified state and bar metrics.
- [- backgroundImageForState:style:barMetrics:](<backgroundimage(for_style_barmetrics_).md>) — Returns the background image for the specified state, style, and metrics.
- [- setBackgroundImage:forState:style:barMetrics:](<setbackgroundimage(__for_style_barmetrics_).md>) — Sets the background image for the specified state, style, and metrics.

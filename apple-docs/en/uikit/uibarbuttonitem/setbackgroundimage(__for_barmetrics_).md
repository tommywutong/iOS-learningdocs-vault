---
title: 'setBackgroundImage(_:for:barMetrics:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitem/setbackgroundimage(_:for:barmetrics:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/setbackgroundimage(_:for:barmetrics:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/setbackgroundimage%28_%3Afor%3Abarmetrics%3A%29.json'
content_hash: 'sha256:54e1fdaa5bbc71b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# setBackgroundImage(_:for:barMetrics:)

<sub>Instance Method</sub>

Sets the background image for a specified state and bar metrics.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setBackgroundImage(_ backgroundImage: UIImage?, for state: UIControl.State, barMetrics: UIBarMetrics)
```

## Parameters

- `backgroundImage` — The background image for the specified state and metrics.

- `state` — A control state.

- `barMetrics` — Bar metrics.

## Discussion

For good results, `backgroundImage` must be a stretchable image.

## See Also

### Customizing the background

- [- backgroundVerticalPositionAdjustmentForBarMetrics:](<backgroundverticalpositionadjustment(for_).md>) — Returns the background vertical position offset for specified bar metrics.
- [- setBackgroundVerticalPositionAdjustment:forBarMetrics:](<setbackgroundverticalpositionadjustment(__for_).md>) — Sets the background vertical position offset for specified bar metrics.
- [- backgroundImageForState:barMetrics:](<backgroundimage(for_barmetrics_).md>) — Returns the background image for a specified state and bar metrics.
- [- backgroundImageForState:style:barMetrics:](<backgroundimage(for_style_barmetrics_).md>) — Returns the background image for the specified state, style, and metrics.
- [- setBackgroundImage:forState:style:barMetrics:](<setbackgroundimage(__for_style_barmetrics_).md>) — Sets the background image for the specified state, style, and metrics.

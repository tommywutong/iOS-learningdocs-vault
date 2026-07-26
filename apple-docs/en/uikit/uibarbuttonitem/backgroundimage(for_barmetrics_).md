---
title: 'backgroundImage(for:barMetrics:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitem/backgroundimage(for:barmetrics:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/backgroundimage(for:barmetrics:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/backgroundimage%28for%3Abarmetrics%3A%29.json'
content_hash: 'sha256:d43f22ba17d302a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# backgroundImage(for:barMetrics:)

<sub>Instance Method</sub>

Returns the background image for a specified state and bar metrics.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func backgroundImage(for state: UIControl.State, barMetrics: UIBarMetrics) -> UIImage?
```

## Parameters

- `state` — A control state.

- `barMetrics` — Bar metrics.

## Return Value

The background image for the button given state and metrics.

## See Also

### Customizing the background

- [- backgroundVerticalPositionAdjustmentForBarMetrics:](<backgroundverticalpositionadjustment(for_).md>) — Returns the background vertical position offset for specified bar metrics.
- [- setBackgroundVerticalPositionAdjustment:forBarMetrics:](<setbackgroundverticalpositionadjustment(__for_).md>) — Sets the background vertical position offset for specified bar metrics.
- [- setBackgroundImage:forState:barMetrics:](<setbackgroundimage(__for_barmetrics_).md>) — Sets the background image for a specified state and bar metrics.
- [- backgroundImageForState:style:barMetrics:](<backgroundimage(for_style_barmetrics_).md>) — Returns the background image for the specified state, style, and metrics.
- [- setBackgroundImage:forState:style:barMetrics:](<setbackgroundimage(__for_style_barmetrics_).md>) — Sets the background image for the specified state, style, and metrics.

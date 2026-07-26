---
title: 'backgroundVerticalPositionAdjustment(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitem/backgroundverticalpositionadjustment(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/backgroundverticalpositionadjustment(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/backgroundverticalpositionadjustment%28for%3A%29.json'
content_hash: 'sha256:a25f0bf90096c92d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# backgroundVerticalPositionAdjustment(for:)

<sub>Instance Method</sub>

Returns the background vertical position offset for specified bar metrics.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func backgroundVerticalPositionAdjustment(for barMetrics: UIBarMetrics) -> CGFloat
```

## Parameters

- `barMetrics` — Bar metrics.

## Return Value

The background vertical position offset for `barMetrics`.

## Discussion

This offset is used to adjust the vertical centering of bordered bar buttons within the bar.

## See Also

### Customizing the background

- [- setBackgroundVerticalPositionAdjustment:forBarMetrics:](<setbackgroundverticalpositionadjustment(__for_).md>) — Sets the background vertical position offset for specified bar metrics.
- [- backgroundImageForState:barMetrics:](<backgroundimage(for_barmetrics_).md>) — Returns the background image for a specified state and bar metrics.
- [- setBackgroundImage:forState:barMetrics:](<setbackgroundimage(__for_barmetrics_).md>) — Sets the background image for a specified state and bar metrics.
- [- backgroundImageForState:style:barMetrics:](<backgroundimage(for_style_barmetrics_).md>) — Returns the background image for the specified state, style, and metrics.
- [- setBackgroundImage:forState:style:barMetrics:](<setbackgroundimage(__for_style_barmetrics_).md>) — Sets the background image for the specified state, style, and metrics.

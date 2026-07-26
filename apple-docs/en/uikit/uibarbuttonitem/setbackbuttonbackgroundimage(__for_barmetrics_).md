---
title: 'setBackButtonBackgroundImage(_:for:barMetrics:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitem/setbackbuttonbackgroundimage(_:for:barmetrics:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/setbackbuttonbackgroundimage(_:for:barmetrics:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/setbackbuttonbackgroundimage%28_%3Afor%3Abarmetrics%3A%29.json'
content_hash: 'sha256:7cce7910d0f1e5c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# setBackButtonBackgroundImage(_:for:barMetrics:)

<sub>Instance Method</sub>

Sets the back button background image for a specified control state and bar metrics.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func setBackButtonBackgroundImage(_ backgroundImage: UIImage?, for state: UIControl.State, barMetrics: UIBarMetrics)
```

## Parameters

- `backgroundImage` — The image to use for the back button’s background.

- `state` — A control state.

- `barMetrics` — Bar metrics.

## Discussion

This modifier applies only to navigation bar back buttons and is ignored by other buttons.

For good results, `backgroundImage` must be a stretchable image.

## See Also

### Customizing the Back button

- [- backButtonBackgroundImageForState:barMetrics:](<backbuttonbackgroundimage(for_barmetrics_).md>) — Returns the back button background image for a specified control state and bar metrics.
- [- backButtonTitlePositionAdjustmentForBarMetrics:](<backbuttontitlepositionadjustment(for_).md>) — Returns the back button title offset for specified bar metrics.
- [- setBackButtonTitlePositionAdjustment:forBarMetrics:](<setbackbuttontitlepositionadjustment(__for_).md>) — Sets the back button title offset for specified bar metrics.
- [- backButtonBackgroundVerticalPositionAdjustmentForBarMetrics:](<backbuttonbackgroundverticalpositionadjustment(for_).md>) — Returns the back button vertical position offset for specified bar metrics.
- [- setBackButtonBackgroundVerticalPositionAdjustment:forBarMetrics:](<setbackbuttonbackgroundverticalpositionadjustment(__for_).md>) — Sets the back button vertical position offset for specified bar metrics.

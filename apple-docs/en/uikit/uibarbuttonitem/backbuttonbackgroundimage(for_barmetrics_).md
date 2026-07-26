---
title: 'backButtonBackgroundImage(for:barMetrics:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitem/backbuttonbackgroundimage(for:barmetrics:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/backbuttonbackgroundimage(for:barmetrics:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/backbuttonbackgroundimage%28for%3Abarmetrics%3A%29.json'
content_hash: 'sha256:2c7c648c17ab4560'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# backButtonBackgroundImage(for:barMetrics:)

<sub>Instance Method</sub>

Returns the back button background image for a specified control state and bar metrics.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func backButtonBackgroundImage(for state: UIControl.State, barMetrics: UIBarMetrics) -> UIImage?
```

## Parameters

- `state` — A control state.

- `barMetrics` — Bar metrics.

## Return Value

The back button background image for `state` and `barMetrics`.

## Discussion

This modifier applies only to navigation bar back buttons and is ignored by other buttons.

## See Also

### Customizing the Back button

- [- setBackButtonBackgroundImage:forState:barMetrics:](<setbackbuttonbackgroundimage(__for_barmetrics_).md>) — Sets the back button background image for a specified control state and bar metrics.
- [- backButtonTitlePositionAdjustmentForBarMetrics:](<backbuttontitlepositionadjustment(for_).md>) — Returns the back button title offset for specified bar metrics.
- [- setBackButtonTitlePositionAdjustment:forBarMetrics:](<setbackbuttontitlepositionadjustment(__for_).md>) — Sets the back button title offset for specified bar metrics.
- [- backButtonBackgroundVerticalPositionAdjustmentForBarMetrics:](<backbuttonbackgroundverticalpositionadjustment(for_).md>) — Returns the back button vertical position offset for specified bar metrics.
- [- setBackButtonBackgroundVerticalPositionAdjustment:forBarMetrics:](<setbackbuttonbackgroundverticalpositionadjustment(__for_).md>) — Sets the back button vertical position offset for specified bar metrics.

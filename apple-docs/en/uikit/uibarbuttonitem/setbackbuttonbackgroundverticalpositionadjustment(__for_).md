---
title: 'setBackButtonBackgroundVerticalPositionAdjustment(_:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitem/setbackbuttonbackgroundverticalpositionadjustment(_:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/setbackbuttonbackgroundverticalpositionadjustment(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/setbackbuttonbackgroundverticalpositionadjustment%28_%3Afor%3A%29.json'
content_hash: 'sha256:cd882fa6fa88aeed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# setBackButtonBackgroundVerticalPositionAdjustment(_:for:)

<sub>Instance Method</sub>

Sets the back button vertical position offset for specified bar metrics.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func setBackButtonBackgroundVerticalPositionAdjustment(_ adjustment: CGFloat, for barMetrics: UIBarMetrics)
```

## Parameters

- `adjustment` — The back button vertical position offset for `barMetrics`.

- `barMetrics` — Bar metrics.

## Discussion

This modifier applies only to navigation bar back buttons and is ignored by other buttons.

This offset is used to adjust the vertical centering of bordered bar buttons within the bar.

## See Also

### Customizing the Back button

- [- backButtonBackgroundImageForState:barMetrics:](<backbuttonbackgroundimage(for_barmetrics_).md>) — Returns the back button background image for a specified control state and bar metrics.
- [- setBackButtonBackgroundImage:forState:barMetrics:](<setbackbuttonbackgroundimage(__for_barmetrics_).md>) — Sets the back button background image for a specified control state and bar metrics.
- [- backButtonTitlePositionAdjustmentForBarMetrics:](<backbuttontitlepositionadjustment(for_).md>) — Returns the back button title offset for specified bar metrics.
- [- setBackButtonTitlePositionAdjustment:forBarMetrics:](<setbackbuttontitlepositionadjustment(__for_).md>) — Sets the back button title offset for specified bar metrics.
- [- backButtonBackgroundVerticalPositionAdjustmentForBarMetrics:](<backbuttonbackgroundverticalpositionadjustment(for_).md>) — Returns the back button vertical position offset for specified bar metrics.

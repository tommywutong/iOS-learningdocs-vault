---
title: 'backButtonTitlePositionAdjustment(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitem/backbuttontitlepositionadjustment(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/backbuttontitlepositionadjustment(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/backbuttontitlepositionadjustment%28for%3A%29.json'
content_hash: 'sha256:fc3aeec58382e9ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# backButtonTitlePositionAdjustment(for:)

<sub>Instance Method</sub>

Returns the back button title offset for specified bar metrics.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func backButtonTitlePositionAdjustment(for barMetrics: UIBarMetrics) -> UIOffset
```

## Parameters

- `barMetrics` — Bar metrics.

## Return Value

The back button title offset for `barMetrics`.

## Discussion

This modifier applies only to navigation bar back buttons and is ignored by other buttons.

## See Also

### Customizing the Back button

- [- backButtonBackgroundImageForState:barMetrics:](<backbuttonbackgroundimage(for_barmetrics_).md>) — Returns the back button background image for a specified control state and bar metrics.
- [- setBackButtonBackgroundImage:forState:barMetrics:](<setbackbuttonbackgroundimage(__for_barmetrics_).md>) — Sets the back button background image for a specified control state and bar metrics.
- [- setBackButtonTitlePositionAdjustment:forBarMetrics:](<setbackbuttontitlepositionadjustment(__for_).md>) — Sets the back button title offset for specified bar metrics.
- [- backButtonBackgroundVerticalPositionAdjustmentForBarMetrics:](<backbuttonbackgroundverticalpositionadjustment(for_).md>) — Returns the back button vertical position offset for specified bar metrics.
- [- setBackButtonBackgroundVerticalPositionAdjustment:forBarMetrics:](<setbackbuttonbackgroundverticalpositionadjustment(__for_).md>) — Sets the back button vertical position offset for specified bar metrics.

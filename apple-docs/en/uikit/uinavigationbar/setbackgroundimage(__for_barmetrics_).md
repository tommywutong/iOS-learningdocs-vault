---
title: 'setBackgroundImage(_:for:barMetrics:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uinavigationbar/setbackgroundimage(_:for:barmetrics:)'
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationbar/setbackgroundimage(_:for:barmetrics:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationbar/setbackgroundimage%28_%3Afor%3Abarmetrics%3A%29.json'
content_hash: 'sha256:bcc39427e47688a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationBar](../uinavigationbar.md)

# setBackgroundImage(_:for:barMetrics:)

<sub>Instance Method</sub>

Sets the background image to use for a given bar position and set of metrics.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setBackgroundImage(_ backgroundImage: UIImage?, for barPosition: UIBarPosition, barMetrics: UIBarMetrics)
```

## Parameters

- `backgroundImage` — The image to use for the specified location and metrics.

- `barPosition` — The location of the navigation bar.

- `barMetrics` — The metrics of the navigation bar.

## Discussion

Resizable images will be stretched vertically, if necessary, for a position of [UIBarPositionTopAttached](../uibarposition/topattached.md).

## See Also

### Changing the background

- [barTintColor](bartintcolor.md) — The tint color to apply to the navigation bar background.
- [- backgroundImageForBarMetrics:](<backgroundimage(for_).md>) — Returns the background image for given bar metrics.
- [- setBackgroundImage:forBarMetrics:](<setbackgroundimage(__for_).md>) — Sets the background image for given bar metrics.
- [- backgroundImageForBarPosition:barMetrics:](<backgroundimage(for_barmetrics_).md>) — Returns the background image to use for a given bar position and set of metrics.

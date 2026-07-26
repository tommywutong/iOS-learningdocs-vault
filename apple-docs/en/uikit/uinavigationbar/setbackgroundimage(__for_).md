---
title: 'setBackgroundImage(_:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uinavigationbar/setbackgroundimage(_:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationbar/setbackgroundimage(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationbar/setbackgroundimage%28_%3Afor%3A%29.json'
content_hash: 'sha256:80032271d9e8887f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationBar](../uinavigationbar.md)

# setBackgroundImage(_:for:)

<sub>Instance Method</sub>

Sets the background image for given bar metrics.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setBackgroundImage(_ backgroundImage: UIImage?, for barMetrics: UIBarMetrics)
```

## Parameters

- `backgroundImage` — The background image to use for `barMetrics`.

- `barMetrics` — A bar metrics constant.

## Discussion

Equivalent to using [- setBackgroundImage:forBarPosition:barMetrics:](<setbackgroundimage(__for_barmetrics_).md>) with a position of [UIBarPositionAny](../uibarposition/any.md).

## See Also

### Changing the background

- [barTintColor](bartintcolor.md) — The tint color to apply to the navigation bar background.
- [- backgroundImageForBarMetrics:](<backgroundimage(for_).md>) — Returns the background image for given bar metrics.
- [- backgroundImageForBarPosition:barMetrics:](<backgroundimage(for_barmetrics_).md>) — Returns the background image to use for a given bar position and set of metrics.
- [- setBackgroundImage:forBarPosition:barMetrics:](<setbackgroundimage(__for_barmetrics_).md>) — Sets the background image to use for a given bar position and set of metrics.

---
title: 'setBackgroundImage(_:forToolbarPosition:barMetrics:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitoolbar/setbackgroundimage(_:fortoolbarposition:barmetrics:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitoolbar/setbackgroundimage(_:fortoolbarposition:barmetrics:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitoolbar/setbackgroundimage%28_%3Afortoolbarposition%3Abarmetrics%3A%29.json'
content_hash: 'sha256:8e91872a8502c6fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIToolbar](../uitoolbar.md)

# setBackgroundImage(_:forToolbarPosition:barMetrics:)

<sub>Instance Method</sub>

Sets the image to use for the background in a given position and with given metrics.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func setBackgroundImage(_ backgroundImage: UIImage?, forToolbarPosition topOrBottom: UIBarPosition, barMetrics: UIBarMetrics)
```

## Parameters

- `backgroundImage` — The image to use for the toolbar background in the position specified by `topOrBottom` and with the metrics specified by `barMetrics`.

- `topOrBottom` — A toolbar position constant.

- `barMetrics` — A bar metrics constant.

## See Also

### Changing the background

- [barTintColor](bartintcolor.md) — The tint color to apply to the toolbar background.
- [- backgroundImageForToolbarPosition:barMetrics:](<backgroundimage(fortoolbarposition_barmetrics_).md>) — Returns the image to use for the background in a given position and with given metrics.

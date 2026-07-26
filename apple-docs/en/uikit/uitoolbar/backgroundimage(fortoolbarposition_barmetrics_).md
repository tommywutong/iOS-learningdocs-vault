---
title: 'backgroundImage(forToolbarPosition:barMetrics:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitoolbar/backgroundimage(fortoolbarposition:barmetrics:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitoolbar/backgroundimage(fortoolbarposition:barmetrics:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitoolbar/backgroundimage%28fortoolbarposition%3Abarmetrics%3A%29.json'
content_hash: 'sha256:b6f0cdff8e702c6c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIToolbar](../uitoolbar.md)

# backgroundImage(forToolbarPosition:barMetrics:)

<sub>Instance Method</sub>

Returns the image to use for the background in a given position and with given metrics.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func backgroundImage(forToolbarPosition topOrBottom: UIBarPosition, barMetrics: UIBarMetrics) -> UIImage?
```

## Parameters

- `topOrBottom` — The location the bar is being drawn in.

- `barMetrics` — The metrics being used to draw the bar.

## Return Value

The image to use for the toolbar background in the position specified by `topOrBottom` and with the metrics specified by `barMetrics`.

## Discussion

The default value is `nil`. When non-`nil` the image will be used instead of the system image for toolbars in the specified position.

## See Also

### Changing the background

- [barTintColor](bartintcolor.md) — The tint color to apply to the toolbar background.
- [- setBackgroundImage:forToolbarPosition:barMetrics:](<setbackgroundimage(__fortoolbarposition_barmetrics_).md>) — Sets the image to use for the background in a given position and with given metrics.

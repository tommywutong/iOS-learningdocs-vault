---
title: 'backgroundImage(for:barMetrics:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uinavigationbar/backgroundimage(for:barmetrics:)'
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationbar/backgroundimage(for:barmetrics:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationbar/backgroundimage%28for%3Abarmetrics%3A%29.json'
content_hash: 'sha256:5287cb2cacd3a806'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationBar](../uinavigationbar.md)

# backgroundImage(for:barMetrics:)

<sub>Instance Method</sub>

Returns the background image to use for a given bar position and set of metrics.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func backgroundImage(for barPosition: UIBarPosition, barMetrics: UIBarMetrics) -> UIImage?
```

## Parameters

- `barPosition` — The location of the navigation bar.

- `barMetrics` — The metrics of the navigation bar.

## Return Value

The image to use for the specified location and metrics.

## Discussion

Resizable images will be stretched vertically, if necessary, for a position of [UIBarPositionTopAttached](../uibarposition/topattached.md).

## See Also

### Changing the background

- [barTintColor](bartintcolor.md) — The tint color to apply to the navigation bar background.
- [- backgroundImageForBarMetrics:](<backgroundimage(for_).md>) — Returns the background image for given bar metrics.
- [- setBackgroundImage:forBarMetrics:](<setbackgroundimage(__for_).md>) — Sets the background image for given bar metrics.
- [- setBackgroundImage:forBarPosition:barMetrics:](<setbackgroundimage(__for_barmetrics_).md>) — Sets the background image to use for a given bar position and set of metrics.

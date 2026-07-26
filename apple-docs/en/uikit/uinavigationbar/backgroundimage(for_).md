---
title: 'backgroundImage(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uinavigationbar/backgroundimage(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationbar/backgroundimage(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationbar/backgroundimage%28for%3A%29.json'
content_hash: 'sha256:215b7d5e4cbe8699'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationBar](../uinavigationbar.md)

# backgroundImage(for:)

<sub>Instance Method</sub>

Returns the background image for given bar metrics.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func backgroundImage(for barMetrics: UIBarMetrics) -> UIImage?
```

## Parameters

- `barMetrics` — A bar metrics constant.

## Return Value

The background image for `barMetrics`.

## Discussion

Equivalent to using [- backgroundImageForBarPosition:barMetrics:](<backgroundimage(for_barmetrics_).md>) with a position of [UIBarPositionAny](../uibarposition/any.md).

## See Also

### Changing the background

- [barTintColor](bartintcolor.md) — The tint color to apply to the navigation bar background.
- [- setBackgroundImage:forBarMetrics:](<setbackgroundimage(__for_).md>) — Sets the background image for given bar metrics.
- [- backgroundImageForBarPosition:barMetrics:](<backgroundimage(for_barmetrics_).md>) — Returns the background image to use for a given bar position and set of metrics.
- [- setBackgroundImage:forBarPosition:barMetrics:](<setbackgroundimage(__for_barmetrics_).md>) — Sets the background image to use for a given bar position and set of metrics.

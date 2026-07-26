---
title: barTintColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationbar/bartintcolor
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationbar/bartintcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationbar/bartintcolor.json'
content_hash: 'sha256:7d6887b07095de19'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationBar](../uinavigationbar.md)

# barTintColor

<sub>Instance Property</sub>

The tint color to apply to the navigation bar background.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var barTintColor: UIColor? { get set }
```

## Discussion

This color is made translucent by default unless you set the [translucent](istranslucent.md) property to [false](../../swift/false.md).

## See Also

### Changing the background

- [- backgroundImageForBarMetrics:](<backgroundimage(for_).md>) — Returns the background image for given bar metrics.
- [- setBackgroundImage:forBarMetrics:](<setbackgroundimage(__for_).md>) — Sets the background image for given bar metrics.
- [- backgroundImageForBarPosition:barMetrics:](<backgroundimage(for_barmetrics_).md>) — Returns the background image to use for a given bar position and set of metrics.
- [- setBackgroundImage:forBarPosition:barMetrics:](<setbackgroundimage(__for_barmetrics_).md>) — Sets the background image to use for a given bar position and set of metrics.

---
title: barTintColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitoolbar/bartintcolor
source_url: 'https://developer.apple.com/documentation/uikit/uitoolbar/bartintcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitoolbar/bartintcolor.json'
content_hash: 'sha256:e66ba04682dc7b69'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIToolbar](../uitoolbar.md)

# barTintColor

<sub>Instance Property</sub>

The tint color to apply to the toolbar background.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var barTintColor: UIColor? { get set }
```

## Discussion

This color is made translucent by default unless you set the [translucent](istranslucent.md) property to [false](../../swift/false.md).

## See Also

### Changing the background

- [- backgroundImageForToolbarPosition:barMetrics:](<backgroundimage(fortoolbarposition_barmetrics_).md>) — Returns the image to use for the background in a given position and with given metrics.
- [- setBackgroundImage:forToolbarPosition:barMetrics:](<setbackgroundimage(__fortoolbarposition_barmetrics_).md>) — Sets the image to use for the background in a given position and with given metrics.

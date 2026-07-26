---
title: progressViewStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprogressview/progressviewstyle
source_url: 'https://developer.apple.com/documentation/uikit/uiprogressview/progressviewstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprogressview/progressviewstyle.json'
content_hash: 'sha256:86028747f0b898de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIProgressView](../uiprogressview.md)

# progressViewStyle

<sub>Instance Property</sub>

The current graphical style of the progress view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var progressViewStyle: UIProgressView.Style { get set }
```

## Discussion

The value of this property is a constant that specifies the style of the progress view. The default style is [UIProgressViewStyleDefault](style/default.md). For more on these constants, see [Style](style.md).

## See Also

### Configuring the progress bar

- [progressTintColor](progresstintcolor.md) — The color shown for the portion of the progress bar that’s filled.
- [progressImage](progressimage.md) — An image to use for the portion of the progress bar that’s filled.
- [trackTintColor](tracktintcolor.md) — The color shown for the portion of the progress bar that isn’t filled.
- [trackImage](trackimage.md) — An image to use for the portion of the track that isn’t filled.

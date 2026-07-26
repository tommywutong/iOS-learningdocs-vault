---
title: progressImage
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprogressview/progressimage
source_url: 'https://developer.apple.com/documentation/uikit/uiprogressview/progressimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprogressview/progressimage.json'
content_hash: 'sha256:7f281cfcb13aeaf6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIProgressView](../uiprogressview.md)

# progressImage

<sub>Instance Property</sub>

An image to use for the portion of the progress bar that’s filled.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var progressImage: UIImage? { get set }
```

## Discussion

If you provide a custom image, the [progressTintColor](progresstintcolor.md) property is ignored.

## See Also

### Configuring the progress bar

- [progressViewStyle](progressviewstyle.md) — The current graphical style of the progress view.
- [progressTintColor](progresstintcolor.md) — The color shown for the portion of the progress bar that’s filled.
- [trackTintColor](tracktintcolor.md) — The color shown for the portion of the progress bar that isn’t filled.
- [trackImage](trackimage.md) — An image to use for the portion of the track that isn’t filled.

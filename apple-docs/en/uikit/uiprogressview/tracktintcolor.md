---
title: trackTintColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprogressview/tracktintcolor
source_url: 'https://developer.apple.com/documentation/uikit/uiprogressview/tracktintcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprogressview/tracktintcolor.json'
content_hash: 'sha256:ab778898b2b2c54d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIProgressView](../uiprogressview.md)

# trackTintColor

<sub>Instance Property</sub>

The color shown for the portion of the progress bar that isn’t filled.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var trackTintColor: UIColor? { get set }
```

## Discussion

If you set [trackTintColor](tracktintcolor.md) to `nil`, the track uses the tint of its parent.

## See Also

### Configuring the progress bar

- [progressViewStyle](progressviewstyle.md) — The current graphical style of the progress view.
- [progressTintColor](progresstintcolor.md) — The color shown for the portion of the progress bar that’s filled.
- [progressImage](progressimage.md) — An image to use for the portion of the progress bar that’s filled.
- [trackImage](trackimage.md) — An image to use for the portion of the track that isn’t filled.

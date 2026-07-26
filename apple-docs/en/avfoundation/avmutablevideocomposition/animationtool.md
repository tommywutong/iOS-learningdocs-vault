---
title: animationTool
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（26.0 起废弃）, iPadOS 4.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, macOS 10.7+（26.0 起废弃）, tvOS 9.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avmutablevideocomposition/animationtool
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/animationtool'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablevideocomposition/animationtool.json'
content_hash: 'sha256:da9515b942acfc50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableVideoComposition](../avmutablevideocomposition.md)

# animationTool

<sub>Instance Property</sub>

A video composition tool to use with Core Animation in offline rendering.

> [!warning] Deprecated
> Use AVVideoComposition.Configuration instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var animationTool: AVVideoCompositionCoreAnimationTool? { get set }
```

## Discussion

This attribute may be `nil`. Set an animation tool if you are using the composition in conjunction with [AVAssetExportSession](../avassetexportsession.md) for offline rendering, rather than with [AVPlayer](../avplayer.md).

## See Also

### Configuring video composition properties

- [frameDuration](frameduration.md) — A time interval for which the video composition should render composed video frames. _(deprecated)_
- [renderSize](rendersize.md) — The size at which the video composition should render. _(deprecated)_
- [renderScale](renderscale.md) — The scale at which the video composition should render. _(deprecated)_

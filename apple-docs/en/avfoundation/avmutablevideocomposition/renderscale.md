---
title: renderScale
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（26.0 起废弃）, iPadOS 4.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, macOS 10.14+（26.0 起废弃）, tvOS 9.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avmutablevideocomposition/renderscale
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/renderscale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablevideocomposition/renderscale.json'
content_hash: 'sha256:d262401d332923fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableVideoComposition](../avmutablevideocomposition.md)

# renderScale

<sub>Instance Property</sub>

The scale at which the video composition should render.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var renderScale: Float { get set }
```

## Discussion

May only be other than `1.0` for a video composition set on an [AVPlayerItem](../avplayeritem.md).

## See Also

### Configuring video composition properties

- [frameDuration](frameduration.md) — A time interval for which the video composition should render composed video frames. _(deprecated)_
- [renderSize](rendersize.md) — The size at which the video composition should render. _(deprecated)_
- [animationTool](animationtool.md) — A video composition tool to use with Core Animation in offline rendering. _(deprecated)_

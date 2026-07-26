---
title: frameDuration
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（26.0 起废弃）, iPadOS 4.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, macOS 10.7+（26.0 起废弃）, tvOS 9.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avmutablevideocomposition/frameduration
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/frameduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablevideocomposition/frameduration.json'
content_hash: 'sha256:84e52a62278c4bf2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableVideoComposition](../avmutablevideocomposition.md)

# frameDuration

<sub>Instance Property</sub>

A time interval for which the video composition should render composed video frames.

> [!warning] Deprecated
> Use AVVideoComposition.Configuration instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var frameDuration: CMTime { get set }
```

## See Also

### Configuring video composition properties

- [renderSize](rendersize.md) — The size at which the video composition should render. _(deprecated)_
- [renderScale](renderscale.md) — The scale at which the video composition should render. _(deprecated)_
- [animationTool](animationtool.md) — A video composition tool to use with Core Animation in offline rendering. _(deprecated)_

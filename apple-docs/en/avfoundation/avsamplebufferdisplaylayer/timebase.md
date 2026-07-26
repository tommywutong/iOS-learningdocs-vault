---
title: timebase
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（18.0 起废弃）, iPadOS 8.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.8+（15.0 起废弃）, tvOS 10.2+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avsamplebufferdisplaylayer/timebase
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/timebase'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferdisplaylayer/timebase.json'
content_hash: 'sha256:a7fac916485635e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferDisplayLayer](../avsamplebufferdisplaylayer.md)

# timebase

<sub>Instance Property</sub>

The renderer’s timebase, which determines how the layer interprets time stamps.

> [!warning] Deprecated
> Use sampleBufferRenderer's timebase instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var timebase: CMTimebase { get }
```

## Discussion

Apple discourages the use of this symbol in iOS 17, tvOS 17, and macOS 14 and later. Use [timebase](../avqueuedsamplebufferrendering/timebase.md) on the [sampleBufferRenderer](samplebufferrenderer.md) instead.

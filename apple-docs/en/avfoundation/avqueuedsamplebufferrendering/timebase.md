---
title: timebase
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avqueuedsamplebufferrendering/timebase
source_url: 'https://developer.apple.com/documentation/avfoundation/avqueuedsamplebufferrendering/timebase'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avqueuedsamplebufferrendering/timebase.json'
content_hash: 'sha256:ecc486380c730064'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVQueuedSampleBufferRendering](../avqueuedsamplebufferrendering.md)

# timebase

<sub>Instance Property</sub>

The timebase for a renderer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var timebase: CMTimebase { get }
```

## Discussion

The timebase governs how time stamps are interpreted by the renderer.

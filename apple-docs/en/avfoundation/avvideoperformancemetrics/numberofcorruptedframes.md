---
title: numberOfCorruptedFrames
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideoperformancemetrics/numberofcorruptedframes
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideoperformancemetrics/numberofcorruptedframes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideoperformancemetrics/numberofcorruptedframes.json'
content_hash: 'sha256:500d751f86a0f79f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoPerformanceMetrics](../avvideoperformancemetrics.md)

# numberOfCorruptedFrames

<sub>Instance Property</sub>

The total number of corrupted frames.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var numberOfCorruptedFrames: Int { get }
```

## See Also

### Inspecting metrics

- [numberOfDroppedFrames](numberofdroppedframes.md) — The total number of frames the system drops prior to decoding or from missing the display deadline.
- [numberOfFramesDisplayedUsingOptimizedCompositing](numberofframesdisplayedusingoptimizedcompositing.md) — The total number of full screen frames rendered in a special power-efficient mode that didn’t require compositing with other UI elements.
- [totalAccumulatedFrameDelay](totalaccumulatedframedelay.md) — The accumulated amount of time between the prescribed presentation times of displayed video frames and their actual time of display.
- [totalNumberOfFrames](totalnumberofframes.md) — The total number of frames that display if no frames drop.

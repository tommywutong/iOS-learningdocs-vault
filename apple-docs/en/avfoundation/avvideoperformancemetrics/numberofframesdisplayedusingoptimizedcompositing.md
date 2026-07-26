---
title: numberOfFramesDisplayedUsingOptimizedCompositing
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideoperformancemetrics/numberofframesdisplayedusingoptimizedcompositing
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideoperformancemetrics/numberofframesdisplayedusingoptimizedcompositing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideoperformancemetrics/numberofframesdisplayedusingoptimizedcompositing.json'
content_hash: 'sha256:36720c9d5b4b2976'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoPerformanceMetrics](../avvideoperformancemetrics.md)

# numberOfFramesDisplayedUsingOptimizedCompositing

<sub>Instance Property</sub>

The total number of full screen frames rendered in a special power-efficient mode that didn’t require compositing with other UI elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var numberOfFramesDisplayedUsingOptimizedCompositing: Int { get }
```

## See Also

### Inspecting metrics

- [numberOfCorruptedFrames](numberofcorruptedframes.md) — The total number of corrupted frames.
- [numberOfDroppedFrames](numberofdroppedframes.md) — The total number of frames the system drops prior to decoding or from missing the display deadline.
- [totalAccumulatedFrameDelay](totalaccumulatedframedelay.md) — The accumulated amount of time between the prescribed presentation times of displayed video frames and their actual time of display.
- [totalNumberOfFrames](totalnumberofframes.md) — The total number of frames that display if no frames drop.

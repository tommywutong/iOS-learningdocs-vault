---
title: numberOfNonDisplayCompositedVideoFrames
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideoperformancemetrics/numberofnondisplaycompositedvideoframes
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideoperformancemetrics/numberofnondisplaycompositedvideoframes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideoperformancemetrics/numberofnondisplaycompositedvideoframes.json'
content_hash: 'sha256:0a1083c02e159654'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoPerformanceMetrics](../avvideoperformancemetrics.md)

# numberOfNonDisplayCompositedVideoFrames

<sub>Instance Property</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly) unsigned long numberOfNonDisplayCompositedVideoFrames;
```

## Discussion

[SPI] The total number of frames that were composited in undetached mode.

## See Also

### Inspecting metrics

- [numberOfCorruptedFrames](numberofcorruptedframes.md) — The total number of corrupted frames.
- [numberOfCorruptedVideoFrames](numberofcorruptedvideoframes.md)
- [numberOfDisplayCompositedVideoFrames](numberofdisplaycompositedvideoframes.md)
- [numberOfDroppedFrames](numberofdroppedframes.md) — The total number of frames the system drops prior to decoding or from missing the display deadline.
- [numberOfDroppedVideoFrames](numberofdroppedvideoframes.md)
- [numberOfFramesDisplayedUsingOptimizedCompositing](numberofframesdisplayedusingoptimizedcompositing.md) — The total number of full screen frames rendered in a special power-efficient mode that didn’t require compositing with other UI elements.
- [totalAccumulatedFrameDelay](totalaccumulatedframedelay.md) — The accumulated amount of time between the prescribed presentation times of displayed video frames and their actual time of display.
- [totalFrameDelay](totalframedelay.md)
- [totalNumberOfFrames](totalnumberofframes.md) — The total number of frames that display if no frames drop.
- [totalNumberOfVideoFrames](totalnumberofvideoframes.md)

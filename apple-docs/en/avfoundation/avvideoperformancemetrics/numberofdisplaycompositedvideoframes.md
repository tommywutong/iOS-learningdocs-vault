---
title: numberOfDisplayCompositedVideoFrames
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideoperformancemetrics/numberofdisplaycompositedvideoframes
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideoperformancemetrics/numberofdisplaycompositedvideoframes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideoperformancemetrics/numberofdisplaycompositedvideoframes.json'
content_hash: 'sha256:d18c2fb9049b434e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoPerformanceMetrics](../avvideoperformancemetrics.md)

# numberOfDisplayCompositedVideoFrames

<sub>Instance Property</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly) unsigned long numberOfDisplayCompositedVideoFrames;
```

## Discussion

[SPI] The total number of frames that were composited in detached mode.  Same as numberOfFramesDisplayedUsingOptimizedCompositing.

## See Also

### Inspecting metrics

- [numberOfCorruptedFrames](numberofcorruptedframes.md) — The total number of corrupted frames.
- [numberOfCorruptedVideoFrames](numberofcorruptedvideoframes.md)
- [numberOfDroppedFrames](numberofdroppedframes.md) — The total number of frames the system drops prior to decoding or from missing the display deadline.
- [numberOfDroppedVideoFrames](numberofdroppedvideoframes.md)
- [numberOfFramesDisplayedUsingOptimizedCompositing](numberofframesdisplayedusingoptimizedcompositing.md) — The total number of full screen frames rendered in a special power-efficient mode that didn’t require compositing with other UI elements.
- [numberOfNonDisplayCompositedVideoFrames](numberofnondisplaycompositedvideoframes.md)
- [totalAccumulatedFrameDelay](totalaccumulatedframedelay.md) — The accumulated amount of time between the prescribed presentation times of displayed video frames and their actual time of display.
- [totalFrameDelay](totalframedelay.md)
- [totalNumberOfFrames](totalnumberofframes.md) — The total number of frames that display if no frames drop.
- [totalNumberOfVideoFrames](totalnumberofvideoframes.md)

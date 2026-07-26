---
title: maxSupportedBufferedFrameCount
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avcapturebroadcastvideooutput/maxsupportedbufferedframecount
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturebroadcastvideooutput/maxsupportedbufferedframecount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturebroadcastvideooutput/maxsupportedbufferedframecount.json'
content_hash: 'sha256:686f86916e806ed3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureBroadcastVideoOutput](../avcapturebroadcastvideooutput.md)

# maxSupportedBufferedFrameCount

<sub>Type Property</sub>

The maximum value supported for maxBufferedFrameCount.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class var maxSupportedBufferedFrameCount: Int { get }
```

## Discussion

This class property returns the system-imposed limit for buffered frame count to ensure optimal performance and memory usage in broadcast workflows. The limit is determined based on system capabilities.

## See Also

### Related Documentation

- [maxBufferedFrameCount](maxbufferedframecount.md) — This represents the maximum count of buffered frames. By default the value is 0, which means late frames are immediately dropped to maintain minimal latency. _(beta)_

### Managing Video Output

- [videoSettings](videosettings.md) — The current video output settings for the broadcast video output. _(beta)_
- [maxBufferedFrameCount](maxbufferedframecount.md) — This represents the maximum count of buffered frames. By default the value is 0, which means late frames are immediately dropped to maintain minimal latency. _(beta)_
- [- resetFrameBuffer](<resetframebuffer().md>) — Tells the broadcast video output to reset the frame buffer and drop all currently buffered frames. _(beta)_
- [droppedFrameReplacementPolicy](droppedframereplacementpolicy-swift.property.md) — The strategy used to replace dropped video frames. _(beta)_

---
title: droppedFrameReplacementPolicy
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avcapturebroadcastvideooutput/droppedframereplacementpolicy-swift.property
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturebroadcastvideooutput/droppedframereplacementpolicy-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturebroadcastvideooutput/droppedframereplacementpolicy-swift.property.json'
content_hash: 'sha256:91c6edfa829fd4a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureBroadcastVideoOutput](../avcapturebroadcastvideooutput.md)

# droppedFrameReplacementPolicy

<sub>Instance Property</sub>

The strategy used to replace dropped video frames.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var droppedFrameReplacementPolicy: AVCaptureBroadcastVideoOutput.DroppedFrameReplacementPolicy { get set }
```

## Discussion

This property determines how the broadcast video output handles dropped frames. The default value is `AVCaptureBroadcastVideoOutputDroppedFrameReplacementPolicyRepeatPreviousFrame`.

## See Also

### Related Documentation

- [DroppedFrameReplacementPolicy](droppedframereplacementpolicy-swift.enum.md) — Constants indicating the replacement policy when a video frame is dropped. _(beta)_

### Managing Video Output

- [videoSettings](videosettings.md) — The current video output settings for the broadcast video output. _(beta)_
- [maxBufferedFrameCount](maxbufferedframecount.md) — This represents the maximum count of buffered frames. By default the value is 0, which means late frames are immediately dropped to maintain minimal latency. _(beta)_
- [maxSupportedBufferedFrameCount](maxsupportedbufferedframecount.md) — The maximum value supported for maxBufferedFrameCount. _(beta)_
- [- resetFrameBuffer](<resetframebuffer().md>) — Tells the broadcast video output to reset the frame buffer and drop all currently buffered frames. _(beta)_

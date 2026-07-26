---
title: videoSettings
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avcapturebroadcastvideooutput/videosettings
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturebroadcastvideooutput/videosettings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturebroadcastvideooutput/videosettings.json'
content_hash: 'sha256:f8e59f29257d2c68'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureBroadcastVideoOutput](../avcapturebroadcastvideooutput.md)

# videoSettings

<sub>Instance Property</sub>

The current video output settings for the broadcast video output.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var videoSettings: [String : Any]? { get }
```

## Discussion

This read-only property reports the actual video format and output settings currently being used for broadcast video output. The value is a dictionary containing metadata descriptors conforming to SMPTE ST 377 (Material Exchange Format) using Universal Labels (ULs) for professional broadcast interoperability.

The settings reflect the format negotiated between the camera capture pipeline and the connected broadcast video destination, taking into account:

- Camera native capture format capabilities
- Connected broadcast video destination capabilities
- System performance constraints
- Display transport bandwidth limitations

This property will return `nil` when no broadcast video destination is connected or when the output pipeline is not active.

> [!important] Important
> The reported settings reflect the actual negotiated format and may differ from the camera’s native capture format due to broadcast hardware constraints.

## See Also

### Managing Video Output

- [maxBufferedFrameCount](maxbufferedframecount.md) — This represents the maximum count of buffered frames. By default the value is 0, which means late frames are immediately dropped to maintain minimal latency. _(beta)_
- [maxSupportedBufferedFrameCount](maxsupportedbufferedframecount.md) — The maximum value supported for maxBufferedFrameCount. _(beta)_
- [- resetFrameBuffer](<resetframebuffer().md>) — Tells the broadcast video output to reset the frame buffer and drop all currently buffered frames. _(beta)_
- [droppedFrameReplacementPolicy](droppedframereplacementpolicy-swift.property.md) — The strategy used to replace dropped video frames. _(beta)_

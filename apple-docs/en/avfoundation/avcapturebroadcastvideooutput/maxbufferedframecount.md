---
title: maxBufferedFrameCount
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avcapturebroadcastvideooutput/maxbufferedframecount
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturebroadcastvideooutput/maxbufferedframecount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturebroadcastvideooutput/maxbufferedframecount.json'
content_hash: 'sha256:3b5d684414d8bb3d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureBroadcastVideoOutput](../avcapturebroadcastvideooutput.md)

# maxBufferedFrameCount

<sub>Instance Property</sub>

This represents the maximum count of buffered frames. By default the value is 0, which means late frames are immediately dropped to maintain minimal latency.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var maxBufferedFrameCount: Int { get set }
```

## Discussion

When set to a value greater than 0, the buffer absorbs minor timing jitter in the capture pipeline, reducing the possibility of dropping frames during temporary processing variations. Frames accumulate in the buffer up to the specified limit. Once the buffer reaches [maxBufferedFrameCount](maxbufferedframecount.md), the oldest frame is removed to make room for each new incoming frame, maintaining a rolling window of buffered content.

Calling [- resetFrameBuffer](<resetframebuffer().md>) clears all buffered frames and resets the buffer count back to 0, allowing the buffer to fill again from empty.

The maximum supported value can be retrieved using [maxSupportedBufferedFrameCount](maxsupportedbufferedframecount.md). Setting a value higher than the maximum supported value will raise an `NSInvalidArgumentException`.

> [!note] Note
> Enabling frame buffering (setting a value \> 0) is useful for scenarios where temporary processing delays or timing variations are acceptable, such as when recording or archiving broadcast content. For live broadcast workflows where minimal latency is critical, keep the default value of 0.

## See Also

### Related Documentation

- [- resetFrameBuffer](<resetframebuffer().md>) — Tells the broadcast video output to reset the frame buffer and drop all currently buffered frames. _(beta)_
- [maxSupportedBufferedFrameCount](maxsupportedbufferedframecount.md) — The maximum value supported for maxBufferedFrameCount. _(beta)_

### Managing Video Output

- [videoSettings](videosettings.md) — The current video output settings for the broadcast video output. _(beta)_
- [maxSupportedBufferedFrameCount](maxsupportedbufferedframecount.md) — The maximum value supported for maxBufferedFrameCount. _(beta)_
- [- resetFrameBuffer](<resetframebuffer().md>) — Tells the broadcast video output to reset the frame buffer and drop all currently buffered frames. _(beta)_
- [droppedFrameReplacementPolicy](droppedframereplacementpolicy-swift.property.md) — The strategy used to replace dropped video frames. _(beta)_

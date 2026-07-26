---
title: resetFrameBuffer()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avcapturebroadcastvideooutput/resetframebuffer()
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturebroadcastvideooutput/resetframebuffer()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturebroadcastvideooutput/resetframebuffer%28%29.json'
content_hash: 'sha256:34d02beae0e3db3c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureBroadcastVideoOutput](../avcapturebroadcastvideooutput.md)

# resetFrameBuffer()

<sub>Instance Method</sub>

Tells the broadcast video output to reset the frame buffer and drop all currently buffered frames.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func resetFrameBuffer()
```

## Discussion

This method can be called when buffered video frames should be dropped. This will force all those frames to be dropped and reset the buffered frame count to 0.

Use this method in scenarios where you need to clear pending frames, such as:

- **Pausing or stopping broadcast**: Drop pending frames that should not be transmitted
- **Reducing accumulated latency**: If buffering has built up significant delay, reset to return to real-time output

## See Also

### Related Documentation

- [maxBufferedFrameCount](maxbufferedframecount.md) — This represents the maximum count of buffered frames. By default the value is 0, which means late frames are immediately dropped to maintain minimal latency. _(beta)_

### Managing Video Output

- [videoSettings](videosettings.md) — The current video output settings for the broadcast video output. _(beta)_
- [maxBufferedFrameCount](maxbufferedframecount.md) — This represents the maximum count of buffered frames. By default the value is 0, which means late frames are immediately dropped to maintain minimal latency. _(beta)_
- [maxSupportedBufferedFrameCount](maxsupportedbufferedframecount.md) — The maximum value supported for maxBufferedFrameCount. _(beta)_
- [droppedFrameReplacementPolicy](droppedframereplacementpolicy-swift.property.md) — The strategy used to replace dropped video frames. _(beta)_

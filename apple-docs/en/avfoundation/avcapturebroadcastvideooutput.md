---
title: AVCaptureBroadcastVideoOutput
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avcapturebroadcastvideooutput
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturebroadcastvideooutput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturebroadcastvideooutput.json'
content_hash: 'sha256:48dfab03371daf2f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureBroadcastVideoOutput

<sub>Class</sub>

[AVCaptureBroadcastVideoOutput](avcapturebroadcastvideooutput.md) is a subclass of [AVCaptureOutput](avcaptureoutput.md) that delivers broadcast-quality video and ancillary data through the device’s DisplayPort hardware interface (USB-C DP Alt Mode)

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class AVCaptureBroadcastVideoOutput
```

## Overview

Not all [Format](avcapturedevice/format.md) instances support [AVCaptureBroadcastVideoOutput](avcapturebroadcastvideooutput.md). Before adding this output to a session, check the device format’s `AVCaptureDeviceFormat.unsupportedCaptureOutputClasses` property to verify that [AVCaptureBroadcastVideoOutput](avcapturebroadcastvideooutput.md) is not listed. If the current format does not support broadcast video output, the connection will be marked inactive and no samples will be delivered.

## Relationships

- **Inherits From**: [AVCaptureOutput](avcaptureoutput.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a broadcast video output

- [- init](<avcapturebroadcastvideooutput/init().md>) _(beta)_

### Managing the Output

- [delegate](avcapturebroadcastvideooutput/delegate.md) — The receiver’s delegate. _(beta)_
- [delegateCallbackQueue](avcapturebroadcastvideooutput/delegatecallbackqueue.md) — The dispatch queue on which all [AVCaptureBroadcastVideoOutputDelegate](avcapturebroadcastvideooutputdelegate.md) methods will be called. _(beta)_
- [- setDelegate:queue:](<avcapturebroadcastvideooutput/setdelegate(__queue_).md>) — Sets the receiver’s delegate and the dispatch queue on which the delegate will be called. _(beta)_

### Managing Video Output

- [videoSettings](avcapturebroadcastvideooutput/videosettings.md) — The current video output settings for the broadcast video output. _(beta)_
- [maxBufferedFrameCount](avcapturebroadcastvideooutput/maxbufferedframecount.md) — This represents the maximum count of buffered frames. By default the value is 0, which means late frames are immediately dropped to maintain minimal latency. _(beta)_
- [maxSupportedBufferedFrameCount](avcapturebroadcastvideooutput/maxsupportedbufferedframecount.md) — The maximum value supported for maxBufferedFrameCount. _(beta)_
- [- resetFrameBuffer](<avcapturebroadcastvideooutput/resetframebuffer().md>) — Tells the broadcast video output to reset the frame buffer and drop all currently buffered frames. _(beta)_
- [droppedFrameReplacementPolicy](avcapturebroadcastvideooutput/droppedframereplacementpolicy-swift.property.md) — The strategy used to replace dropped video frames. _(beta)_

### Dropped Frame Replacement

- [DroppedFrameReplacementPolicy](avcapturebroadcastvideooutput/droppedframereplacementpolicy-swift.enum.md) — Constants indicating the replacement policy when a video frame is dropped. _(beta)_

### Type Methods

- [+ new](<avcapturebroadcastvideooutput/new().md>) _(beta)_

## See Also

### Related Documentation

- [AVCaptureBroadcastVideoOutputDelegate](avcapturebroadcastvideooutputdelegate.md) — Protocol for receiving broadcast video output events and data. _(beta)_

### Broadcast video output

- [AVCaptureBroadcastVideoOutputDelegate](avcapturebroadcastvideooutputdelegate.md) — Protocol for receiving broadcast video output events and data. _(beta)_

---
title: AVCaptureBroadcastVideoOutputDelegate
framework: AVFoundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avcapturebroadcastvideooutputdelegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturebroadcastvideooutputdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturebroadcastvideooutputdelegate.json'
content_hash: 'sha256:3fc27afa875e3b6c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureBroadcastVideoOutputDelegate

<sub>Protocol</sub>

Protocol for receiving broadcast video output events and data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
protocol AVCaptureBroadcastVideoOutputDelegate : NSObjectProtocol
```

## Overview

Objects conforming to this protocol can be set as delegates to receive notifications about broadcast video output operations, including dropped frames and ancillary data processing.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Responding to dropped frames

- [- broadcastVideoOutput:didDropVideoFrameWithPresentationTimeStamp:fromConnection:](<avcapturebroadcastvideooutputdelegate/broadcastvideooutput(__diddropvideoframewithpresentationtimestamp_from_).md>) — Called when a video frame is dropped during broadcast video output processing. _(beta)_

## See Also

### Broadcast video output

- [AVCaptureBroadcastVideoOutput](avcapturebroadcastvideooutput.md) — [AVCaptureBroadcastVideoOutput](avcapturebroadcastvideooutput.md) is a subclass of [AVCaptureOutput](avcaptureoutput.md) that delivers broadcast-quality video and ancillary data through the device’s DisplayPort hardware interface (USB-C DP Alt Mode) _(beta)_

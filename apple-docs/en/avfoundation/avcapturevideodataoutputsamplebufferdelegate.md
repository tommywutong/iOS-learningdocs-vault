---
title: AVCaptureVideoDataOutputSampleBufferDelegate
framework: AVFoundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturevideodataoutputsamplebufferdelegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutputsamplebufferdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideodataoutputsamplebufferdelegate.json'
content_hash: 'sha256:5774452f50e30f4a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureVideoDataOutputSampleBufferDelegate

<sub>Protocol</sub>

Methods for receiving sample buffers from, and monitoring the status of, a video data output.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol AVCaptureVideoDataOutputSampleBufferDelegate : NSObjectProtocol
```

## Overview

This protocol defines an interface for delegates of an [AVCaptureVideoDataOutput](avcapturevideodataoutput.md) object to receive captured video sample buffers and be notified of late sample buffers that were dropped.

The delegate of an [AVCaptureVideoDataOutput](avcapturevideodataoutput.md) object must adopt the `AVCaptureVideoDataOutputSampleBufferDelegate` protocol. The methods in this protocol are optional.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Managing sample buffer behavior

- [- captureOutput:didOutputSampleBuffer:fromConnection:](<avcapturevideodataoutputsamplebufferdelegate/captureoutput(__didoutput_from_).md>) — Notifies the delegate that a new video frame was written.
- [- captureOutput:didDropSampleBuffer:fromConnection:](<avcapturevideodataoutputsamplebufferdelegate/captureoutput(__diddrop_from_).md>) — Notifies the delegate that a video frame was discarded.

## See Also

### Receiving captured video data

- [- setSampleBufferDelegate:queue:](<avcapturevideodataoutput/setsamplebufferdelegate(__queue_).md>) — Sets the sample buffer delegate and the queue for invoking callbacks.
- [sampleBufferDelegate](avcapturevideodataoutput/samplebufferdelegate.md) — The capture object’s delegate.
- [sampleBufferCallbackQueue](avcapturevideodataoutput/samplebuffercallbackqueue.md) — The queue on which the system invokes delegate callbacks.

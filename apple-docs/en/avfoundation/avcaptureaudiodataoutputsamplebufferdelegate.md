---
title: AVCaptureAudioDataOutputSampleBufferDelegate
framework: AVFoundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureaudiodataoutputsamplebufferdelegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutputsamplebufferdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureaudiodataoutputsamplebufferdelegate.json'
content_hash: 'sha256:a5613816d76af4be'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureAudioDataOutputSampleBufferDelegate

<sub>Protocol</sub>

Methods for receiving audio sample data from an audio capture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
protocol AVCaptureAudioDataOutputSampleBufferDelegate : NSObjectProtocol
```

## Overview

This protocol defines an interface for delegates of an [AVCaptureAudioDataOutput](avcaptureaudiodataoutput.md) object to receive captured audio sample buffers.

The delegate of an [AVCaptureAudioDataOutput](avcaptureaudiodataoutput.md) object must adopt this protocol. The method in this protocol is optional.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Managing sample buffer behavior

- [- captureOutput:didOutputSampleBuffer:fromConnection:](<avcaptureaudiodataoutputsamplebufferdelegate/captureoutput(__didoutput_from_).md>) — Notifies the delegate that a sample buffer was written.

## See Also

### Receiving captured audio data

- [- setSampleBufferDelegate:queue:](<avcaptureaudiodataoutput/setsamplebufferdelegate(__queue_).md>) — Sets the delegate that will accept captured buffers and the dispatch queue on which the delegate will be called.
- [sampleBufferDelegate](avcaptureaudiodataoutput/samplebufferdelegate.md) — The capture object’s delegate.
- [sampleBufferCallbackQueue](avcaptureaudiodataoutput/samplebuffercallbackqueue.md) — The queue on which delegate callbacks are invoked

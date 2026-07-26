---
title: sampleBufferCallbackQueue
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureaudiodataoutput/samplebuffercallbackqueue
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutput/samplebuffercallbackqueue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureaudiodataoutput/samplebuffercallbackqueue.json'
content_hash: 'sha256:b5025cc5ced56067'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureAudioDataOutput](../avcaptureaudiodataoutput.md)

# sampleBufferCallbackQueue

<sub>Instance Property</sub>

The queue on which delegate callbacks are invoked

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var sampleBufferCallbackQueue: dispatch_queue_t? { get }
```

## See Also

### Receiving captured audio data

- [- setSampleBufferDelegate:queue:](<setsamplebufferdelegate(__queue_).md>) — Sets the delegate that will accept captured buffers and the dispatch queue on which the delegate will be called.
- [sampleBufferDelegate](samplebufferdelegate.md) — The capture object’s delegate.
- [AVCaptureAudioDataOutputSampleBufferDelegate](../avcaptureaudiodataoutputsamplebufferdelegate.md) — Methods for receiving audio sample data from an audio capture.

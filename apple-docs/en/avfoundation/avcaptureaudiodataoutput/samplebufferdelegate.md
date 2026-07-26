---
title: sampleBufferDelegate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureaudiodataoutput/samplebufferdelegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutput/samplebufferdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureaudiodataoutput/samplebufferdelegate.json'
content_hash: 'sha256:087d904ca33047b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureAudioDataOutput](../avcaptureaudiodataoutput.md)

# sampleBufferDelegate

<sub>Instance Property</sub>

The capture object’s delegate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var sampleBufferDelegate: (any AVCaptureAudioDataOutputSampleBufferDelegate)? { get }
```

## Discussion

You use the delegate to manage incoming data.

## See Also

### Receiving captured audio data

- [- setSampleBufferDelegate:queue:](<setsamplebufferdelegate(__queue_).md>) — Sets the delegate that will accept captured buffers and the dispatch queue on which the delegate will be called.
- [sampleBufferCallbackQueue](samplebuffercallbackqueue.md) — The queue on which delegate callbacks are invoked
- [AVCaptureAudioDataOutputSampleBufferDelegate](../avcaptureaudiodataoutputsamplebufferdelegate.md) — Methods for receiving audio sample data from an audio capture.

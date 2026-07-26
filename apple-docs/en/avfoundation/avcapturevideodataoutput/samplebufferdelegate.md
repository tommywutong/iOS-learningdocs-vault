---
title: sampleBufferDelegate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturevideodataoutput/samplebufferdelegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/samplebufferdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideodataoutput/samplebufferdelegate.json'
content_hash: 'sha256:ad0d00ecf3320dd7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureVideoDataOutput](../avcapturevideodataoutput.md)

# sampleBufferDelegate

<sub>Instance Property</sub>

The capture object’s delegate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var sampleBufferDelegate: (any AVCaptureVideoDataOutputSampleBufferDelegate)? { get }
```

## Discussion

The delegate receives sample buffers after they are captured.

You set the delegate using [- setSampleBufferDelegate:queue:](<setsamplebufferdelegate(__queue_).md>).

## See Also

### Receiving captured video data

- [- setSampleBufferDelegate:queue:](<setsamplebufferdelegate(__queue_).md>) — Sets the sample buffer delegate and the queue for invoking callbacks.
- [sampleBufferCallbackQueue](samplebuffercallbackqueue.md) — The queue on which the system invokes delegate callbacks.
- [AVCaptureVideoDataOutputSampleBufferDelegate](../avcapturevideodataoutputsamplebufferdelegate.md) — Methods for receiving sample buffers from, and monitoring the status of, a video data output.

---
title: sampleBufferCallbackQueue
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturevideodataoutput/samplebuffercallbackqueue
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/samplebuffercallbackqueue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideodataoutput/samplebuffercallbackqueue.json'
content_hash: 'sha256:834b624af18c095c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureVideoDataOutput](../avcapturevideodataoutput.md)

# sampleBufferCallbackQueue

<sub>Instance Property</sub>

The queue on which the system invokes delegate callbacks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var sampleBufferCallbackQueue: dispatch_queue_t? { get }
```

## Discussion

You set the queue using [- setSampleBufferDelegate:queue:](<setsamplebufferdelegate(__queue_).md>).

## See Also

### Receiving captured video data

- [- setSampleBufferDelegate:queue:](<setsamplebufferdelegate(__queue_).md>) — Sets the sample buffer delegate and the queue for invoking callbacks.
- [sampleBufferDelegate](samplebufferdelegate.md) — The capture object’s delegate.
- [AVCaptureVideoDataOutputSampleBufferDelegate](../avcapturevideodataoutputsamplebufferdelegate.md) — Methods for receiving sample buffers from, and monitoring the status of, a video data output.

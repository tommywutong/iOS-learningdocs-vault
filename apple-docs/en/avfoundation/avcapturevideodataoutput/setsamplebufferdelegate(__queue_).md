---
title: 'setSampleBufferDelegate(_:queue:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturevideodataoutput/setsamplebufferdelegate(_:queue:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/setsamplebufferdelegate(_:queue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideodataoutput/setsamplebufferdelegate%28_%3Aqueue%3A%29.json'
content_hash: 'sha256:259b988bef533b55'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureVideoDataOutput](../avcapturevideodataoutput.md)

# setSampleBufferDelegate(_:queue:)

<sub>Instance Method</sub>

Sets the sample buffer delegate and the queue for invoking callbacks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setSampleBufferDelegate(_ sampleBufferDelegate: (any AVCaptureVideoDataOutputSampleBufferDelegate)?, queue sampleBufferCallbackQueue: dispatch_queue_t?)
```

## Parameters

- `sampleBufferDelegate` — An object conforming to the [AVCaptureVideoDataOutputSampleBufferDelegate](../avcapturevideodataoutputsamplebufferdelegate.md) protocol that will receive sample buffers after they are captured.

- `sampleBufferCallbackQueue` — The queue on which callbacks should be invoked. You must use a serial dispatch queue, to guarantee that video frames will be delivered in order. The sampleBufferCallbackQueue parameter may not be `NULL`, except when setting the `sampleBufferDelegate` to `nil`.

## Discussion

When a new video sample buffer is captured, it is sent to the sample buffer delegate using [- captureOutput:didOutputSampleBuffer:fromConnection:](<../avcapturevideodataoutputsamplebufferdelegate/captureoutput(__didoutput_from_).md>). All delegate methods are invoked on the specified dispatch queue.

If the queue is blocked when new frames are captured, those frames will be automatically dropped at a time determined by the value of the [alwaysDiscardsLateVideoFrames](alwaysdiscardslatevideoframes.md) property. This allows you to process existing frames on the same queue without having to manage the potential memory usage increases that would otherwise occur when that processing is unable to keep up with the rate of incoming frames.

If your frame processing is consistently unable to keep up with the rate of incoming frames, you should consider using the [minFrameDuration](minframeduration.md) property, which will generally yield better performance characteristics and more consistent frame rates than frame dropping alone.

If you need to minimize the chances of frames being dropped, you should specify a queue on which a sufficiently small amount of processing is being done outside of receiving sample buffers. However, if you migrate extra processing to another queue, you are responsible for ensuring that memory usage does not grow without bound from frames that have not been processed.

### Special considerations

This method uses [dispatch_retain](../../dispatch/dispatch_retain.md) and [dispatch_release](../../dispatch/dispatch_release.md) to manage the queue.

## See Also

### Receiving captured video data

- [sampleBufferDelegate](samplebufferdelegate.md) — The capture object’s delegate.
- [sampleBufferCallbackQueue](samplebuffercallbackqueue.md) — The queue on which the system invokes delegate callbacks.
- [AVCaptureVideoDataOutputSampleBufferDelegate](../avcapturevideodataoutputsamplebufferdelegate.md) — Methods for receiving sample buffers from, and monitoring the status of, a video data output.

---
title: 'captureOutput(_:didOutput:from:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturevideodataoutputsamplebufferdelegate/captureoutput(_:didoutput:from:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutputsamplebufferdelegate/captureoutput(_:didoutput:from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideodataoutputsamplebufferdelegate/captureoutput%28_%3Adidoutput%3Afrom%3A%29.json'
content_hash: 'sha256:a576d8e8ef5974b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureVideoDataOutputSampleBufferDelegate](../avcapturevideodataoutputsamplebufferdelegate.md)

# captureOutput(_:didOutput:from:)

<sub>Instance Method</sub>

Notifies the delegate that a new video frame was written.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func captureOutput(_ output: AVCaptureOutput, didOutput sampleBuffer: CMSampleBuffer, from connection: AVCaptureConnection)
```

## Parameters

- `output` — The capture output object.

- `sampleBuffer` — A `CMSampleBuffer` object containing the video frame data and additional information about the frame, such as its format and presentation time.

- `connection` — The connection from which the video was received.

## Discussion

Delegates receive this message whenever the output captures and outputs a new video frame, decoding or re-encoding it as specified by its `videoSettings` property. Delegates can use the provided video frame in conjunction with other APIs for further processing.

This method is called on the dispatch queue specified by the output’s [sampleBufferCallbackQueue](../avcapturevideodataoutput/samplebuffercallbackqueue.md) property. It is called periodically, so it must be efficient to prevent capture performance problems, including dropped frames.

If you need to reference the `CMSampleBuffer` object outside of the scope of this method, you must `CFRetain` it and then `CFRelease` it when you are finished with it.

To maintain optimal performance, some sample buffers directly reference pools of memory that may need to be reused by the device system and other capture inputs. This is frequently the case for uncompressed device native capture where memory blocks are copied as little as possible. If multiple sample buffers reference such pools of memory for too long, inputs will no longer be able to copy new samples into memory and those samples will be dropped.

If your application is causing samples to be dropped by retaining the provided [CMSampleBuffer](../../coremedia/cmsamplebuffer.md) objects for too long, but it needs access to the sample data for a long period of time, consider copying the data into a new buffer and then releasing the sample buffer (if it was previously retained) so that the memory it references can be reused.

## See Also

### Managing sample buffer behavior

- [- captureOutput:didDropSampleBuffer:fromConnection:](<captureoutput(__diddrop_from_).md>) — Notifies the delegate that a video frame was discarded.

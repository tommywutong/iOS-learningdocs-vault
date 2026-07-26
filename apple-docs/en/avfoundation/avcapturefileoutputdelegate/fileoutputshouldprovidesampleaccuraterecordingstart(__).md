---
title: 'fileOutputShouldProvideSampleAccurateRecordingStart(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.8+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturefileoutputdelegate/fileoutputshouldprovidesampleaccuraterecordingstart(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturefileoutputdelegate/fileoutputshouldprovidesampleaccuraterecordingstart(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturefileoutputdelegate/fileoutputshouldprovidesampleaccuraterecordingstart%28_%3A%29.json'
content_hash: 'sha256:0ee132494e56a1d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureFileOutputDelegate](../avcapturefileoutputdelegate.md)

# fileOutputShouldProvideSampleAccurateRecordingStart(_:)

<sub>Instance Method</sub>

Allows a client to opt in to frame accurate recording in [- captureOutput:didOutputSampleBuffer:fromConnection:](<fileoutput(__didoutputsamplebuffer_from_).md>).

<sub>macOS</sub>

```swift
func fileOutputShouldProvideSampleAccurateRecordingStart(_ output: AVCaptureFileOutput) -> Bool
```

## Parameters

- `output` — The capture file output instance that is associated with the delegate.

## Return Value

[true](../../swift/true.md) if frame accurate recording is required; otherwise [false](../../swift/false.md).

## Discussion

In apps linked before OS X Mountain Lion, delegates that implement the [- captureOutput:didOutputSampleBuffer:fromConnection:](<fileoutput(__didoutputsamplebuffer_from_).md>) method can ensure that starting and stopping a recording is frame accurate by calling [- startRecordingToOutputFileURL:recordingDelegate:](<../avcapturefileoutput/startrecording(to_recordingdelegate_).md>) or [- stopRecording](<../avcapturefileoutput/stoprecording().md>) from within the callback. Frame accurate recording requires the capture output to apply outputSettings when the session starts running, so it is ready to start and/or stop recording on any given frame boundary. Applying compression settings for the entire length of the session has power, thermal, and CPU implications.

In apps linked on or after OS X Mountain Lion, delegates must implement this method to indicate whether frame accurate recording is required. The capture file output calls this method only once when the delegate is added and never again. If your delegate returns [false](../../swift/false.md), the capture file output applies compression settings only when [- startRecordingToOutputFileURL:recordingDelegate:](<../avcapturefileoutput/startrecording(to_recordingdelegate_).md>) is called and disables these settings once the recording stops.

## See Also

### Sample processing

- [- captureOutput:didOutputSampleBuffer:fromConnection:](<fileoutput(__didoutputsamplebuffer_from_).md>) — Gives the delegate the opportunity to inspect samples as they are received by the output and start and stop recording at exact times.

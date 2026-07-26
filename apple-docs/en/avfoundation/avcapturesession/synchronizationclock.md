---
title: synchronizationClock
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.4+, iPadOS 15.4+, Mac Catalyst 15.4+, macOS 12.3+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesession/synchronizationclock
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/synchronizationclock'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/synchronizationclock.json'
content_hash: 'sha256:78dbb39091700433'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# synchronizationClock

<sub>Instance Property</sub>

A clock to use for output synchronization.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var synchronizationClock: CMClock? { get }
```

## Discussion

All capture output sample buffer timestamps are on the synchronization clock’s timebase. Use this clock in conjunction with the clock from an [Port](../avcaptureinput/port.md) object to synchronize capture output with external data sources such as Core Motion samples.

The example below shows how to reverse synchronize the output timestamps to the original timestamps in the [- captureOutput:didOutputSampleBuffer:fromConnection:](<../avcapturevideodataoutputsamplebufferdelegate/captureoutput(__didoutput_from_).md>) method:

```swift
func captureOutput(_ output: AVCaptureOutput, didOutput sampleBuffer: CMSampleBuffer, from connection: AVCaptureConnection) {
    // Get the original and capture session clocks.
    guard let port = connection.inputPorts.first,
          let originalClock = port.clock,
          let sessionClock = captureSession?.synchronizationClock else { return }
        
    // Get the presentation timestamp of the current sample buffer.
    let syncedPTS = sampleBuffer.presentationTimeStamp
        
    // Convert the timestamp to the original timebase.
    let originalPTS = sessionClock.convertTime(syncedPTS, to: originalClock)
}
```

This property is key-value observable.

## See Also

### Synchronizing output

- [masterClock](masterclock.md) — A clock object used for output synchronization. _(deprecated)_

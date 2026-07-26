---
title: masterClock
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+（15.4 起废弃）, iPadOS 7.0+（15.4 起废弃）, Mac Catalyst 14.0+（15.4 起废弃）, macOS 10.9+（12.3 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturesession/masterclock
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/masterclock'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/masterclock.json'
content_hash: 'sha256:89525588056204ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# masterClock

<sub>Instance Property</sub>

A clock object used for output synchronization.

> [!warning] Deprecated
> Use [synchronizationClock](synchronizationclock.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var masterClock: CMClock? { get }
```

## Discussion

The returned [CMClock](../../coremedia/cmclock.md) object is read-only and provides a timebase for all sample buffers in capture output. Use this clock in conjunction with the clock from an [Port](../avcaptureinput/port.md) object to synchronize capture output with external data sources such as motion samples.

For example, to synchronize output timestamps to the original timestamps provided by an input device, you can do the following in your [- captureOutput:didOutputSampleBuffer:fromConnection:](<../avcapturefileoutputdelegate/fileoutput(__didoutputsamplebuffer_from_).md>) method:

```swift
guard let masterClock = captureSession.masterClock,
    let originalClock = connection.inputPorts.first?.clock else { return }

let synchedPTS = sampleBuffer.presentationTimeStamp
let originalPTS = masterClock.convertTime(synchedPTS, to: originalClock)
```

This property is key-value observable.

## See Also

### Synchronizing output

- [synchronizationClock](synchronizationclock.md) — A clock to use for output synchronization.

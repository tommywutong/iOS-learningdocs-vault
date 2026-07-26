---
title: isSignalCompensationDelaySupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avexternalsyncdevice/issignalcompensationdelaysupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avexternalsyncdevice/issignalcompensationdelaysupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avexternalsyncdevice/issignalcompensationdelaysupported.json'
content_hash: 'sha256:ee47bb33f6cb9186'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVExternalSyncDevice](../avexternalsyncdevice.md)

# isSignalCompensationDelaySupported

<sub>Instance Property</sub>

Whether adjusting the signal compensation delay property is currently supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isSignalCompensationDelaySupported: Bool { get }
```

## Discussion

This property returns `true` if the [signalCompensationDelay](signalcompensationdelay.md) can be adjusted.

[signalCompensationDelay](signalcompensationdelay.md) can be adjusted while the [AVCaptureSession](../avcapturesession.md) is not running.

Once the session is running, this property’s value depends on [adjustingSignalCompensationDelayWhileRunningSupported](../avcapturedevice/isadjustingsignalcompensationdelaywhilerunningsupported.md) of the [AVCaptureDevice](../avcapturedevice.md) backing the [AVCaptureDeviceInput](../avcapturedeviceinput.md) that is following this external sync device. Inspect that property in advance to determine whether [signalCompensationDelay](signalcompensationdelay.md) will remain adjustable while running on a given device.

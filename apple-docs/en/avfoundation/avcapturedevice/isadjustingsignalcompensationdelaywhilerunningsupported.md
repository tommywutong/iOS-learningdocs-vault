---
title: isAdjustingSignalCompensationDelayWhileRunningSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/isadjustingsignalcompensationdelaywhilerunningsupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/isadjustingsignalcompensationdelaywhilerunningsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/isadjustingsignalcompensationdelaywhilerunningsupported.json'
content_hash: 'sha256:5c5b7666a4371330'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# isAdjustingSignalCompensationDelayWhileRunningSupported

<sub>Instance Property</sub>

Whether adjusting the signal compensation delay property of an external sync device is supported while the session is running.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isAdjustingSignalCompensationDelayWhileRunningSupported: Bool { get }
```

## Discussion

This property returns `true` if the `signalCompensationDelay` of an [AVExternalSyncDevice](../avexternalsyncdevice.md) being followed by this device’s [AVCaptureDeviceInput](../avcapturedeviceinput.md) can be adjusted while the [AVCaptureSession](../avcapturesession.md) is running.

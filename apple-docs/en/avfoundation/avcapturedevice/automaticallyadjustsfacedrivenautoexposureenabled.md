---
title: automaticallyAdjustsFaceDrivenAutoExposureEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.4+, iPadOS 15.4+, Mac Catalyst 15.4+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/automaticallyadjustsfacedrivenautoexposureenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/automaticallyadjustsfacedrivenautoexposureenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/automaticallyadjustsfacedrivenautoexposureenabled.json'
content_hash: 'sha256:46d4854d292a15a0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# automaticallyAdjustsFaceDrivenAutoExposureEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the device automatically adjusts face-driven autoexposure.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var automaticallyAdjustsFaceDrivenAutoExposureEnabled: Bool { get set }
```

## Discussion

The value of this property defaults to [true](../../swift/true.md) for devices that support autoexposure. If your app requires explicitly setting the state of [faceDrivenAutoExposureEnabled](isfacedrivenautoexposureenabled.md), set this value to [false](../../swift/false.md).

To set this property value, you must call the device’s [- lockForConfiguration:](<lockforconfiguration().md>) method to obtain exclusive access to configure it. Otherwise, attempting to set a value raises an exception. When you finish configuring the device, call [- unlockForConfiguration](<unlockforconfiguration().md>) to release the lock.

## See Also

### Configuring face-driven automatic exposure

- [faceDrivenAutoExposureEnabled](isfacedrivenautoexposureenabled.md) — A Boolean value that indicates whether the device has face-driven autoexposure enabled.

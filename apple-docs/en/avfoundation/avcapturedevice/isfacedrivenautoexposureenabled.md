---
title: isFaceDrivenAutoExposureEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.4+, iPadOS 15.4+, Mac Catalyst 15.4+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/isfacedrivenautoexposureenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/isfacedrivenautoexposureenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/isfacedrivenautoexposureenabled.json'
content_hash: 'sha256:30471b729fa5f600'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# isFaceDrivenAutoExposureEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the device has face-driven autoexposure enabled.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isFaceDrivenAutoExposureEnabled: Bool { get set }
```

## Discussion

Face-driven autoexposure takes a subject’s face into account when performing automatic exposure adjustments. Enabling this feature can better expose subjects with darker skin tones or those who are backlit. For apps that link against iOS 15.4 or later, the value of this property defaults to [true](../../swift/true.md) for devices that support autoexposure.

Before setting a value for this property, perform the following:

- Obtain exclusive access to the device by calling its [- lockForConfiguration:](<lockforconfiguration().md>) method.
- Set the value of the device’s [automaticallyAdjustsFaceDrivenAutoExposureEnabled](automaticallyadjustsfacedrivenautoexposureenabled.md) property to [false](../../swift/false.md).

Attempting to set a value before performing these steps results in an exception.

When you finish configuring the device, unlock it by calling its [- unlockForConfiguration](<unlockforconfiguration().md>) method.

> [!important] Important
> Updating the state of this property doesn’t initiate an exposure change. After setting a new value, set an appropriate [exposureMode](exposuremode-swift.property.md) to apply the change.

## See Also

### Configuring face-driven automatic exposure

- [automaticallyAdjustsFaceDrivenAutoExposureEnabled](automaticallyadjustsfacedrivenautoexposureenabled.md) — A Boolean value that indicates whether the device automatically adjusts face-driven autoexposure.

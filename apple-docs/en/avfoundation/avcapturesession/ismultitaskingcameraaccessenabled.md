---
title: isMultitaskingCameraAccessEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesession/ismultitaskingcameraaccessenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/ismultitaskingcameraaccessenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/ismultitaskingcameraaccessenabled.json'
content_hash: 'sha256:274b545ca9f18a2a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# isMultitaskingCameraAccessEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the capture session enables access to the camera while multitasking.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isMultitaskingCameraAccessEnabled: Bool { get set }
```

## Discussion

The default value is [false](../../swift/false.md).

> [!important] Important
> For apps that have the [com.apple.developer.avfoundation.multitasking-camera-access](../../bundleresources/entitlements/com.apple.developer.avfoundation.multitasking-camera-access.md) entitlement, this property value defaults to [true](../../swift/true.md) if [multitaskingCameraAccessSupported](ismultitaskingcameraaccesssupported.md) is also [true](../../swift/true.md).

If the value of the [multitaskingCameraAccessSupported](ismultitaskingcameraaccesssupported.md) property is [true](../../swift/true.md), you can enable multitasking camera access by setting this value to [true](../../swift/true.md) prior to starting the capture session.

This property is key-value observable.

> [!note] Note
> If you enable multitasking camera access, the system doesn’t interrupt the capture session with a reason of [AVCaptureSessionInterruptionReasonVideoDeviceNotAvailableWithMultipleForegroundApps](interruptionreason/videodevicenotavailablewithmultipleforegroundapps.md).

To learn about best practices for using the camera while multitasking, see [Accessing the camera while multitasking on iPad](../../avkit/accessing-the-camera-while-multitasking-on-ipad.md).

## See Also

### Configuring multitasking

- [multitaskingCameraAccessSupported](ismultitaskingcameraaccesssupported.md) — A Boolean value that indicates whether the capture session supports using the camera while multitasking.

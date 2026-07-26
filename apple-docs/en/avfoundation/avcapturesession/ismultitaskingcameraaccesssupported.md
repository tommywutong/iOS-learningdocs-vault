---
title: isMultitaskingCameraAccessSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesession/ismultitaskingcameraaccesssupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/ismultitaskingcameraaccesssupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/ismultitaskingcameraaccesssupported.json'
content_hash: 'sha256:09a0da4517245894'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# isMultitaskingCameraAccessSupported

<sub>Instance Property</sub>

A Boolean value that indicates whether the capture session supports using the camera while multitasking.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isMultitaskingCameraAccessSupported: Bool { get }
```

## Discussion

Query this property to determine whether you can use the camera while multitasking by setting the state of the [multitaskingCameraAccessEnabled](ismultitaskingcameraaccessenabled.md) property to `true`.

In iOS and iPadOS, this property is `true` for any of the following cases:

- The app runs on an iPad that supports Stage Manager with an extended display.
- The app links against iOS 18 or later and uses `voip` as one of its [UIBackgroundModes](../../bundleresources/information-property-list/uibackgroundmodes.md).
- The app has the [com.apple.developer.avfoundation.multitasking-camera-access](../../bundleresources/entitlements/com.apple.developer.avfoundation.multitasking-camera-access.md) entitlement.

In tvOS, this property is always `true`.

> [!note] Note
> This property is key-value observable. If the value changes from `true` to `false`, the value of [multitaskingCameraAccessEnabled](ismultitaskingcameraaccessenabled.md) also changes to `false`.

To learn about best practices for using the camera while multitasking, see [Accessing the camera while multitasking on iPad](../../avkit/accessing-the-camera-while-multitasking-on-ipad.md).

## See Also

### Configuring multitasking

- [multitaskingCameraAccessEnabled](ismultitaskingcameraaccessenabled.md) — A Boolean value that indicates whether the capture session enables access to the camera while multitasking.

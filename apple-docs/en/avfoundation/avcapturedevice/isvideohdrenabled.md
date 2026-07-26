---
title: isVideoHDREnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/isvideohdrenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/isvideohdrenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/isvideohdrenabled.json'
content_hash: 'sha256:31367825e5bc052d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# isVideoHDREnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the device streams high dynamic range video buffers, also known as extended dynamic range (EDR).

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isVideoHDREnabled: Bool { get set }
```

## Discussion

The device ignores the value of this property when [activeColorSpace](activecolorspace.md) is HLG BT2020 color space because HDR is effectively always on and can’t be disabled.

Before changing the value of this property, you must call [- lockForConfiguration:](<lockforconfiguration().md>) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you finish configuring the device, call [- unlockForConfiguration](<unlockforconfiguration().md>) to release the lock and allow other devices to configure the settings.

Note that setting this property may cause a lengthy reconfiguration of the device, similar to setting a new active format or capture session preset. If you’re setting either the active format or the [sessionPreset](../avcapturesession/sessionpreset.md) _and_ this property, you should bracket these operations with [- beginConfiguration](<../avcapturesession/beginconfiguration().md>) and session [- commitConfiguration](<../avcapturesession/commitconfiguration().md>) to minimize reconfiguration time.

This property is key-value observable.

## See Also

### Configuring HDR settings

- [automaticallyAdjustsVideoHDREnabled](automaticallyadjustsvideohdrenabled.md) — A Boolean value that indicates whether the device automatically manages the state of high dynamic range (HDR) video streaming.

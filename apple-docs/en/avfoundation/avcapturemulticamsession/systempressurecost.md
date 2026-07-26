---
title: systemPressureCost
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturemulticamsession/systempressurecost
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturemulticamsession/systempressurecost'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturemulticamsession/systempressurecost.json'
content_hash: 'sha256:5cf6c45d182f8636'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureMultiCamSession](../avcapturemulticamsession.md)

# systemPressureCost

<sub>Instance Property</sub>

A value that indicates the system pressure cost of the current session configuration.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var systemPressureCost: Float { get }
```

## Discussion

The session’s system pressure cost value, ranging from `0.0` to `1.0`, indicates the cost of running the current session configuration. When the value exceeds `1.0`, the capture session cannot run sustainably, but it may be able to run briefly before stopping. While the session is running in an unsustainable configuration, you may monitor the device’s [systemPressureState](../avcapturedevice/systempressurestate-swift.property.md) and reduce pressure by reducing the frame rate, throttling your use of the GPU, and so on.

When the session reaches a critical system pressure state, it temporarily shuts down, and your app receives an [AVCaptureSessionWasInterruptedNotification](../avcapturesession/wasinterruptednotification.md) notification indicating the reason your session stopped. When system pressure is alleviated, the session interruption ends.

## See Also

### Managing resources

- [hardwareCost](hardwarecost.md) — A value that indicates the percentage of the session’s available hardware budget currently in use.

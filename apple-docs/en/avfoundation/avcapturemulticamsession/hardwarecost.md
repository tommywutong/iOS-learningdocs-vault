---
title: hardwareCost
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturemulticamsession/hardwarecost
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturemulticamsession/hardwarecost'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturemulticamsession/hardwarecost.json'
content_hash: 'sha256:82429d6c6453e657'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureMultiCamSession](../avcapturemulticamsession.md)

# hardwareCost

<sub>Instance Property</sub>

A value that indicates the percentage of the session’s available hardware budget currently in use.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var hardwareCost: Float { get }
```

## Discussion

The capture session takes into account the currently connected inputs, outputs, and enabled features to calculate the hardware cost. This value represents the percentage of the hardware in use, normalized to a range of `0.0` to `1.0`. When the value is greater than `1.0`, the capture session cannot run your configuration due to hardware constraints. In this case, you receive an [AVCaptureSessionRuntimeErrorNotification](../avcapturesession/runtimeerrornotification.md) when you attempt to start the session.

The default value of this property is `0.0`.

## See Also

### Managing resources

- [systemPressureCost](systempressurecost.md) — A value that indicates the system pressure cost of the current session configuration.

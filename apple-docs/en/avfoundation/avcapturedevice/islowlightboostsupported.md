---
title: isLowLightBoostSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/islowlightboostsupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/islowlightboostsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/islowlightboostsupported.json'
content_hash: 'sha256:bb14eef9671f99f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# isLowLightBoostSupported

<sub>Instance Property</sub>

A Boolean value that indicates whether the capture device supports boosting images in low-light conditions.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isLowLightBoostSupported: Bool { get }
```

## Discussion

You can set the capture device’s [automaticallyEnablesLowLightBoostWhenAvailable](automaticallyenableslowlightboostwhenavailable.md) property only if this property is [true](../../swift/true.md).

This property is key-value observable.

## See Also

### Configuring low light settings

- [lowLightBoostEnabled](islowlightboostenabled.md) — A Boolean value that indicates whether the capture device’s low light boost feature is in an enabled state.
- [automaticallyEnablesLowLightBoostWhenAvailable](automaticallyenableslowlightboostwhenavailable.md) — A Boolean value that indicates whether the capture device automatically switches to low-light boost mode when necessary.

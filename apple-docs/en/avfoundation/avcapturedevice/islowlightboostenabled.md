---
title: isLowLightBoostEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/islowlightboostenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/islowlightboostenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/islowlightboostenabled.json'
content_hash: 'sha256:d5a1ae68afb06e2e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# isLowLightBoostEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the capture device’s low light boost feature is in an enabled state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isLowLightBoostEnabled: Bool { get }
```

## Discussion

The value of this property indicates whether the capture device currently enhancing images to improve quality due to low light conditions. When this property is [true](../../swift/true.md), the capture device has switched into a special mode in which it perceives more light in images.

This property is key-value observable.

## See Also

### Configuring low light settings

- [lowLightBoostSupported](islowlightboostsupported.md) — A Boolean value that indicates whether the capture device supports boosting images in low-light conditions.
- [automaticallyEnablesLowLightBoostWhenAvailable](automaticallyenableslowlightboostwhenavailable.md) — A Boolean value that indicates whether the capture device automatically switches to low-light boost mode when necessary.

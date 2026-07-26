---
title: isCameraIntrinsicMatrixDeliverySupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureconnection/iscameraintrinsicmatrixdeliverysupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureconnection/iscameraintrinsicmatrixdeliverysupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureconnection/iscameraintrinsicmatrixdeliverysupported.json'
content_hash: 'sha256:6f774d2ac72bfd5c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureConnection](../avcaptureconnection.md)

# isCameraIntrinsicMatrixDeliverySupported

<sub>Instance Property</sub>

A Boolean value that indicates whether the capture connection currently supports delivering camera intrinsics information.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isCameraIntrinsicMatrixDeliverySupported: Bool { get }
```

## Discussion

A value of [true](../../swift/true.md) means you can set [cameraIntrinsicMatrixDeliveryEnabled](iscameraintrinsicmatrixdeliveryenabled.md) to [true](../../swift/true.md). The property is only [true](../../swift/true.md) if both the connection’s input device format and output type support delivering camera intrinsics. In iOS 11, the [AVCaptureVideoDataOutput](../avcapturevideodataoutput.md) class is the only output type that supports camera intrinsics.

## See Also

### Delivering camera calibration settings

- [cameraIntrinsicMatrixDeliveryEnabled](iscameraintrinsicmatrixdeliveryenabled.md) — A Boolean value that indicates whether the connection can configure the capture pipeline to deliver camera intrinsics information.

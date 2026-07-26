---
title: isCameraIntrinsicMatrixDeliveryEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureconnection/iscameraintrinsicmatrixdeliveryenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureconnection/iscameraintrinsicmatrixdeliveryenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureconnection/iscameraintrinsicmatrixdeliveryenabled.json'
content_hash: 'sha256:8aa9878b4d9bd56f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureConnection](../avcaptureconnection.md)

# isCameraIntrinsicMatrixDeliveryEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the connection can configure the capture pipeline to deliver camera intrinsics information.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isCameraIntrinsicMatrixDeliveryEnabled: Bool { get set }
```

## Discussion

You can set this property to [true](../../swift/true.md) for a video connection if [cameraIntrinsicMatrixDeliverySupported](iscameraintrinsicmatrixdeliverysupported.md) is [true](../../swift/true.md), and only before calling the [AVCaptureSession](../avcapturesession.md) [- startRunning](<../avcapturesession/startrunning().md>) method. The default value is [false](../../swift/false.md).

Camera intrinsics describe the current imaging parameters of a capture device in ways that you can use to render overlays or perform computer vision tasks. If [true](../../swift/true.md), any [AVCaptureVideoDataOutput](../avcapturevideodataoutput.md) instance in this connection can include the [kCMSampleBufferAttachmentKey_CameraIntrinsicMatrix](../../coremedia/kcmsamplebufferattachmentkey_cameraintrinsicmatrix.md) attachment for each sample buffer it vends.

## See Also

### Delivering camera calibration settings

- [cameraIntrinsicMatrixDeliverySupported](iscameraintrinsicmatrixdeliverysupported.md) — A Boolean value that indicates whether the capture connection currently supports delivering camera intrinsics information.

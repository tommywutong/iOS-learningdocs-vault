---
title: videoZoomFactorUpscaleThreshold
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/videozoomfactorupscalethreshold
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/videozoomfactorupscalethreshold'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/videozoomfactorupscalethreshold.json'
content_hash: 'sha256:07d4394ccae56e0f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# videoZoomFactorUpscaleThreshold

<sub>Instance Property</sub>

A threshold at which the system upscales pixel data.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var videoZoomFactorUpscaleThreshold: CGFloat { get }
```

## Discussion

The device achieves a zoom effect by cropping around the center of the image captured by the sensor. At low zoom factors, the cropped images is equal to or larger than the output size. At higher zoom factors, the device must scale the cropped image up to the output size, resulting in a loss of image quality. This property indicates the factors at which upscaling occurs.

## See Also

### Determining zoom capabilities

- [systemRecommendedVideoZoomRange](systemrecommendedvideozoomrange.md) — The system’s recommended zoom range for this device format.
- [videoMaxZoomFactor](videomaxzoomfactor.md) — A maximum zoom factor the format allows.
- [secondaryNativeResolutionZoomFactors](secondarynativeresolutionzoomfactors.md) — The zoom factors at which this device transitions to secondary native resolution modes.
- [supportedVideoZoomRangesForDepthDataDelivery](supportedvideozoomrangesfordepthdatadelivery.md) — The zoom ranges that support the delivery of depth data.
- [zoomFactorsOutsideOfVideoZoomRangesForDepthDeliverySupported](zoomfactorsoutsideofvideozoomrangesfordepthdeliverysupported.md) — A Boolean value that indicates whether the format supports zoom factors outside the range supported for depth delivery.

---
title: zoomFactorsOutsideOfVideoZoomRangesForDepthDeliverySupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.2+, iPadOS 17.2+, Mac Catalyst 17.2+, macOS 14.2+, tvOS 17.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/zoomfactorsoutsideofvideozoomrangesfordepthdeliverysupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/zoomfactorsoutsideofvideozoomrangesfordepthdeliverysupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/zoomfactorsoutsideofvideozoomrangesfordepthdeliverysupported.json'
content_hash: 'sha256:a8a18ec6c9d98e10'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# zoomFactorsOutsideOfVideoZoomRangesForDepthDeliverySupported

<sub>Instance Property</sub>

A Boolean value that indicates whether the format supports zoom factors outside the range supported for depth delivery.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var zoomFactorsOutsideOfVideoZoomRangesForDepthDeliverySupported: Bool { get }
```

## Discussion

Setting a zoom factor outside the range defined by the [supportedVideoZoomFactorsForDepthDataDelivery](supportedvideozoomfactorsfordepthdatadelivery.md) property results in the system suspending depth data delivery. It resumes delivery when you set the zoom factor back to a supported value.

## See Also

### Determining zoom capabilities

- [systemRecommendedVideoZoomRange](systemrecommendedvideozoomrange.md) — The system’s recommended zoom range for this device format.
- [videoMaxZoomFactor](videomaxzoomfactor.md) — A maximum zoom factor the format allows.
- [videoZoomFactorUpscaleThreshold](videozoomfactorupscalethreshold.md) — A threshold at which the system upscales pixel data.
- [secondaryNativeResolutionZoomFactors](secondarynativeresolutionzoomfactors.md) — The zoom factors at which this device transitions to secondary native resolution modes.
- [supportedVideoZoomRangesForDepthDataDelivery](supportedvideozoomrangesfordepthdatadelivery.md) — The zoom ranges that support the delivery of depth data.

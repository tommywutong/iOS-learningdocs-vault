---
title: videoMaxZoomFactor
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/videomaxzoomfactor
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/videomaxzoomfactor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/videomaxzoomfactor.json'
content_hash: 'sha256:a05bc43d9e2c9c87'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# videoMaxZoomFactor

<sub>Instance Property</sub>

A maximum zoom factor the format allows.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var videoMaxZoomFactor: CGFloat { get }
```

## Discussion

A maximum factor of `1.0` indicates that the format isn’t capable of zooming.

## See Also

### Determining zoom capabilities

- [systemRecommendedVideoZoomRange](systemrecommendedvideozoomrange.md) — The system’s recommended zoom range for this device format.
- [videoZoomFactorUpscaleThreshold](videozoomfactorupscalethreshold.md) — A threshold at which the system upscales pixel data.
- [secondaryNativeResolutionZoomFactors](secondarynativeresolutionzoomfactors.md) — The zoom factors at which this device transitions to secondary native resolution modes.
- [supportedVideoZoomRangesForDepthDataDelivery](supportedvideozoomrangesfordepthdatadelivery.md) — The zoom ranges that support the delivery of depth data.
- [zoomFactorsOutsideOfVideoZoomRangesForDepthDeliverySupported](zoomfactorsoutsideofvideozoomrangesfordepthdeliverysupported.md) — A Boolean value that indicates whether the format supports zoom factors outside the range supported for depth delivery.

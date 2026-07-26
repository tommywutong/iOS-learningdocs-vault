---
title: secondaryNativeResolutionZoomFactors
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 17.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedeviceformat/secondarynativeresolutionzoomfactors
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedeviceformat/secondarynativeresolutionzoomfactors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedeviceformat/secondarynativeresolutionzoomfactors.json'
content_hash: 'sha256:ece5e2c3b3fa456c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [Format](../avcapturedevice/format.md)

# secondaryNativeResolutionZoomFactors

<sub>Instance Property</sub>

The zoom factors at which this device transitions to secondary native resolution modes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly) NSArray<NSNumber *> * secondaryNativeResolutionZoomFactors;
```

## Discussion

Devices that provide secondary native resolution zoom factors can switch their pixel sampling mode dynamically to produce high-fidelity images without upscaling at a fixed zoom factor beyond 1.0.

## See Also

### Determining zoom capabilities

- [systemRecommendedVideoZoomRange](systemrecommendedvideozoomrange.md) — The system’s recommended zoom range for this device format.
- [videoMaxZoomFactor](../avcapturedevice/format/videomaxzoomfactor.md) — A maximum zoom factor the format allows.
- [videoZoomFactorUpscaleThreshold](../avcapturedevice/format/videozoomfactorupscalethreshold.md) — A threshold at which the system upscales pixel data.
- [supportedVideoZoomRangesForDepthDataDelivery](supportedvideozoomrangesfordepthdatadelivery.md) — The zoom ranges that support the delivery of depth data.
- [AVZoomRange](../avzoomrange.md) — An object that defines an inclusive range of zoom values.
- [zoomFactorsOutsideOfVideoZoomRangesForDepthDeliverySupported](../avcapturedevice/format/zoomfactorsoutsideofvideozoomrangesfordepthdeliverysupported.md) — A Boolean value that indicates whether the format supports zoom factors outside the range supported for depth delivery.

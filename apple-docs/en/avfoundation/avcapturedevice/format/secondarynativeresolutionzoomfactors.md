---
title: secondaryNativeResolutionZoomFactors
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 17.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/secondarynativeresolutionzoomfactors
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/secondarynativeresolutionzoomfactors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/secondarynativeresolutionzoomfactors.json'
content_hash: 'sha256:5fbc958d9cdf6c7f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# secondaryNativeResolutionZoomFactors

<sub>Instance Property</sub>

The zoom factors at which this device transitions to secondary native resolution modes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
@nonobjc var secondaryNativeResolutionZoomFactors: [CGFloat] { get }
```

## Discussion

Devices that provide secondary native resolution zoom factors can switch their pixel sampling mode dynamically to produce high-fidelity images without upscaling at a fixed zoom factor beyond `1.0`.

## See Also

### Determining zoom capabilities

- [systemRecommendedVideoZoomRange](systemrecommendedvideozoomrange.md) — The system’s recommended zoom range for this device format.
- [videoMaxZoomFactor](videomaxzoomfactor.md) — A maximum zoom factor the format allows.
- [videoZoomFactorUpscaleThreshold](videozoomfactorupscalethreshold.md) — A threshold at which the system upscales pixel data.
- [supportedVideoZoomRangesForDepthDataDelivery](supportedvideozoomrangesfordepthdatadelivery.md) — The zoom ranges that support the delivery of depth data.
- [zoomFactorsOutsideOfVideoZoomRangesForDepthDeliverySupported](zoomfactorsoutsideofvideozoomrangesfordepthdeliverysupported.md) — A Boolean value that indicates whether the format supports zoom factors outside the range supported for depth delivery.

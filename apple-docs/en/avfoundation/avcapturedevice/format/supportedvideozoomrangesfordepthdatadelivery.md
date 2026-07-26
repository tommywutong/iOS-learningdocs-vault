---
title: supportedVideoZoomRangesForDepthDataDelivery
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.2+, iPadOS 17.2+, Mac Catalyst 17.2+, macOS 14.2+, tvOS 17.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/supportedvideozoomrangesfordepthdatadelivery
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/supportedvideozoomrangesfordepthdatadelivery'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/supportedvideozoomrangesfordepthdatadelivery.json'
content_hash: 'sha256:f543249cef2b2918'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# supportedVideoZoomRangesForDepthDataDelivery

<sub>Instance Property</sub>

The zoom ranges that support the delivery of depth data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
@nonobjc var supportedVideoZoomRangesForDepthDataDelivery: [ClosedRange<CGFloat>] { get }
```

## Discussion

Virtual devices support limited zoom ranges when delivering depth data to any output. If a device format has no [supportedDepthDataFormats](supporteddepthdataformats.md), the value of this property is an empty array.

The presence of one or more ranges where the minimum and maximum zoom factors aren’t equal means the system supports continuous zoom with depth. For example, if the value of this property contains the closed ranges `2...2` and `4...4`, the system only allows you to set zoom factors 2 and 4 when you enable depth data delivery. Setting a zoom factor outside these ranges results in an exception. Alternatively, a closed range of `2...5` indicates the system supports depth data delivery with zoom factors from 2 to 5. You can set a zoom factor outside this range, but results in a loss of depth data. Setting the zoom factor back to the supported range resumes depth data delivery.

When you enable depth data delivery, the effective [videoZoomFactorUpscaleThreshold](videozoomfactorupscalethreshold.md) is `1.0`, which means that all zoom factors that aren’t native zoom factors (see [virtualDeviceSwitchOverVideoZoomFactors](../virtualdeviceswitchovervideozoomfactors.md) and [secondaryNativeResolutionZoomFactors](secondarynativeresolutionzoomfactors.md)) result in digital upscaling.

## See Also

### Determining zoom capabilities

- [systemRecommendedVideoZoomRange](systemrecommendedvideozoomrange.md) — The system’s recommended zoom range for this device format.
- [videoMaxZoomFactor](videomaxzoomfactor.md) — A maximum zoom factor the format allows.
- [videoZoomFactorUpscaleThreshold](videozoomfactorupscalethreshold.md) — A threshold at which the system upscales pixel data.
- [secondaryNativeResolutionZoomFactors](secondarynativeresolutionzoomfactors.md) — The zoom factors at which this device transitions to secondary native resolution modes.
- [zoomFactorsOutsideOfVideoZoomRangesForDepthDeliverySupported](zoomfactorsoutsideofvideozoomrangesfordepthdeliverysupported.md) — A Boolean value that indicates whether the format supports zoom factors outside the range supported for depth delivery.

---
title: AVZoomRange
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.2+, iPadOS 17.2+, Mac Catalyst 17.2+, macOS 14.2+, tvOS 17.2+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avzoomrange
source_url: 'https://developer.apple.com/documentation/avfoundation/avzoomrange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avzoomrange.json'
content_hash: 'sha256:0431aca119ba94a0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVZoomRange

<sub>Class</sub>

An object that defines an inclusive range of zoom values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@interface AVZoomRange : NSObject
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

## Topics

### Inspecting a range

- [minZoomFactor](avzoomrange/minzoomfactor.md) — The range’s minimum zoom factor.
- [maxZoomFactor](avzoomrange/maxzoomfactor.md) — The range’s maximum zoom factor.
- [containsZoomFactor:](avzoomrange/containszoomfactor_.md) — Returns a Boolean value that indicates whether the specified zoom factor exists in the range.

## See Also

### Determining zoom capabilities

- [systemRecommendedVideoZoomRange](avcapturedeviceformat/systemrecommendedvideozoomrange.md) — The system’s recommended zoom range for this device format.
- [videoMaxZoomFactor](avcapturedevice/format/videomaxzoomfactor.md) — A maximum zoom factor the format allows.
- [videoZoomFactorUpscaleThreshold](avcapturedevice/format/videozoomfactorupscalethreshold.md) — A threshold at which the system upscales pixel data.
- [secondaryNativeResolutionZoomFactors](avcapturedeviceformat/secondarynativeresolutionzoomfactors.md) — The zoom factors at which this device transitions to secondary native resolution modes.
- [supportedVideoZoomRangesForDepthDataDelivery](avcapturedeviceformat/supportedvideozoomrangesfordepthdatadelivery.md) — The zoom ranges that support the delivery of depth data.
- [zoomFactorsOutsideOfVideoZoomRangesForDepthDeliverySupported](avcapturedevice/format/zoomfactorsoutsideofvideozoomrangesfordepthdeliverysupported.md) — A Boolean value that indicates whether the format supports zoom factors outside the range supported for depth delivery.
